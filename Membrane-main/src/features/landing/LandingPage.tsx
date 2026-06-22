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
            <span className="text-sm" style={{ color: '#a78bfa' }}>Now with MiniMax M2.7 & DeepSeek V4 Flash</span>
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
            <div key={i} className="card card-hover animate-fadeIn" style={{ animationDelay: `${i * 100}ms`, borderLeft: `3px solid ${feature.color}` }}>
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
