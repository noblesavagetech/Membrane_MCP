cat << 'INNER_EOF' > src/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg-primary: #0a0a0f;
  --bg-secondary: #12121a;
  --bg-tertiary: #1a1a24;
  --bg-card: #16161f;
  --accent-primary: #8b5cf6;
  --accent-secondary: #ec4899;
  --accent-tertiary: #06b6d4;
  --text-primary: #f4f4f5;
  --text-secondary: #a1a1aa;
  --text-muted: #71717a;
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-default: rgba(255, 255, 255, 0.1);
  --shadow-glow: 0 0 60px rgba(139, 92, 246, 0.15);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  font-family: 'Inter', system-ui, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
}

body { min-height: 100vh; position: relative; }
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse 80% 50% at 50% -20%, rgba(139,92,246,0.12) 0%, transparent 50%),
              radial-gradient(ellipse 60% 40% at 100% 100%, rgba(236,72,153,0.06) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

#root { min-height: 100vh; position: relative; z-index: 1; }

/* Typography */
h1, h2, h3 { font-weight: 600; line-height: 1.3; }
h1 { font-size: 2.5rem; } h2 { font-size: 2rem; } h3 { font-size: 1.5rem; }
.text-4xl { font-size: 2.25rem; } .text-3xl { font-size: 1.875rem; }
.text-2xl { font-size: 1.5rem; } .text-xl { font-size: 1.25rem; }
.text-lg { font-size: 1.125rem; } .text-sm { font-size: 0.875rem; }
.text-xs { font-size: 0.75rem; }
.font-bold { font-weight: 700; } .font-semibold { font-weight: 600; } .font-medium { font-weight: 500; }
.text-white { color: white; } .text-gray-300 { color: #d4d4d8; }
.text-gray-400 { color: #a1a1aa; } .text-gray-500 { color: #71717a; }
.text-gray-600 { color: #52525b; } .text-gray-700 { color: #3f3f46; }
.text-purple-400 { color: #a78bfa; } .text-pink-400 { color: #f472b6; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  gap: 8px; padding: 10px 20px; font-size: 0.9rem; font-weight: 500;
  border-radius: 10px; border: none; cursor: pointer;
  transition: all 0.2s ease; text-decoration: none;
}
.btn-primary {
  background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
  color: white; box-shadow: 0 4px 20px rgba(139, 92, 246, 0.3);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 30px rgba(139, 92, 246, 0.4); }
.btn-secondary {
  background: #1a1a24; color: #e4e4e7;
  border: 1px solid rgba(255,255,255,0.1);
}
.btn-secondary:hover { background: #242430; border-color: rgba(255,255,255,0.15); }
.btn-ghost { background: transparent; color: #a1a1aa; }
.btn-ghost:hover { background: rgba(255,255,255,0.05); color: #e4e4e7; }
.btn-sm { padding: 6px 12px; font-size: 0.8rem; }
.btn-lg { padding: 14px 28px; font-size: 1rem; }
.w-full { width: 100%; }

/* Inputs */
.input {
  width: 100%; padding: 12px 16px; font-size: 0.95rem;
  background: #1a1a24; border: 1px solid rgba(255,255,255,0.1);
  border-radius: 10px; color: #e4e4e7; outline: none;
  transition: all 0.2s ease; font-family: inherit;
}
.input:focus { border-color: #8b5cf6; box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15); }
.input::placeholder { color: #71717a; }
.textarea { resize: vertical; min-height: 120px; }

/* Cards */
.card {
  background: #16161f; border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px; padding: 24px; transition: all 0.3s ease;
}
.card-hover:hover {
  border-color: rgba(255,255,255,0.1); transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* Gradient Text */
.gradient-text {
  background: linear-gradient(to right, #a78bfa, #f472b6);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Layout */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.gap-1 { gap: 4px; } .gap-2 { gap: 8px; } .gap-3 { gap: 12px; }
.gap-4 { gap: 16px; } .gap-6 { gap: 24px; }

/* Spacing */
.p-2 { padding: 8px; } .p-3 { padding: 12px; } .p-4 { padding: 16px; }
.p-6 { padding: 24px; } .p-8 { padding: 32px; } .p-12 { padding: 48px; }
.px-4 { padding-left: 16px; padding-right: 16px; } .px-6 { padding-left: 24px; padding-right: 24px; }
.py-4 { padding-top: 16px; padding-bottom: 16px; } .py-12 { padding-top: 48px; padding-bottom: 48px; }
.pt-14 { padding-top: 56px; } .pt-24 { padding-top: 96px; } .pt-32 { padding-top: 128px; }
.pb-20 { padding-bottom: 80px; } .mt-1 { margin-top: 4px; } .mt-2 { margin-top: 8px; }
.mt-3 { margin-top: 12px; } .mt-4 { margin-top: 16px; } .mt-6 { margin-top: 24px; }
.mt-8 { margin-top: 32px; } .mb-2 { margin-bottom: 8px; } .mb-3 { margin-bottom: 12px; }
.mb-4 { margin-bottom: 16px; } .mb-6 { margin-bottom: 24px; } .mb-8 { margin-bottom: 32px; }

/* Grid */
.grid { display: grid; }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }

/* Width/Height */
.w-full { width: 100%; } .w-64 { width: 256px; } .w-80 { width: 320px; }
.w-16 { width: 64px; } .h-screen { height: 100vh; }
.h-10 { height: 40px; } .h-14 { height: 56px; }
.h-full { height: 100%; } .flex-1 { flex: 1; }
.min-h-screen { min-height: 100vh; }
.max-w-3xl { max-width: 768px; } .max-w-md { max-width: 28rem; }
.max-w-xs { max-width: 20rem; }

/* Position */
.fixed { position: fixed; } .relative { position: relative; }
.top-0 { top: 0; } .left-0 { left: 0; } .right-0 { right: 0; }
.z-50 { z-index: 50; }

/* Borders */
.border { border: 1px solid rgba(255,255,255,0.06); }
.border-r { border-right: 1px solid rgba(255,255,255,0.06); }
.border-l { border-left: 1px solid rgba(255,255,255,0.06); }
.border-t { border-top: 1px solid rgba(255,255,255,0.06); }
.border-b { border-bottom: 1px solid rgba(255,255,255,0.06); }
.border-l-2 { border-left-width: 2px; }
.border-l-3 { border-left-width: 3px; }
.rounded { border-radius: 10px; }
.rounded-lg { border-radius: 16px; }
.rounded-xl { border-radius: 24px; }
.rounded-full { border-radius: 9999px; }
.rounded-xl { border-radius: 12px; }

/* Overflow */
.overflow-hidden { overflow: hidden; }
.overflow-y-auto { overflow-y: auto; }

/* Backgrounds */
.bg-transparent { background: transparent; }
.bg-gray-900\/50 { background: rgba(17, 24, 39, 0.5); }

/* Editor Textarea - Critical Missing */
.editor-textarea {
  width: 100%; min-height: 400px; padding: 0;
  background: transparent; border: none; outline: none;
  color: #e4e4e7; font-family: 'JetBrains Mono', monospace;
  font-size: 0.95rem; line-height: 1.8; resize: none;
}
.editor-textarea::placeholder { color: #52525b; }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
  0%, 100% { opacity: 1; } 50% { opacity: 0.5; }
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
.animate-fadeIn { animation: fadeIn 0.5s ease forwards; }
.animate-pulse { animation: pulse 2s ease-in-out infinite; }
.animate-spin { animation: spin 1s linear infinite; }

.delay-50 { animation-delay: 50ms; }
.delay-100 { animation-delay: 100ms; }
.delay-150 { animation-delay: 150ms; }
.delay-200 { animation-delay: 200ms; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #12121a; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.25); }

/* Utilities */
.truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.line-clamp-2 {
  display: -webkit-box; -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; overflow: hidden;
}
.line-clamp-3 {
  display: -webkit-box; -webkit-line-clamp: 3;
  -webkit-box-orient: vertical; overflow: hidden;
}
.cursor-pointer { cursor: pointer; }
.text-center { text-align: center; }
.opacity-70 { opacity: 0.7; }

/* Responsive */
@media (max-width: 768px) {
  .grid-cols-2, .grid-cols-3 { grid-template-columns: 1fr; }
}

/* Navigation */
nav {
  background: rgba(10, 10, 15, 0.95);
  backdrop-filter: blur(12px);
}

/* Hover transitions */
.hover\:bg-white\/5:hover { background: rgba(255,255,255,0.05); }
.hover\:bg-white\/10:hover { background: rgba(255,255,255,0.1); }
.hover\:text-purple-400:hover { color: #a78bfa; }
.hover\:text-pink-400:hover { color: #f472b6; }
.hover\:text-white:hover { color: white; }
.hover\:text-red-400:hover { color: #f87171; }
.transition-colors { transition: color 0.2s, background 0.2s; }

/* Spinner */
.spinner {
  width: 16px; height: 16px;
  border: 2px solid rgba(255,255,255,0.2);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
}

/* Empty states */
.empty-state { display: flex; flex-direction: column; align-items: center; justify-content: center; }
INNER_EOF

cat << 'INNER_EOF' > src/services/api.ts
const getApiBase = () => {
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL
  return ''
}

export const API_BASE = getApiBase()

const getAuthHeaders = () => {
  const token = localStorage.getItem('token')
  return token ? { Authorization: \`Bearer \${token}\` } : {} as Record<string, string>
}

export const api = {
  async get<T>(path: string): Promise<T> {
    const res = await fetch(\`\${API_BASE}\${path}\`, { 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() } 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async post<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(\`\${API_BASE}\${path}\`, { 
      method: 'POST', 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() }, 
      body: data ? JSON.stringify(data) : undefined 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async postForm<T>(path: string, formData: FormData): Promise<T> {
    const res = await fetch(\`\${API_BASE}\${path}\`, { 
      method: 'POST', 
      headers: getAuthHeaders(), 
      body: formData 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async put<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(\`\${API_BASE}\${path}\`, { 
      method: 'PUT', 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() }, 
      body: data ? JSON.stringify(data) : undefined 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async delete(path: string): Promise<void> {
    const res = await fetch(\`\${API_BASE}\${path}\`, { 
      method: 'DELETE', 
      headers: getAuthHeaders() 
    })
    if (!res.ok) throw new Error(await res.text())
  },

  async chatStream(projectId: number, message: string, selectedText = '', model = 'default') {
    const params = new URLSearchParams({ message, selected_text: selectedText, model })
    const response = await fetch(\`\${API_BASE}/api/projects/\${projectId}/chat/stream?\${params}\`, { 
      headers: getAuthHeaders() 
    })
    if (!response.ok) throw new Error('Chat failed')
    return response.body
  },

  async generate(data: { prompt: string; story_id: number; chapter_id?: number; context_type: string; model?: string }) {
    return this.post<{ content: string }>('/api/ai/generate', data)
  },

  async getModels() {
    return this.get<{ id: string; name: string }[]>('/api/models')
  },
  
  // Project documents
  async getProjectDocuments(projectId: number) {
    return this.get<{ id: number; title: string; content: string }[]>(\`/api/projects/\${projectId}/documents\`)
  },
  
  async createProjectDocument(projectId: number, title: string) {
    return this.post<{ id: number; title: string; content: string }>(\`/api/projects/\${projectId}/documents\`, { title, content: '' })
  },
  
  async updateProjectDocument(projectId: number, documentId: number, data: { title?: string; content?: string }) {
    return this.put<{ id: number; title: string; content: string }>(\`/api/projects/\${projectId}/documents/\${documentId}\`, data)
  },
  
  async deleteProjectDocument(projectId: number, documentId: number) {
    return this.delete(\`/api/projects/\${projectId}/documents/\${documentId}\`)
  }
}
INNER_EOF

cat << 'INNER_EOF' > src/features/editor/EditorWorkspace.tsx
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
      const doc = await api.get<{ id: number; title: string; content: string }>(\`/api/projects/\${projectId}/document\`)
      if (doc) {
        setDocs([doc])
        setActiveDoc(doc)
      }
    } catch {
      // Create first document if none exists
      const doc = await api.post<{ id: number; title: string; content: string }>('/api/projects', { name: 'Untitled Project' })
      const newDoc = await api.get<{ id: number; title: string; content: string }>(\`/api/projects/\${projectId}/document\`)
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
        await api.put(\`/api/projects/\${projectId}/document\`, { content: updated.content })
        // Also update title via project endpoint
        await api.put(\`/api/projects/\${projectId}\`, { name: updated.title })
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
              className={\`group flex items-center p-2 rounded-lg cursor-pointer transition-all \${activeDoc?.id === d.id ? 'bg-purple-500/10 text-purple-400' : 'hover:bg-white/5 text-gray-400'}\`}
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
                <span className={\`text-xs \${saving ? 'text-purple-400 animate-pulse' : 'text-gray-500'}\`}>
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
            <div key={i} className={\`p-3 rounded-lg text-sm \${m.role === 'user' ? 'ml-8 bg-gradient-to-r from-purple-500/20 to-pink-500/20' : 'mr-8 bg-white/5'}\`}>
              <div className="text-xs opacity-50 mb-1">{m.role === 'user' ? 'You' : 'AI'}</div>
              <div className="whitespace-pre-wrap">{m.content}</div>
            </div>
          ))}
          <div ref={messagesEnd} />
        </div>
        <div className="p-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <div className="flex gap-2 mb-2">
            <button onClick={() => setChatInput(\`/improve \${selectedText}\`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Improve</button>
            <button onClick={() => setChatInput(\`/expand \${selectedText}\`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Expand</button>
            <button onClick={() => setChatInput(\`/simplify \${selectedText}\`)} disabled={!selectedText} className="btn btn-ghost btn-sm text-xs">Simplify</button>
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
INNER_EOF

cat << 'INNER_EOF' > src/features/stories/StoryEditor.tsx
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { api } from '../../services/api'

interface Story { id: number; title: string; genre: string; premise: string; chapters: Chapter[]; characters: Character[] }
interface Chapter { id: number; title: string; content: string; summary: string; order: number }
interface Character { id: number; name: string; role: string; traits: string }

export default function StoryEditor() {
  const { id } = useParams<{ id: string }>()
  const [story, setStory] = useState<Story | null>(null)
  const [activeChapter, setActiveChapter] = useState<number | null>(null)
  const [generating, setGenerating] = useState(false)
  const [showCharacters, setShowCharacters] = useState(false)
  const [showChapters, setShowChapters] = useState(true)
  const [newCharacter, setNewCharacter] = useState({ name: '', role: '', traits: '' })
  const [models, setModels] = useState<{id: string; name: string}[]>([])
  const [model, setModel] = useState('default')
  const [saving, setSaving] = useState(false)

  useEffect(() => { if (id) void loadStory(); void loadModels() }, [id])

  const loadStory = async () => {
    const data = await api.get<Story>(\`/api/stories/\${id}\`)
    setStory(data)
    if (data.chapters?.length && !activeChapter) setActiveChapter(data.chapters[0].id)
  }

  const loadModels = async () => setModels(await api.getModels())

  const updateChapter = async (content: string) => {
    if (!activeChapter) return
    setSaving(true)
    await api.put(\`/api/chapters/\${activeChapter}\`, { content })
    await loadStory()
    setSaving(false)
  }

  const createChapter = async () => {
    await api.post(\`/api/stories/\${id}/chapters\`, { title: \`Chapter \${(story?.chapters.length || 0) + 1}\` })
    await loadStory()
  }

  const generate = async () => {
    if (!story || !activeChapter) return
    setGenerating(true)
    try {
      const result = await api.generate({ prompt: 'Continue the story naturally with compelling prose', story_id: story.id, chapter_id: activeChapter, context_type: 'prose', model })
      const ch = story.chapters.find(c => c.id === activeChapter)
      await updateChapter(\`\${ch?.content || ''}\n\n\${result.content}\`)
    } finally { setGenerating(false) }
  }

  const summarizeChapter = async () => {
    if (!activeChapter) return
    await api.post(\`/api/chapters/\${activeChapter}/summarize\`)
    await loadStory()
  }

  const createCharacter = async (e: React.FormEvent) => {
    e.preventDefault()
    await api.post(\`/api/stories/\${id}/characters\`, newCharacter)
    setNewCharacter({ name: '', role: '', traits: '' })
    await loadStory()
  }

  const deleteCharacter = async (charId: number) => {
    await api.delete(\`/api/stories/\${id}/characters/\${charId}\`)
    await loadStory()
  }

  if (!story) return <div className="min-h-screen flex items-center justify-center" style={{ background: '#0a0a0f' }}><div className="spinner"></div></div>

  const chapter = story.chapters.find(c => c.id === activeChapter)

  return (
    <div className="flex h-screen" style={{ background: '#0a0a0f' }}>
      {/* Top Navigation */}
      <nav className="fixed top-0 left-0 right-0 h-14 flex items-center justify-between px-4" style={{ background: 'rgba(10,10,15,0.95)', backdropFilter: 'blur(12px)', borderBottom: '1px solid rgba(255,255,255,0.06)', zIndex: 50 }}>
        <div className="flex items-center gap-4">
          <Link to="/stories" className="btn btn-ghost btn-sm">←</Link>
          <div>
            <h1 className="font-semibold text-white">{story.title}</h1>
            <p className="text-xs text-gray-500">{story.genre}</p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <select value={model} onChange={e => setModel(e.target.value)} className="input" style={{ width: 'auto', padding: '4px 8px', fontSize: '0.8rem' }}>
            {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
          </select>
          <button onClick={() => setShowChapters(!showChapters)} className="btn btn-secondary btn-sm">Chapters</button>
          <button onClick={() => setShowCharacters(!showCharacters)} className="btn btn-secondary btn-sm">Characters</button>
        </div>
      </nav>

      {/* Chapters Sidebar */}
      {showChapters && (
        <aside className="w-64 pt-14 h-full overflow-y-auto border-r" style={{ background: '#12121a', borderColor: 'rgba(255,255,255,0.06)' }}>
          <div className="p-4">
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-sm font-semibold text-gray-400">Chapters</h3>
              <button onClick={createChapter} className="text-purple-400 hover:text-purple-300 text-sm">+ Add</button>
            </div>
            <div className="space-y-1">
              {story.chapters?.sort((a, b) => a.order - b.order).map(c => (
                <button key={c.id} onClick={() => setActiveChapter(c.id)}
                  className="w-full text-left px-3 py-2 rounded-lg text-sm transition"
                  style={{ background: c.id === activeChapter ? 'rgba(139,92,246,0.2)' : 'transparent', color: c.id === activeChapter ? '#a78bfa' : '#a1a1aa' }}>
                  {c.title}
                </button>
              ))}
            </div>
          </div>
        </aside>
      )}

      {/* Main Editor */}
      <main className="flex-1 pt-14 overflow-y-auto">
        {chapter && (
          <div className="p-6" style={{ maxWidth: '900px', margin: '0 auto' }}>
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-white">{chapter.title}</h2>
              <div className="flex gap-2">
                <button onClick={summarizeChapter} className="btn btn-secondary btn-sm">Summarize</button>
                <button onClick={generate} disabled={generating} className="btn btn-primary btn-sm">
                  {generating ? <span className="spinner"></span> : '✨ Generate'}
                </button>
              </div>
            </div>
            {chapter.summary && (
              <div className="mb-6 p-4 rounded-lg" style={{ background: 'rgba(139,92,246,0.1)', border: '1px solid rgba(139,92,246,0.2)' }}>
                <span className="text-xs text-purple-400 font-semibold">Summary:</span>
                <p className="text-sm text-gray-300 mt-1">{chapter.summary}</p>
              </div>
            )}
            <div className="flex items-center gap-2 mb-4 text-xs text-gray-500">
              <span>{saving ? 'Saving...' : 'Auto-save enabled'}</span>
            </div>
            <textarea value={chapter.content} onChange={e => void updateChapter(e.target.value)}
              className="w-full p-4 rounded-lg outline-none"
              style={{ background: '#0f0f14', color: '#e4e4e7', fontFamily: "'JetBrains Mono', monospace", fontSize: '0.95rem', lineHeight: '1.8', minHeight: '60vh' }}
              placeholder="Start writing your chapter..."
            />
          </div>
        )}
      </main>

      {/* Characters Sidebar */}
      {showCharacters && (
        <aside className="w-72 pt-14 h-full overflow-y-auto border-l" style={{ background: '#12121a', borderColor: 'rgba(255,255,255,0.06)' }}>
          <div className="p-4">
            <h3 className="text-sm font-semibold text-gray-400 mb-3">Characters</h3>
            <form onSubmit={createCharacter} className="mb-4 p-3 rounded-lg" style={{ background: 'rgba(255,255,255,0.03)' }}>
              <input value={newCharacter.name} onChange={e => setNewCharacter({...newCharacter, name: e.target.value})} placeholder="Name" className="input mb-2" style={{ fontSize: '0.85rem', padding: '8px' }} required />
              <input value={newCharacter.role} onChange={e => setNewCharacter({...newCharacter, role: e.target.value})} placeholder="Role (protagonist, villain...)" className="input mb-2" style={{ fontSize: '0.85rem', padding: '8px' }} />
              <input value={newCharacter.traits} onChange={e => setNewCharacter({...newCharacter, traits: e.target.value})} placeholder="Key traits" className="input mb-2" style={{ fontSize: '0.85rem', padding: '8px' }} />
              <button type="submit" className="btn btn-primary btn-sm w-full" style={{ background: 'linear-gradient(135deg, #ec4899, #8b5cf6)' }}>Add Character</button>
            </form>
            <div className="space-y-2">
              {story.characters?.map(c => (
                <div key={c.id} className="p-3 rounded-lg flex justify-between items-start" style={{ background: 'rgba(255,255,255,0.03)' }}>
                  <div>
                    <div className="font-medium">{c.name}</div>
                    <div className="text-xs text-pink-400">{c.role}</div>
                    {c.traits && <div className="text-xs text-gray-500 mt-1">{c.traits}</div>}
                  </div>
                  <button onClick={() => deleteCharacter(c.id)} className="text-gray-600 hover:text-red-400 text-xs">✕</button>
                </div>
              ))}
            </div>
          </div>
        </aside>
      )}
    </div>
  )
}
INNER_EOF

