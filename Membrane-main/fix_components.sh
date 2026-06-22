mkdir -p src/features/landing src/features/auth src/features/dashboard src/features/editor src/features/stories

cat << 'INNER_EOF' > src/features/landing/LandingPage.tsx
import { Link } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

export default function LandingPage() {
  const { user } = useAuth()

  return (
    <div className="min-h-screen" style={{ background: 'linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #0a0a0f 100%)' }}>
      <nav className="p-6 flex items-center justify-between" style={{ position: 'fixed', top: 0, left: 0, right: 0, zIndex: 50, background: 'rgba(10,10,15,0.8)', backdropFilter: 'blur(12px)', borderBottom: '1px solid rgba(255,255,255,0.06)' }}>
        <h1 className="text-2xl font-bold gradient-text">Membrane</h1>
        <div className="flex gap-4">
          {user ? (
            <Link to="/dashboard" className="btn btn-primary">Enter Workspace</Link>
          ) : (
            <Link to="/login" className="btn btn-primary">Get Started</Link>
          )}
        </div>
      </nav>

      <main className="pt-32 pb-20 px-6" style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <div className="text-center mb-16 animate-fadeIn">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full mb-6" style={{ background: 'rgba(139,92,246,0.15)', border: '1px solid rgba(139,92,246,0.3)' }}>
            <span className="w-2 h-2 rounded-full" style={{ background: '#10b981' }}></span>
            <span className="text-sm" style={{ color: '#a78bfa' }}>Now with MiniMax M2.5 & DeepSeek V4 Flash</span>
          </div>
          <h1 className="text-5xl font-bold mb-6" style={{ background: 'linear-gradient(to right, #fff, #a78bfa)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            Write with AI-Powered Precision
          </h1>
          <p className="text-xl text-gray-400 mb-8" style={{ maxWidth: '600px', margin: '0 auto' }}>
            A full-stack writing platform combining collaborative document editing with AI-powered story planning
          </p>
          <div className="flex gap-4 justify-center">
            <Link to="/login" className="btn btn-primary btn-lg">Start Writing</Link>
            <Link to="/dashboard" className="btn btn-secondary btn-lg">View Demo</Link>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-6" style={{ maxWidth: '900px', margin: '0 auto' }}>
          {[
            { title: 'Membrane Workspace', icon: '📝', desc: ['Real-time document editing', 'AI-powered chat assistance', 'File upload with semantic indexing', 'Vector-based memory'], color: '#8b5cf6' },
            { title: 'Story Engine', icon: '📚', desc: ['Multi-story management', 'Chapter organization', 'Character development', 'AI prose generation'], color: '#ec4899' }
          ].map((feature, i) => (
            <div key={i} className="card card-hover animate-fadeIn" style={{ animationDelay: \`\${i * 100}ms\`, borderLeft: \`3px solid \${feature.color}\` }}>
              <h3 className="text-xl font-semibold mb-4" style={{ color: feature.color }}>{feature.icon} {feature.title}</h3>
              <ul className="space-y-3">
                {feature.desc.map((item, j) => (
                  <li key={j} className="flex items-center gap-3 text-gray-400">
                    <span style={{ color: feature.color }}>▸</span> {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}
INNER_EOF

cat << 'INNER_EOF' > src/features/auth/LoginPage.tsx
import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

export default function LoginPage() {
  const [isLogin, setIsLogin] = useState(true)
  const [email, setEmail] = useState('')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const { login, signup } = useAuth()
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    try {
      if (isLogin) await login(email, password)
      else await signup(email, username, password)
      navigate('/dashboard')
    } catch { setError('Authentication failed. Try again.') }
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-4" style={{ background: 'radial-gradient(ellipse at top, #1a1a2e 0%, #0a0a0f 50%)' }}>
      <div className="w-full" style={{ maxWidth: '420px' }}>
        <div className="card p-8 animate-fadeIn" style={{ boxShadow: '0 0 60px rgba(139,92,246,0.15)' }}>
          <div className="text-center mb-8">
            <h1 className="text-2xl font-bold gradient-text mb-2">{isLogin ? 'Welcome Back' : 'Create Account'}</h1>
            <p className="text-gray-500">Start your writing journey</p>
          </div>

          {error && <div className="mb-4 p-3 rounded-lg" style={{ background: 'rgba(239,68,68,0.15)', border: '1px solid rgba(239,68,68,0.3)', color: '#f87171' }}>{error}</div>}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm text-gray-400 mb-2">Email</label>
              <input type="email" value={email} onChange={e => setEmail(e.target.value)} className="input" placeholder="you@example.com" required />
            </div>
            {!isLogin && (
              <div>
                <label className="block text-sm text-gray-400 mb-2">Username</label>
                <input type="text" value={username} onChange={e => setUsername(e.target.value)} className="input" placeholder="username" required />
              </div>
            )}
            <div>
              <label className="block text-sm text-gray-400 mb-2">Password</label>
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} className="input" placeholder="••••••••" required />
            </div>
            <button type="submit" className="btn btn-primary w-full" style={{ padding: '14px' }}>
              {isLogin ? 'Sign In' : 'Create Account'}
            </button>
          </form>

          <div className="mt-6 text-center">
            <span className="text-gray-500">{isLogin ? "Don't have an account?" : 'Already have an account?'}</span>
            <button onClick={() => setIsLogin(!isLogin)} className="ml-2 font-medium" style={{ color: '#a78bfa' }}>{isLogin ? 'Sign up' : 'Sign in'}</button>
          </div>

          <Link to="/" className="block mt-6 text-center text-gray-500 hover:text-white">← Back to Home</Link>
        </div>
      </div>
    </div>
  )
}
INNER_EOF

cat << 'INNER_EOF' > src/features/dashboard/Dashboard.tsx
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
    await api.delete(\`/api/projects/\${id}\`)
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
              <div key={p.id} className="card card-hover animate-fadeIn" style={{ animationDelay: \`\${i * 50}ms\` }}>
                <div className="flex items-start justify-between mb-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center" style={{ background: 'linear-gradient(135deg, #8b5cf6, #ec4899)' }}>📄</div>
                  <button onClick={() => deleteProject(p.id)} className="text-gray-600 hover:text-red-400">✕</button>
                </div>
                <Link to={\`/workspace/\${p.id}\`} className="text-lg font-semibold hover:text-purple-400 block mb-1">{p.name}</Link>
                <p className="text-sm text-gray-500 line-clamp-2">{p.description || 'No description'}</p>
                <div className="mt-4 pt-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.06)' }}>
                  <Link to={\`/workspace/\${p.id}\`} className="btn btn-secondary btn-sm w-full">Open Project</Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}
INNER_EOF

