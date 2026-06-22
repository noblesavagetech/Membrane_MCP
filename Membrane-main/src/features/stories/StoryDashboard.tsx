import { useEffect, useState, type FormEvent } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'
import { api } from '../../services/api'
import './StoryDashboard.css'

interface Story { 
  id: number
  title: string
  description: string
  updated_at: string
}

export default function StoryDashboard() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const [stories, setStories] = useState<Story[]>([])
  const [showCreateModal, setShowCreateModal] = useState(false)
  const [newStoryTitle, setNewStoryTitle] = useState('')
  const [newStoryDescription, setNewStoryDescription] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => { loadStories() }, [])

  const loadStories = async () => {
    setLoading(true)
    try {
      const response = await api.getStories()
      const normalizedStories = Array.isArray(response)
        ? response
        : ((response as { stories?: Story[] })?.stories ?? [])
      setStories(normalizedStories)
    } catch (err) {
      console.error('Failed to load stories:', err)
    } finally {
      setLoading(false)
    }
  }

  const closeCreateModal = () => {
    setShowCreateModal(false)
    setNewStoryTitle('')
    setNewStoryDescription('')
  }

  const handleCreateStory = async () => {
    if (!newStoryTitle.trim()) {
      alert('Title is required')
      return
    }

    try {
      await api.createStory(newStoryTitle.trim(), newStoryDescription.trim())
      closeCreateModal()
      await loadStories()
    } catch (err) {
      console.error('Failed to create story:', err)
      alert('Failed to create story')
    }
  }

  const handleCreateSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    await handleCreateStory()
  }

  const handleDeleteStory = async (storyId: number, title: string) => {
    if (!confirm(`Delete "${title}"?`)) return
    try {
      await api.deleteStory(storyId)
      await loadStories()
    } catch (err) {
      console.error('Failed to delete story:', err)
      alert('Failed to delete story')
    }
  }

  return (
    <div className="story-dashboard">
      <header className="dashboard-header">
        <div>
          <h1>Your Membrane</h1>
          <p className="dashboard-subtitle">{user?.username ? `Signed in as ${user.username}` : 'Story workspace'}</p>
        </div>

        <div className="dashboard-nav">
          <button
            type="button"
            className="nav-link"
            onClick={() => navigate('/dashboard')}
          >
            Projects
          </button>
          <Link to="/stories" className="nav-link active">Stories</Link>
          <button
            type="button"
            className="nav-link"
            onClick={logout}
          >
            Logout
          </button>
        </div>
      </header>

      <main className="dashboard-main">
        <div className="projects-header">
          <h2>Story Engine</h2>
          <button className="new-project-btn" onClick={() => setShowCreateModal(true)}>+ New Story</button>
        </div>

        {loading && (
          <div className="dashboard-empty">
            <h3>Loading stories...</h3>
          </div>
        )}

        {!loading && stories.length === 0 && (
          <div className="dashboard-empty">
            <h3>No stories yet</h3>
            <p>Create your first story to start writing.</p>
            <button className="new-project-btn" onClick={() => setShowCreateModal(true)}>Create First Story</button>
          </div>
        )}

        {!loading && stories.length > 0 && (
          <div className="projects-grid">
            {stories.map((story) => (
              <article key={story.id} className="project-card">
                <Link to={`/story/${story.id}`} className="project-link">
                  <div className="project-icon">📖</div>
                  <h3>{story.title}</h3>
                  <p>{story.description || 'No description yet.'}</p>
                  <span className="project-updated">
                    Updated {story.updated_at ? new Date(story.updated_at).toLocaleDateString() : 'just now'}
                  </span>
                </Link>
                <button
                  className="project-delete"
                  onClick={() => handleDeleteStory(story.id, story.title)}
                  aria-label={`Delete ${story.title}`}
                >
                  ×
                </button>
              </article>
            ))}
          </div>
        )}
      </main>

      {showCreateModal && (
        <div
          className="modal-overlay"
          onClick={(e) => {
            if (e.target === e.currentTarget) closeCreateModal()
          }}
        >
          <div className="modal-card">
            <h3>Create New Story</h3>
            <p>Start with a title and optional description.</p>

            <form onSubmit={handleCreateSubmit} className="story-form">
              <label htmlFor="new-story-title">Story Title</label>
              <input
                id="new-story-title"
                type="text"
                className="story-input"
                value={newStoryTitle}
                onChange={(e) => setNewStoryTitle(e.target.value)}
                placeholder="The Last City in the Storm"
                autoFocus
              />

              <label htmlFor="new-story-description">Description</label>
              <textarea
                id="new-story-description"
                className="story-input story-textarea"
                value={newStoryDescription}
                onChange={(e) => setNewStoryDescription(e.target.value)}
                placeholder="What is this story about?"
                rows={4}
              />

              <div className="modal-actions">
                <button type="button" className="modal-btn modal-btn-secondary" onClick={closeCreateModal}>
                  Cancel
                </button>
                <button type="submit" className="modal-btn modal-btn-primary">
                  Create Story
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
