cat << 'INNER_EOF' > src/features/editor/EditorWorkspace.tsx
import { useEffect, useState, useRef } from 'react'
import { useParams, Link } from 'react-router-dom'
import { api } from '../../services/api'
import '../../App.css'

interface Document { id: number; title: string; content: string; updated_at: string }

export default function EditorWorkspace() {
  const { projectId } = useParams()
  const [doc, setDoc] = useState<Document | null>(null)
  const [docs, setDocs] = useState<Document[]>([])
  const [saving, setSaving] = useState(false)
  const saveTimeout = useRef<ReturnType<typeof setTimeout> | null>(null)

  useEffect(() => {
    if (projectId) void loadDocs()
  }, [projectId])

  const loadDocs = async () => {
    const list = await api.get<Document[]>(\`/api/projects/\${projectId}/documents\`)
    setDocs(list)
    if (list.length > 0 && !doc) setDoc(list[0])
    else if (list.length === 0) createDoc()
  }

  const createDoc = async () => {
    const newDoc = await api.post<Document>(\`/api/projects/\${projectId}/documents\`, { title: 'Untitled Document', content: '' })
    setDocs([...docs, newDoc])
    setDoc(newDoc)
  }

  const updateDoc = (updates: Partial<Document>) => {
    if (!doc) return
    const updated = { ...doc, ...updates }
    setDoc(updated)
    setDocs(docs.map(d => d.id === doc.id ? updated : d))

    if (saveTimeout.current) clearTimeout(saveTimeout.current)
    setSaving(true)
    saveTimeout.current = setTimeout(async () => {
      await api.put(\`/api/documents/\${doc.id}\`, updates)
      setSaving(false)
    }, 1000)
  }

  const deleteDoc = async (id: number) => {
    if (!confirm('Delete document?')) return
    await api.delete(\`/api/documents/\${id}\`)
    if (doc?.id === id) setDoc(null)
    await loadDocs()
  }

  return (
    <div className="flex h-screen overflow-hidden text-gray-300" style={{ background: '#0a0a0f' }}>
      {/* Sidebar Navigation */}
      <aside className="w-16 flex flex-col items-center py-4 border-r" style={{ background: 'rgba(10,10,15,0.95)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <Link to="/dashboard" className="w-10 h-10 rounded-xl flex items-center justify-center mb-8 hover:bg-white/10 transition-colors" title="Dashboard">🏠</Link>
        <Link to="/stories" className="w-10 h-10 rounded-xl flex items-center justify-center mb-8 hover:bg-white/10 transition-colors" title="Story Engine">📚</Link>
        <button className="w-10 h-10 rounded-xl flex items-center justify-center mt-auto hover:bg-white/10 transition-colors" title="Settings">⚙️</button>
      </aside>

      {/* Document Sidebar */}
      <aside className="w-64 border-r flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b flex justify-between items-center" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-gray-200">Documents</h2>
          <button onClick={createDoc} className="btn btn-primary btn-sm rounded-full w-8 h-8 flex items-center justify-center">+</button>
        </div>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {docs.map(d => (
            <div key={d.id} className={\`group flex items-center justify-between p-2 rounded-lg cursor-pointer transition-all \${doc?.id === d.id ? 'bg-purple-500/10 text-purple-400' : 'hover:bg-white/5'}\`} onClick={() => setDoc(d)}>
              <span className="truncate flex-1">{d.title || 'Untitled'}</span>
              <button onClick={(e) => { e.stopPropagation(); deleteDoc(d.id); }} className="opacity-0 group-hover:opacity-100 text-gray-500 hover:text-red-400">✕</button>
            </div>
          ))}
        </div>
      </aside>

      {/* Main Editor */}
      <main className="flex-1 flex flex-col relative" style={{ background: '#0f0f15' }}>
        {doc ? (
          <>
            <header className="h-14 border-b flex items-center px-6 justify-between" style={{ borderColor: 'rgba(255,255,255,0.06)', background: 'rgba(10,10,15,0.8)', backdropFilter: 'blur(12px)' }}>
              <input value={doc.title} onChange={e => updateDoc({ title: e.target.value })} className="bg-transparent text-lg font-semibold border-none outline-none flex-1 truncate text-gray-200 placeholder-gray-600" placeholder="Document Title" style={{ color: '#fff' }} />
              <div className="flex items-center gap-4">
                <span className={\`text-xs \${saving ? 'text-purple-400 animate-pulse' : 'text-gray-500'}\`}>{saving ? 'Saving...' : 'Saved'}</span>
                <button className="btn btn-secondary btn-sm">Share</button>
              </div>
            </header>
            <div className="flex-1 overflow-y-auto p-12">
              <textarea value={doc.content} onChange={e => updateDoc({ content: e.target.value })} className="editor-textarea" placeholder="Start writing..." spellCheck={false} />
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-gray-500">
            <div className="text-center animate-fadeIn">
              <span className="text-4xl mb-4 block">📝</span>
              <p>Select or create a document to begin</p>
            </div>
          </div>
        )}
      </main>

      {/* AI Assistant Sidebar */}
      <aside className="w-80 border-l flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-gray-200">AI Assistant</h2>
          <p className="text-xs text-gray-500 mt-1">Context-aware suggestions</p>
        </div>
        <div className="flex-1 p-4 flex flex-col justify-end">
          <div className="card text-sm p-3 mb-4 border-l-2" style={{ borderColor: '#8b5cf6', background: 'rgba(139,92,246,0.05)' }}>
            I'm ready to help you write. Try asking me to expand on a concept or summarize your notes.
          </div>
          <input className="input text-sm" placeholder="Ask AI..." />
        </div>
      </aside>
    </div>
  )
}
INNER_EOF

cat << 'INNER_EOF' > src/features/stories/StoryDashboard.tsx
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../../services/api'

interface Story { id: number; title: string; genre: string; summary: string }

export default function StoryDashboard() {
  const [stories, setStories] = useState<Story[]>([])
  const [newTitle, setNewTitle] = useState('')

  useEffect(() => { void loadStories() }, [])
  const loadStories = async () => setStories(await api.get<Story[]>('/api/stories'))

  const createStory = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!newTitle.trim()) return
    await api.post('/api/stories', { title: newTitle, genre: 'Fiction', summary: '' })
    setNewTitle('')
    await loadStories()
  }

  return (
    <div className="min-h-screen" style={{ background: '#0a0a0f' }}>
      <nav className="flex items-center justify-between px-6 py-4 border-b" style={{ background: 'rgba(10,10,15,0.95)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="flex items-center gap-4">
          <h1 className="text-xl font-bold gradient-text">Story Engine</h1>
        </div>
        <Link to="/dashboard" className="btn btn-secondary btn-sm">← Back to Workspace</Link>
      </nav>

      <main className="pt-12 px-6" style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-2xl font-bold">Your Stories</h2>
            <p className="text-gray-500 mt-1">Manage novels, scripts, and narrative projects</p>
          </div>
        </div>

        <form onSubmit={createStory} className="mb-12 flex gap-4 bg-gray-900/50 p-6 rounded-xl border border-gray-800">
          <input value={newTitle} onChange={e => setNewTitle(e.target.value)} placeholder="New story title..." className="input" style={{ flex: 1, maxWidth: '400px' }} />
          <button type="submit" className="btn btn-primary" style={{ background: 'linear-gradient(135deg, #ec4899, #f43f5e)' }}>Create Story</button>
        </form>

        <div className="grid grid-cols-3 gap-6">
          {stories.map((s, i) => (
            <div key={s.id} className="card card-hover flex flex-col" style={{ animationDelay: \`\${i * 50}ms\`, minHeight: '200px' }}>
              <div className="flex-1">
                <span className="text-xs font-semibold px-2 py-1 rounded-full mb-3 inline-block" style={{ background: 'rgba(236,72,153,0.1)', color: '#ec4899' }}>{s.genre || 'Fiction'}</span>
                <Link to={\`/story/\${s.id}\`} className="text-xl font-bold hover:text-pink-400 block mb-2">{s.title}</Link>
                <p className="text-sm text-gray-500 line-clamp-3">{s.summary || 'No summary provided yet. Open the story to start developing your narrative.'}</p>
              </div>
              <div className="mt-4 pt-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
                <Link to={\`/story/\${s.id}\`} className="btn btn-secondary btn-sm w-full font-medium" style={{ borderColor: 'rgba(236,72,153,0.3)', color: '#ec4899' }}>Open Story Sandbox</Link>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}
INNER_EOF

cat << 'INNER_EOF' > src/features/stories/StoryEditor.tsx
import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { api } from '../../services/api'

interface Story { id: number; title: string; genre: string; summary: string }

export default function StoryEditor() {
  const { storyId } = useParams()
  const [story, setStory] = useState<Story | null>(null)

  useEffect(() => {
    if (storyId) void api.get<Story>(\`/api/stories/\${storyId}\`).then(setStory)
  }, [storyId])

  if (!story) return <div className="min-h-screen flex items-center justify-center text-gray-500">Loading story metadata...</div>

  return (
    <div className="flex h-screen overflow-hidden text-gray-300" style={{ background: '#0a0a0f' }}>
      <aside className="w-16 flex flex-col items-center py-4 border-r" style={{ background: 'rgba(10,10,15,0.95)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <Link to="/stories" className="w-10 h-10 rounded-xl flex items-center justify-center mb-8 hover:bg-white/10 transition-colors" title="Back to Stories">📚</Link>
      </aside>

      <aside className="w-64 border-r flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-gray-200">Sandbox</h2>
        </div>
        <div className="flex-1 p-2 space-y-1 text-sm">
          {['Overview', 'Characters', 'World Building', 'Plot Outline', 'Chapters'].map(item => (
            <div key={item} className="p-2 rounded hover:bg-white/5 cursor-pointer text-gray-400 hover:text-pink-400 transition-colors">
              {item}
            </div>
          ))}
        </div>
      </aside>

      <main className="flex-1 overflow-y-auto p-12" style={{ background: '#0f0f15' }}>
        <div className="max-w-3xl mx-auto">
          <input className="text-4xl font-bold bg-transparent border-none outline-none w-full mb-4 text-white placeholder-gray-700" value={story.title} onChange={e => setStory({ ...story, title: e.target.value })} />
          <div className="flex gap-4 mb-8">
            <input className="input max-w-xs" placeholder="Genre..." value={story.genre} onChange={e => setStory({ ...story, genre: e.target.value })} />
            <button className="btn btn-primary" style={{ background: 'linear-gradient(135deg, #ec4899, #f43f5e)' }}>Save Changes</button>
          </div>
          <div>
            <label className="block text-sm font-semibold text-pink-400 mb-2">Logline / Core Concept</label>
            <textarea className="editor-textarea min-h-[200px]" placeholder="What is this story about? Describe the core conflict..." value={story.summary} onChange={e => setStory({ ...story, summary: e.target.value })} />
          </div>
        </div>
      </main>

      <aside className="w-80 border-l flex flex-col" style={{ background: 'linear-gradient(180deg, #111118 0%, #0a0a0f 100%)', borderColor: 'rgba(255,255,255,0.06)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
          <h2 className="font-semibold text-pink-400">Story Engine AI</h2>
        </div>
        <div className="flex-1 p-4 flex flex-col justify-end">
          <div className="card text-sm p-3 mb-4 border-l-2" style={{ borderColor: '#ec4899', background: 'rgba(236,72,153,0.05)' }}>
            I can help you brainstorm character arcs, generate plot points, or critique pacing. What are we working on?
          </div>
          <input className="input text-sm" placeholder="Ask Story AI..." />
        </div>
      </aside>
    </div>
  )
}
INNER_EOF

