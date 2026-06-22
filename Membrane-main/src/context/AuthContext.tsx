import { createContext, useContext, useEffect, useState } from 'react'
import type { ReactNode } from 'react'
import { api } from '../services/api'

interface User { id: number; email: string; username: string }
interface AuthContextType { user: User | null; login: (email: string, password: string) => Promise<void>; signup: (email: string, username: string, password: string) => Promise<void>; logout: () => void }

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) api.get<User>('/api/auth/me').then(setUser).catch(() => localStorage.removeItem('token'))
  }, [])

  const login = async (email: string, password: string) => {
    const form = new FormData()
    form.append('email', email)
    form.append('password', password)
    const data = await api.postForm<{ token: string; user: User }>('/api/auth/login', form)
    localStorage.setItem('token', data.token)
    setUser(data.user)
  }

  const signup = async (email: string, username: string, password: string) => {
    const form = new FormData()
    form.append('email', email)
    form.append('username', username)
    form.append('password', password)
    const data = await api.postForm<{ token: string; user: User }>('/api/auth/signup', form)
    localStorage.setItem('token', data.token)
    setUser(data.user)
  }

  const logout = () => {
    localStorage.removeItem('token')
    setUser(null)
  }

  return <AuthContext.Provider value={{ user, login, signup, logout }}>{children}</AuthContext.Provider>
}

export const useAuth = () => {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
