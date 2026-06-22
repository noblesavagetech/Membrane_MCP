const getApiBase = () => {
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL
  return ''
}

export const API_BASE = getApiBase()

const getAuthHeaders = () => {
  const token = localStorage.getItem('token')
  return token ? { Authorization: `Bearer ${token}` } : {} as Record<string, string> as Record<string, string>
}

export const api = {
  async get<T>(path: string): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, { 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() } 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async post<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, { 
      method: 'POST', 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() }, 
      body: data ? JSON.stringify(data) : undefined 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async postForm<T>(path: string, formData: FormData): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, { 
      method: 'POST', 
      headers: getAuthHeaders(), 
      body: formData 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async put<T>(path: string, data?: unknown): Promise<T> {
    const res = await fetch(`${API_BASE}${path}`, { 
      method: 'PUT', 
      headers: { 'Content-Type': 'application/json', ...getAuthHeaders() }, 
      body: data ? JSON.stringify(data) : undefined 
    })
    if (!res.ok) throw new Error(await res.text())
    return res.json()
  },

  async delete(path: string): Promise<void> {
    const res = await fetch(`${API_BASE}${path}`, { 
      method: 'DELETE', 
      headers: getAuthHeaders() 
    })
    if (!res.ok) throw new Error(await res.text())
  },

  async chatStream(projectId: number, message: string, selectedText = '', model = 'default') {
    const params = new URLSearchParams({ message, selected_text: selectedText, model })
    const response = await fetch(`${API_BASE}/api/projects/${projectId}/chat/stream?${params}`, { 
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
    return this.get<{ id: number; title: string; content: string }[]>(`/api/projects/${projectId}/documents`)
  },
  
  async createProjectDocument(projectId: number, title: string) {
    return this.post<{ id: number; title: string; content: string }>(`/api/projects/${projectId}/documents`, { title, content: '' })
  },
  
  async updateProjectDocument(projectId: number, documentId: number, data: { title?: string; content?: string }) {
    return this.put<{ id: number; title: string; content: string }>(`/api/projects/${projectId}/documents/${documentId}`, data)
  },
  
  async deleteProjectDocument(projectId: number, documentId: number) {
    return this.delete(`/api/projects/${projectId}/documents/${documentId}`)
  },

  // Stories
  async getStories() {
    return this.get<any[]>('/api/stories')
  },

  async createStory(title: string, description: string = '') {
    return this.post<any>('/api/stories', { title, description })
  },

  async getStory(storyId: number) {
    return this.get<any>(`/api/stories/${storyId}`)
  },

  async updateStory(storyId: number, data: { title?: string; description?: string }) {
    return this.put<any>(`/api/stories/${storyId}`, data)
  },

  async deleteStory(storyId: number) {
    return this.delete(`/api/stories/${storyId}`)
  },

  // Chapters
  async createChapter(storyId: number, title: string) {
    return this.post<any>(`/api/stories/${storyId}/chapters`, { title })
  },

  async updateChapter(chapterId: number, data: { title?: string; text?: string; summary?: string }) {
    return this.put<any>(`/api/chapters/${chapterId}`, data)
  },

  async summarizeChapter(chapterId: number) {
    return this.post<{ summary: string }>(`/api/chapters/${chapterId}/summarize`, {})
  },

  // Characters
  async createCharacter(storyId: number, data: { name: string; role?: string; traits?: string; backstory?: string; description?: string }) {
    return this.post<any>(`/api/stories/${storyId}/characters`, data)
  },

  async getCharacters(storyId: number) {
    return this.get<any[]>(`/api/stories/${storyId}/characters`)
  },

  async updateCharacter(storyId: number, characterId: number, data: { name?: string; role?: string; traits?: string; backstory?: string; description?: string }) {
    return this.put<any>(`/api/stories/${storyId}/characters/${characterId}`, data)
  },

  async deleteCharacter(storyId: number, characterId: number) {
    return this.delete(`/api/stories/${storyId}/characters/${characterId}`)
  },

  // Beats
  async createBeat(chapterId: number, description: string, order: number = 0) {
    return this.post<any>(`/api/chapters/${chapterId}/beats`, { description, order })
  },

  async getBeats(chapterId: number) {
    return this.get<any[]>(`/api/chapters/${chapterId}/beats`)
  },

  async updateBeat(chapterId: number, beatId: number, data: { description?: string; order?: number }) {
    return this.put<any>(`/api/chapters/${chapterId}/beats/${beatId}`, data)
  },

  async deleteBeat(chapterId: number, beatId: number) {
    return this.delete(`/api/chapters/${chapterId}/beats/${beatId}`)
  },

  // World Building
  async createWorldElement(chapterId: number, category: string, description: string) {
    return this.post<any>(`/api/chapters/${chapterId}/worldbuilding`, { category, description })
  },

  async getWorldElements(chapterId: number) {
    return this.get<any[]>(`/api/chapters/${chapterId}/worldbuilding`)
  },

  async updateWorldElement(chapterId: number, elementId: number, data: { category?: string; description?: string }) {
    return this.put<any>(`/api/chapters/${chapterId}/worldbuilding/${elementId}`, data)
  },

  async deleteWorldElement(chapterId: number, elementId: number) {
    return this.delete(`/api/chapters/${chapterId}/worldbuilding/${elementId}`)
  },

  // Key Events
  async createKeyEvent(chapterId: number, description: string, order: number = 0) {
    return this.post<any>(`/api/chapters/${chapterId}/keyevents`, { description, order })
  },

  async getKeyEvents(chapterId: number) {
    return this.get<any[]>(`/api/chapters/${chapterId}/keyevents`)
  },

  async updateKeyEvent(chapterId: number, eventId: number, data: { description?: string; order?: number }) {
    return this.put<any>(`/api/chapters/${chapterId}/keyevents/${eventId}`, data)
  },

  async deleteKeyEvent(chapterId: number, eventId: number) {
    return this.delete(`/api/chapters/${chapterId}/keyevents/${eventId}`)
  },

  // Character Generation
  async generateCharacter(storyId: number, data: { generation_type: string; parameters: Record<string, string>; use_context: boolean; model: string }) {
    return this.post<{ content: string }>(`/api/stories/${storyId}/characters/generate`, { story_id: storyId, ...data })
  },

  // Worldbuilding Generation
  async generateWorldbuilding(storyId: number, data: { chapter_id: number; generation_type: string; parameters: Record<string, string>; use_context: boolean; model: string }) {
    return this.post<{ content: string }>(`/api/stories/${storyId}/worldbuilding/generate`, { story_id: storyId, ...data })
  },

  // MCP per-story config
  async getMCPConfig(storyId: number) {
    return this.get<{ provider: string; model: string; system_prompt: string; enabled: boolean }>(`/api/mcp/config/${storyId}`)
  },

  async updateMCPConfig(storyId: number, data: { provider?: string; model?: string; system_prompt?: string; enabled?: boolean }) {
    return this.put<{ provider: string; model: string; system_prompt: string; enabled: boolean }>(`/api/mcp/config/${storyId}`, data)
  },
}
