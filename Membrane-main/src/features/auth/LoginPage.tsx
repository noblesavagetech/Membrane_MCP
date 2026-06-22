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
