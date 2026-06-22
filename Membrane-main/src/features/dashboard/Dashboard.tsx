import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'
import { api } from '../../services/api'

interface Project { id: number; name: string; description: string; updated_at: string }

export default function Dashboard() {
  const [projects, setProjects] = useState<Project[]>([])
  const [newName, setNewName] = useState('')
  const { user, logout } = useAuth()

  useEffect(() => { void loadProjects() }, [])
  const loadProjects = async () => setProjects(await api.get<Project[]>('/api/projects'))

  const createProject = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!newName.trim()) return
    await api.post('/api/projects', { name: newName })
    setNewName('')
    await loadProjects()
  }

  const deleteProject = async (id: number) => {
    if (!confirm('Delete this project?')) return
    await api.delete(`/api/projects/${id}`)
    await loadProjects()
  }

  return (
    <div className="min-h-screen" style={{ background: '#0a0a0f' }}>
      <nav className="flex items-center justify-between px-6 py-4" style={{ position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, background: 'rgba(10,10,15,0.95)', backdropFilter: 'blur(12px)', borderBottom: '1px solid rgba(255,255,255,0.06)' }}>
        <div className="flex items-center gap-4">
          <h1 className="text-xl font-bold gradient-text">Membrane</h1>
          <span className="text-gray-500">/</span>
          <span className="text-gray-400">Workspace</span>
        </div>
        <div className="flex items-center gap-4">
          <Link to="/stories" className="btn btn-secondary btn-sm">
            <span>📚</span> Story Engine
          </Link>
          <span className="text-gray-500 text-sm">{user?.email}</span>
          <button onClick={logout} className="text-gray-400 hover:text-white text-sm">Logout</button>
        </div>
      </nav>

      <main className="pt-24 px-6" style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-2xl font-bold">Your Projects</h2>
            <p className="text-gray-500 mt-1">Manage your writing workspaces</p>
          </div>
        </div>

        <form onSubmit={createProject} className="mb-8 flex gap-4">
          <input value={newName} onChange={e => setNewName(e.target.value)} placeholder="New project name..." className="input" style={{ flex: 1, maxWidth: '400px' }} />
          <button type="submit" className="btn btn-primary">Create Project</button>
        </form>

        {projects.length === 0 ? (
          <div className="card text-center py-16 animate-fadeIn">
            <div className="text-4xl mb-4">📁</div>
            <h3 className="text-lg font-semibold mb-2">No projects yet</h3>
            <p className="text-gray-500 mb-4">Create your first project to get started</p>
            <button onClick={() => setNewName('My First Project')} className="btn btn-primary">Create Project</button>
          </div>
        ) : (
          <div className="grid grid-cols-3 gap-4">
            {projects.map((p, i) => (
              <div key={p.id} className="card card-hover animate-fadeIn" style={{ animationDelay: `${i * 50}ms` }}>
                <div className="flex items-start justify-between mb-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center" style={{ background: 'linear-gradient(135deg, #8b5cf6, #ec4899)' }}>📄</div>
                  <button onClick={() => deleteProject(p.id)} className="text-gray-600 hover:text-red-400">✕</button>
                </div>
                <Link to={`/workspace/${p.id}`} className="text-lg font-semibold hover:text-purple-400 block mb-1">{p.name}</Link>
                <p className="text-sm text-gray-500 line-clamp-2">{p.description || 'No description'}</p>
                <div className="mt-4 pt-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
                  <Link to={`/workspace/${p.id}`} className="btn btn-secondary btn-sm w-full">Open Project</Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}
