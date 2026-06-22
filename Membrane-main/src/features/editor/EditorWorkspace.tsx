import { useEffect, useState, useRef } from 'react'
import { useParams, Link } from 'react-router-dom'
import { api } from '../../services/api'

interface Document { id: number; title: string; content: string }

export default function EditorWorkspace() {
  const { projectId } = useParams<{ projectId: string }>()
  const [docs, setDocs] = useState<Document[]>([])
  const [activeDoc, setActiveDoc] = useState<Document | null>(null)
  const [saving, setSaving] = useState(false)
  const [models, setModels] = useState<{id: string; name: string}[]>([])
  const [model, setModel] = useState('default')
  const [messages, setMessages] = useState<{role: string; content: string}[]>([])
  const [chatInput, setChatInput] = useState('')
  const [streaming, setStreaming] = useState(false)
  const [selectedText, setSelectedText] = useState('')
  const saveTimeout = useRef<ReturnType<typeof setTimeout> | null>(null)
  const messagesEnd = useRef<HTMLDivElement>(null)

  useEffect(() => { 
    if (projectId) void loadDocs()
    void loadModels()
  }, [projectId])

  useEffect(() => { 
    messagesEnd.current?.scrollIntoView({ behavior: 'smooth' }) 
  }, [messages])

  const loadDocs = async () => {
    if (!projectId) return
    try {
      // Try the correct endpoint
      const doc = await api.get<{ id: number; title: string; content: string }>(`/api/projects/${projectId}/document`)
      if (doc) {
        setDocs([doc])
        setActiveDoc(doc)
      }
    } catch {
      // Create first document if none exists
      await api.post<{ id: number; title: string; content: string }>('/api/projects', { name: 'Untitled Project' })
      const newDoc = await api.get<{ id: number; title: string; content: string }>(`/api/projects/${projectId}/document`)
      if (newDoc) {
        setDocs([newDoc])
        setActiveDoc(newDoc)
      }
    }
  }

  const loadModels = async () => setModels(await api.getModels())

  const updateDoc = (updates: Partial<Document>) => {
    if (!activeDoc) return
    const updated = { ...activeDoc, ...updates }
    setActiveDoc(updated)
    setDocs(docs.map(d => d.id === activeDoc.id ? updated : d))

    if (saveTimeout.current) clearTimeout(saveTimeout.current)
    setSaving(true)
    saveTimeout.current = setTimeout(async () => {
      try {
        await api.put(`/api/projects/${projectId}/document`, { content: updated.content })
        // Also update title via project endpoint
        await api.put(`/api/projects/${projectId}`, { name: updated.title })
      } catch (e) { console.error(e) }
      setSaving(false)
    }, 1000)
  }

  const handleSelect = () => { 
    const sel = window.getSelection()?.toString() || ''
    if (sel) setSelectedText(sel)
  }

  const sendMessage = async () => {
    if (!chatInput.trim() || streaming || !projectId) return
    const userMsg = { role: 'user', content: chatInput }
    setMessages(m => [...m, userMsg])
    setChatInput('')
    setStreaming(true)
    try {
      const stream = await api.chatStream(parseInt(projectId), chatInput, selectedText, model)
      const reader = stream?.getReader()
      const decoder = new TextDecoder()
      const assistantMsg = { role: 'assistant', content: '' }
      setMessages(m => [...m, assistantMsg])
      while (reader) {
        const { done, value } = await reader.read()
        if (done) break
        const text = decoder.decode(value)
        for (const line of text.split('\n')) {
          if (!line.startsWith('data: ')) continue
          const data = line.slice(6)
          if (data === '[DONE]') continue
          try {
            const chunk = JSON.parse(data)
            if (chunk.content) { 
              assistantMsg.content += chunk.content
              setMessages(m => [...m.slice(0, -1), { ...assistantMsg }]) 
            }
          } catch {}
        }
      }
    } finally { setStreaming(false); setSelectedText('') }
  }

  return (
    <div className="flex h-screen overflow-hidden text-gray-300" style={{ background: '#0a0a0f' }}>
      {/* Sidebar */}
      <aside className="w-16 flex flex-col items-center py-4 border-r" style={{ background: 'rgba(10,10,15,0.95)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <Link to="/dashboard" className="w-10 h-10 rounded-xl flex items-center justify-center mb-8 hover:bg-white/10 transition-colors">🏠</Link>
        <Link to="/stories" className="w-10 h-10 rounded-xl flex items-center justify-center mb-8 hover:bg-white/10 transition-colors">📚</Link>
      </aside>

      {/* Document List */}
      <aside className="w-64 border-r flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b flex justify-between items-center" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-gray-200">Documents</h2>
        </div>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {docs.map(d => (
            <div key={d.id} 
              className={`group flex items-center p-2 rounded-lg cursor-pointer transition-all ${activeDoc?.id === d.id ? 'bg-purple-500/10 text-purple-400' : 'hover:bg-white/5 text-gray-400'}`}
              onClick={() => setActiveDoc(d)}>
              <span className="truncate flex-1">{d.title || 'Untitled'}</span>
            </div>
          ))}
        </div>
      </aside>

      {/* Main Editor */}
      <main className="flex-1 flex flex-col relative" style={{ background: '#0f0f15' }}>
        {activeDoc ? (
          <>
            <header className="h-14 border-b flex items-center px-6 justify-between" style={{ borderColor: 'rgba(255,255,255,0.06)', background: 'rgba(10,10,15,0.8)', backdropFilter: 'blur(12px)' }}>
              <input 
                value={activeDoc.title} 
                onChange={e => updateDoc({ title: e.target.value })} 
                className="bg-transparent text-lg font-semibold border-none outline-none flex-1 truncate text-white placeholder-gray-600" 
                placeholder="Document Title" 
              />
              <div className="flex items-center gap-4">
                <select value={model} onChange={e => setModel(e.target.value)} className="input" style={{ width: 'auto', padding: '4px 8px', fontSize: '0.8rem' }}>
                  {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>
                <span className={`text-xs ${saving ? 'text-purple-400 animate-pulse' : 'text-gray-500'}`}>
                  {saving ? 'Saving...' : 'Saved'}
                </span>
              </div>
            </header>
            <div className="flex-1 overflow-y-auto p-12">
              <textarea 
                value={activeDoc.content} 
                onChange={e => updateDoc({ content: e.target.value })} 
                onSelect={handleSelect}
                className="editor-textarea" 
                placeholder="Start writing your masterpiece..." 
                spellCheck={false} 
              />
            </div>
            {selectedText && (
              <div className="px-4 py-2" style={{ background: 'rgba(139,92,246,0.1)', borderTop: '1px solid rgba(139,92,246,0.3)' }}>
                <span className="text-sm text-purple-400">Selected: </span>
                <span className="text-sm text-gray-300">"{selectedText.slice(0, 80)}{selectedText.length > 80 ? '...' : ''}"</span>
              </div>
            )}
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-gray-500">
            <div className="text-center animate-fadeIn">
              <span className="text-4xl mb-4 block">📝</span>
              <p>Select or create a document</p>
            </div>
          </div>
        )}
      </main>

      {/* AI Chat Sidebar */}
      <aside className="w-80 border-l flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-gray-200">AI Assistant</h2>
          <p className="text-xs text-gray-500 mt-1">Context-aware writing help</p>
        </div>
        <div className="flex-1 overflow-y-auto p-4 space-y-3">
          {messages.length === 0 && (
            <div className="card text-sm p-3 border-l-2" style={{ borderColor: '#8b5cf6', background: 'rgba(139,92,246,0.05)' }}>
              I'm ready to help you write. Select text and ask me to improve, expand, or simplify it.
            </div>
          )}
          {messages.map((m, i) => (
            <div key={i} className={`p-3 rounded-lg text-sm ${m.role === 'user' ? 'ml-8 bg-gradient-to-r from-purple-500/20 to-pink-500/20' : 'mr-8 bg-white/5'}`}>
              <div className="text-xs opacity-50 mb-1">{m.role === 'user' ? 'You' : 'AI'}</div>
              <div className="whitespace-pre-wrap">{m.content}</div>
            </div>
          ))}
          <div ref={messagesEnd} />
        </div>
        <div className="p-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <div className="flex gap-2 mb-2">
            <button onClick={() => setChatInput(`/improve ${selectedText}`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Improve</button>
            <button onClick={() => setChatInput(`/expand ${selectedText}`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Expand</button>
            <button onClick={() => setChatInput(`/simplify ${selectedText}`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Simplify</button>
          </div>
          <div className="flex gap-2">
            <input 
              value={chatInput} 
              onChange={e => setChatInput(e.target.value)} 
              onKeyDown={e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); void sendMessage() } }}
              className="input text-sm" 
              placeholder="Ask AI..." 
              disabled={streaming} 
            />
            <button onClick={() => void sendMessage()} disabled={streaming || !chatInput.trim()} className="btn btn-primary btn-sm">
              {streaming ? <span className="spinner"></span> : '→'}
            </button>
          </div>
        </div>
      </aside>
    </div>
  )
}
