import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import LoginPage from './features/auth/LoginPage'
import Dashboard from './features/dashboard/Dashboard'
import EditorWorkspace from './features/editor/EditorWorkspace'
import LandingPage from './features/landing/LandingPage'
import StoryDashboard from './features/stories/StoryDashboard'
import StoryEditor from './features/stories/StoryEditor'

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuth()
  return user ? <>{children}</> : <Navigate to="/login" />
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
          <Route path="/stories" element={<ProtectedRoute><StoryDashboard /></ProtectedRoute>} />
          <Route path="/story/:id" element={<ProtectedRoute><StoryEditor /></ProtectedRoute>} />
          <Route path="/workspace/:projectId" element={<ProtectedRoute><EditorWorkspace /></ProtectedRoute>} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}
