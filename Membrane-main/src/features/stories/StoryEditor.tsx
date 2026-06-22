import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { api } from '../../services/api'
import CharacterGenerator from './CharacterGenerator'
import WorldbuildingGenerator from './WorldbuildingGenerator'
import './StoryEditor.css'

const defaultProsePrompt =
  "You are a narrative designer. Your task is to expand the provided series of beats into a complete, action-oriented scene.\n\nInstructions\nScene Generation: Write the entire scene in the third person. Expand each provided beat into a specific action, an unfolding event, or a piece of purposeful dialogue. The final output must be a unified, cohesive scene, not a simple list of expanded points.\n\nDialogue Rules: Dialogue must be direct and consistent with established character traits. It will be concise, moving the plot forward without unnecessary exposition or filler. Use of purple prose and flowery language is strictly forbidden.\n\nAction Rules: Prioritize physical actions and tangible events. Describe characters' movements and reactions to show their state of mind and propel the narrative.\n\nNarrative Flow: Ensure smooth, logical transitions between beats. The scene must unfold in a continuous and believable sequence."

const defaultBeatPrompt =
  `# NARRATIVE BLUEPRINT GENERATOR: REFINED

## PRIMARY OBJECTIVE

Transform provided story beats into a structured, actionable instruction set for prose generation. Your output is NOT prose. It is a detailed guide that tells another AI *what happens, what it means, and what key visual/sensory details to include*, allowing it to write the prose.

## CORE PRINCIPLE: HIERARCHY OF CONTEXT

**1. Provided Beats:** Your **ONLY** source for plot events. Expand these.
**2. Chapter Text:** Your source for **immediate tone, voice, and character positions.** Use this to maintain flow and consistency.
**3. Character Descriptions:** Your **reference for physical traits and outfits.** Use this to select details when instructed by the system below.
**4. Chapter Summary:** Background for continuity only.

## INSTRUCTION GENERATION RULES

### 1. DIALOGUE PROTOCOL: SHOW, DON'T TELL

- **Retain Core Intent:** Preserve the purpose of each line from the beat.
- **Expand to Exchange:** Create back-and-forth. Characters respond to what was *just said*.
- **Action Over Description:** Each dialogue turn gets **ONE** observable action that shows delivery or reaction.
- **Physical Detail Integration (The Key Change):**
    - Do **NOT** attach a physical detail to every line.
    - **DO** include a precise physical detail instruction **only when the action itself makes a character's trait *relevant*.**
    - **Rule of Thumb:** If the action involves a specific body part (a hand gesture, a step forward, a glance), you may reference the established description of that feature. If the action is general (a sigh, a shrug, a pause), skip the physical detail.

**Format:**

\`\`\`
[Character A]: "The line of dialogue."
↳ Instruction: [ONE observable action showing delivery.]
[Character B]: "The responsive line."
↳ Instruction: [ONE observable reaction.]
↳ Detail: [ONE precise physical characteristic ONLY if contextually motivated (e.g., "describe the width of his shoulders as he squares them").]
\`\`\`

### 2. PHYSICAL & OUTFIT DESCRIPTION MANDATE (CORRECTED)

- **Outfits Are Essential:** You **MUST** provide a complete outfit description for every character in the scene **at the start of the scene's instructions.** This is non-negotiable. It establishes visual setting.
- **Distribution, Not Omission:** The goal is to avoid *repeating* these descriptions in every block. They are stated once, upfront. The prose AI will recall them. Subsequent physical detail instructions are **selective enhancements.**
- **Strategic Physical Details:** After the initial outfit block, physical details are used **sparingly and purposefully:**
    - To **re-establish** a character's presence after a long absence in the scene.
    - To **highlight** a pivotal action where a specific trait is thematically or practically relevant.
    - To **vary** sensory input (don't just describe eyes; describe hands, posture, voice quality in turn).

### 3. THE "SHOW-DON'T-TELL" ENGINE

Replace all internal state labels with observable phenomena.

**Never Instruct:** "She was nervous."
**Always Instruct:**

- **Visible:** "Her fingers tap a rapid, uneven rhythm on the tabletop."
- **Audible:** "Her breath hitches before she speaks."
- **Spatial:** "He takes a half-step back, increasing the distance between them."

**The Prose AI's job** is to choose *how* to manifest this. Your job is to mandate the **observable effect.**

## OUTPUT STRUCTURE

### 🎬 SCENE [#]: [BEAT-DERIVED CORE CONFLICT]

**Tone:** [2-3 adjectives for the observable atmosphere.]
**Setting:** [Time, location. If continuous: "CONTINUOUS."]
**ENVIRONMENTAL NOTE:** [ONE sentence on a key environmental feature that will impact the scene (e.g., "The low-ceilinged room feels oppressive," or "Rain streaks the single window.")]

---

### CHARACTER ATTIRE (VISUAL ANCHORS)

**CRITICAL: WRITE THE FULL OUTFIT FOR EVERY CHARACTER PRESENT. NO SHORTCUTS.**

**[Character Name]:** [Complete outfit from undergarments to outerwear. Include colors, fabrics, fit. E.g., "Navy blue sports bra, black leggings, oversized grey hoodie with frayed cuffs, white running shoes."]
**[Character Name]:** [Full outfit description.]

---

### BEAT-BY-BEAT INSTRUCTION BLOCKS

**[BLOCK #] – [ACTION VERB]:** [E.g., CONFRONT, CONFIDE, DISCOVER]
**The Beat:** [One-sentence summary of the plot point from the provided beats.]

**Instruction:**
[The core directive for this narrative moment. Use the Action-Impact and Dialogue Protocols above. This is where you "show don't tell." Focus on what happens and what it causes.]

**Plot Goal:** [The concrete narrative purpose of this block. E.g., "Establishes a secret through a withheld glance," or "Reveals vulnerability via a misplaced object."]

---

## SYNTHESIS CHECKLIST

- [ ]  All dialogue preserves original intent and flows as a responsive exchange.
- [ ]  All emotional states are conveyed through observable actions/words only.
- [ ]  Outfit descriptions are complete for all characters at scene start.
- [ ]  Physical detail instructions (post-outfit) are **few and strategically motivated** by the action.
- [ ]  Instructions focus on **impact and consequence**, not just movement.
- [ ]  No instruction references "as before" or relies on unseen context. All necessary data is in the prompt.
- [ ]  The sequence of blocks clearly advances the plot from the provided beats.

## EXAMPLE (Applying the Corrections)

**BEAT:** "Elena confronts Marcus about the broken heirloom."

**INSTRUCTION BLOCK:[BLOCK 1] – CONFRONT: THE ACCUSATIONThe Beat:** Elena initiates a confrontation over the broken vase.
**Instruction:**

1. Elena places the shards of porcelain on the table between them. The sound is sharp, final.
2. **Elena:** "It was on the mantle. Just like it always is."
    - **Instruction:** Her voice is flat, devoid of the expected heat. She is stating a fact, not starting a fight.
3. **Marcus:** "It slipped."
    - **Instruction:** He doesn't look at the pieces. His gaze is fixed on a point just past her shoulder.
    - **Detail:** Describe the tension in his jawline, held rigidly still. *[MOTIVATED: The action (avoiding gaze) involves the head/face, and the tension is a key emotional signal.]*
4. **Elena:** "Things don't just slip."
    - **Instruction:** This is the push. She leans forward slightly, her hands flat on the table.
    - **Detail:** Describe the faded scar across her right knuckle, prominent as her hands press down. *[MOTIVATED: The action involves hands, and the scar is a character detail that gains thematic weight in a moment of accusation.]***Plot Goal:** To escalate the conflict from an event to an accusation of intent, using physical objects and restrained physicality as the battleground.`

const LAST_CHAPTER_CHUNK_CHARS = 2500

// Collapsible Section Component
function CollapsibleSection({ title, children, icon, badge }: { title: string; children: React.ReactNode; icon?: string; badge?: number }) {
  const [isOpen, setIsOpen] = useState(true)
  return (
    <section className="se-section">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="se-section-header"
        type="button"
      >
        <div className="se-section-title-wrap">
          {icon && <span className="se-section-icon">{icon}</span>}
          <span className="se-section-title">{title}</span>
          {badge !== undefined && badge > 0 && (
            <span className="se-section-badge">{badge}</span>
          )}
        </div>
        <span className="se-section-arrow">{isOpen ? '▼' : '▶'}</span>
      </button>
      {isOpen && <div className="se-section-body">{children}</div>}
    </section>
  )
}

export default function StoryEditor() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [story, setStory] = useState<any>(null)
  const [currentChapter, setCurrentChapter] = useState<any>(null)
  const [chapterText, setChapterText] = useState('')
  const [chapterTitle, setChapterTitle] = useState('')
  const [chapterSummary, setChapterSummary] = useState('')
  
  // Chapter-scoped data
  const [beats, setBeats] = useState<any[]>([])
  const [worldElements, setWorldElements] = useState<any[]>([])
  const [keyEvents, setKeyEvents] = useState<any[]>([])
  
  // Story-scoped data
  const [characters, setCharacters] = useState<any[]>([])
  const [newCharacterName, setNewCharacterName] = useState('')
  const [newCharacterTraits, setNewCharacterTraits] = useState('')
  const [newCharacterBackstory, setNewCharacterBackstory] = useState('')
  
  // AI Generation
  const [aiProsePrompt, setAiProsePrompt] = useState(defaultProsePrompt)
  const [aiProseInput, setAiProseInput] = useState('')
  const [aiProseResult, setAiProseResult] = useState('')
  const [aiProseModel, setAiProseModel] = useState('anthropic/claude-sonnet-4.5')
  const [selectedCharactersForProse, setSelectedCharactersForProse] = useState<number[]>([])
  const [generatingProse, setGeneratingProse] = useState(false)
  const [charactersExpandedForProse, setCharactersExpandedForProse] = useState(false)
  
  const [aiBeatPrompt, setAiBeatPrompt] = useState(defaultBeatPrompt)
  const [aiBeatInput, setAiBeatInput] = useState('')
  const [aiBeatResult, setAiBeatResult] = useState('')
  const [aiBeatModel, setAiBeatModel] = useState('anthropic/claude-sonnet-4.5')
  const [selectedCharactersForBeat, setSelectedCharactersForBeat] = useState<number[]>([])
  const [generatingBeat, setGeneratingBeat] = useState(false)
  const [charactersExpandedForBeat, setCharactersExpandedForBeat] = useState(false)
  
  const [queryPrompt, setQueryPrompt] = useState('')
  const [queryResult, setQueryResult] = useState('')
  const [queryModel, setQueryModel] = useState('anthropic/claude-sonnet-4.5')
  const [querying, setQuerying] = useState(false)
  
  const [models, setModels] = useState<any[]>([])
  const [saveMessage, setSaveMessage] = useState('')
  
  // Inline add forms
  const [newBeatDesc, setNewBeatDesc] = useState('')
  const [newWorldCategory, setNewWorldCategory] = useState('')
  const [newWorldDesc, setNewWorldDesc] = useState('')
  const [newEventDesc, setNewEventDesc] = useState('')

  // MCP per-story config
  const [mcpConfig, setMCPConfig] = useState({ provider: 'openrouter', model: 'default', system_prompt: '', enabled: true })
  const [mcpSaveMsg, setMCPSaveMsg] = useState('')
  const [mcpToolCalls, setMCPToolCalls] = useState<any[]>([])

  useEffect(() => {
    if (id) {
      loadStory()
      loadModels()
    }
  }, [id])

  useEffect(() => {
    if (currentChapter) {
      loadChapterData()
    }
  }, [currentChapter?.id])

  const loadStory = async () => {
    try {
      const data = await api.getStory(Number(id))
      setStory(data)
      
      // Auto-create chapter if none exist
      if (!data.chapters || data.chapters.length === 0) {
        await api.createChapter(data.id, `${data.title} - Chapter 1`)
        const refreshed = await api.getStory(Number(id))
        setStory(refreshed)
        if (refreshed.chapters && refreshed.chapters.length > 0) {
          switchToChapter(refreshed.chapters[0])
        }
      } else {
        switchToChapter(data.chapters[0])
      }
      
      // Load story-level characters
      const chars = await api.getCharacters(data.id)
      setCharacters(chars)

      // Load MCP config for this story
      try {
        const cfg = await api.getMCPConfig(data.id)
        setMCPConfig(cfg)
      } catch {
        // MCP config may not exist yet — use defaults
        setMCPConfig({ provider: 'openrouter', model: 'default', system_prompt: '', enabled: true })
      }
    } catch (err) {
      console.error('Failed to load story:', err)
    }
  }

  const loadModels = async () => {
    try {
      const data = await api.getModels()
      setModels(data)
    } catch (err) {
      console.error('Failed to load models:', err)
    }
  }

  const switchToChapter = (chapter: any) => {
    setCurrentChapter(chapter)
    setChapterText(chapter.text || '')
    setChapterTitle(chapter.title || '')
    setChapterSummary(chapter.summary || '')
  }

  const loadChapterData = async () => {
    if (!currentChapter) return
    try {
      const [beatsData, worldData, eventsData] = await Promise.all([
        api.getBeats(currentChapter.id),
        api.getWorldElements(currentChapter.id),
        api.getKeyEvents(currentChapter.id)
      ])
      setBeats(beatsData)
      setWorldElements(worldData)
      setKeyEvents(eventsData)
    } catch (err) {
      console.error('Failed to load chapter data:', err)
    }
  }

  const handleAddChapter = async () => {
    try {
      const chapterCount = story.chapters?.length || 0
      await api.createChapter(story.id, `Chapter ${chapterCount + 1}`)
      await loadStory()
    } catch (err) {
      console.error('Failed to create chapter:', err)
    }
  }

  const handleSaveChapter = async () => {
    try {
      await api.updateChapter(currentChapter.id, { title: chapterTitle, text: chapterText })
      const refreshed = await api.getStory(story.id)
      setStory(refreshed)
      const updated = refreshed.chapters.find((c: any) => c.id === currentChapter.id)
      if (updated) {
        setCurrentChapter(updated)
      }
      setSaveMessage('Chapter saved!')
      setTimeout(() => setSaveMessage(''), 2000)
    } catch (err) {
      console.error('Failed to save chapter:', err)
      setSaveMessage('Save failed')
    }
  }

  const handleSaveSummary = async () => {
    try {
      await api.updateChapter(currentChapter.id, { summary: chapterSummary })
      const refreshed = await api.getStory(story.id)
      setStory(refreshed)
      const updated = refreshed.chapters.find((c: any) => c.id === currentChapter.id)
      if (updated) {
        setCurrentChapter(updated)
        setChapterSummary(updated.summary)
      }
      setSaveMessage('Summary saved!')
      setTimeout(() => setSaveMessage(''), 2000)
    } catch (err) {
      console.error('Failed to save summary:', err)
    }
  }

  const handleSummarizeChapter = async () => {
    if (!currentChapter || !story) return
    try {
      // Route through MCP so the LLM gets full context and tools
      const result = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: story.id,
          chapter_id: currentChapter.id,
          prompt: 'Summarize the current chapter concisely, capturing key plot points, character arcs, and emotional tone.',
          context_type: 'summary',
          model: 'google/gemini-3.1-flash-lite-preview'
        }
      })
      const summary = result?.result?.data?.content || result?.result?.summary || result?.content || 'Summary generated via MCP.'
      setChapterSummary(summary)
      setSaveMessage('Summary generated via MCP!')
      setTimeout(() => setSaveMessage(''), 2000)

      // Log the tool call for the debug panel
      setMCPToolCalls(prev => [...prev, {
        tool: 'summarize_chapter',
        args: { chapter_id: currentChapter.id },
        time: new Date().toLocaleTimeString()
      }])
    } catch (err) {
      console.error('Failed to summarize:', err)
      setSaveMessage('Summary failed')
    }
  }

  // Character CRUD
  const handleAddCharacter = async () => {
    const name = newCharacterName.trim()
    if (!name) {
      alert('Character name is required.')
      return
    }
    try {
      await api.createCharacter(story.id, {
        name,
        traits: newCharacterTraits.trim(),
        backstory: newCharacterBackstory.trim(),
      })
      const chars = await api.getCharacters(story.id)
      setCharacters(chars)
      setNewCharacterName('')
      setNewCharacterTraits('')
      setNewCharacterBackstory('')
    } catch (err) {
      console.error('Failed to add character:', err)
    }
  }

  const handleUpdateCharacter = async (charId: number) => {
    const char = characters.find(c => c.id === charId)
    if (!char) return
    const name = (document.getElementById(`char-name-${charId}`) as HTMLInputElement)?.value
    const traits = (document.getElementById(`char-traits-${charId}`) as HTMLTextAreaElement)?.value
    const backstory = (document.getElementById(`char-backstory-${charId}`) as HTMLTextAreaElement)?.value
    try {
      await api.updateCharacter(story.id, charId, { name, traits, backstory })
      const chars = await api.getCharacters(story.id)
      setCharacters(chars)
    } catch (err) {
      console.error('Failed to update character:', err)
    }
  }

  const handleDeleteCharacter = async (charId: number, name: string) => {
    if (!confirm(`Delete character "${name}"?`)) return
    try {
      await api.deleteCharacter(story.id, charId)
      setCharacters(characters.filter(c => c.id !== charId))
    } catch (err) {
      console.error('Failed to delete character:', err)
    }
  }

  // Beat CRUD
  const handleAddBeat = async () => {
    const description = newBeatDesc.trim()
    if (!description) return
    try {
      await api.createBeat(currentChapter.id, description, beats.length)
      await loadChapterData()
      setNewBeatDesc('')
    } catch (err) {
      console.error('Failed to add beat:', err)
    }
  }

  const handleUpdateBeat = async (beatId: number) => {
    const description = (document.getElementById(`beat-desc-${beatId}`) as HTMLInputElement)?.value
    const order = parseInt((document.getElementById(`beat-order-${beatId}`) as HTMLInputElement)?.value || '0')
    try {
      await api.updateBeat(currentChapter.id, beatId, { description, order })
      await loadChapterData()
    } catch (err) {
      console.error('Failed to update beat:', err)
    }
  }

  const handleDeleteBeat = async (beatId: number) => {
    if (!confirm('Delete this beat?')) return
    try {
      await api.deleteBeat(currentChapter.id, beatId)
      await loadChapterData()
    } catch (err) {
      console.error('Failed to delete beat:', err)
    }
  }

  // World Element CRUD
  const handleAddWorldElement = async () => {
    const category = newWorldCategory.trim()
    const description = newWorldDesc.trim()
    if (!category || !description) return
    try {
      await api.createWorldElement(currentChapter.id, category, description)
      await loadChapterData()
      setNewWorldCategory('')
      setNewWorldDesc('')
    } catch (err) {
      console.error('Failed to add world element:', err)
    }
  }

  const handleUpdateWorldElement = async (elemId: number) => {
    const category = (document.getElementById(`world-cat-${elemId}`) as HTMLInputElement)?.value
    const description = (document.getElementById(`world-desc-${elemId}`) as HTMLTextAreaElement)?.value
    try {
      await api.updateWorldElement(currentChapter.id, elemId, { category, description })
      await loadChapterData()
    } catch (err) {
      console.error('Failed to update world element:', err)
    }
  }

  const handleDeleteWorldElement = async (elemId: number) => {
    if (!confirm('Delete this world element?')) return
    try {
      await api.deleteWorldElement(currentChapter.id, elemId)
      await loadChapterData()
    } catch (err) {
      console.error('Failed to delete world element:', err)
    }
  }

  // Key Event CRUD
  const handleAddKeyEvent = async () => {
    const description = newEventDesc.trim()
    if (!description) return
    try {
      await api.createKeyEvent(currentChapter.id, description, keyEvents.length)
      await loadChapterData()
      setNewEventDesc('')
    } catch (err) {
      console.error('Failed to add key event:', err)
    }
  }

  const handleUpdateKeyEvent = async (eventId: number) => {
    const description = (document.getElementById(`event-desc-${eventId}`) as HTMLInputElement)?.value
    const order = parseInt((document.getElementById(`event-order-${eventId}`) as HTMLInputElement)?.value || '0')
    try {
      await api.updateKeyEvent(currentChapter.id, eventId, { description, order })
      await loadChapterData()
    } catch (err) {
      console.error('Failed to update key event:', err)
    }
  }

  const handleDeleteKeyEvent = async (eventId: number) => {
    if (!confirm('Delete this key event?')) return
    try {
      await api.deleteKeyEvent(currentChapter.id, eventId)
      await loadChapterData()
    } catch (err) {
      console.error('Failed to delete key event:', err)
    }
  }

  // MCP per-story config
  const handleMCPConfigChange = (changes: Partial<typeof mcpConfig>) => {
    setMCPConfig(prev => ({ ...prev, ...changes }))
  }

  const saveMCPConfig = async () => {
    if (!story) return
    try {
      const saved = await api.updateMCPConfig(story.id, mcpConfig)
      setMCPConfig(saved)
      setMCPSaveMsg('已儲存')
      setTimeout(() => setMCPSaveMsg(''), 2000)
    } catch (err) {
      console.error('Failed to save MCP config:', err)
      setMCPSaveMsg('儲存失敗')
    }
  }

  const appendOutputToChapter = (output: string, source: string) => {
    const clean = output.trim()
    if (!clean) {
      alert(`No ${source} output to insert yet.`)
      return
    }

    setChapterText(prev => {
      const base = prev.trimEnd()
      return base ? `${base}\n\n${clean}` : clean
    })
    setSaveMessage(`${source} inserted into chapter`) 
    setTimeout(() => setSaveMessage(''), 1800)
  }

  const copyOutput = async (output: string, source: string) => {
    const clean = output.trim()
    if (!clean) {
      alert(`No ${source} output to copy yet.`)
      return
    }
    try {
      await navigator.clipboard.writeText(clean)
      setSaveMessage(`${source} copied`)
      setTimeout(() => setSaveMessage(''), 1800)
    } catch {
      alert('Clipboard copy failed. Please copy manually from the output box.')
    }
  }

  const getLastChapterChunk = (text: string) => {
    const chunk = text.slice(-LAST_CHAPTER_CHUNK_CHARS).trim()
    return chunk || '(No chapter text yet.)'
  }

  // AI Generation
  const handleGenerateProse = async () => {
    if (!aiProsePrompt.trim()) {
      alert('System Prompt is required for prose generation.')
      return
    }
    if (!aiProseInput.trim()) {
      alert('Scene Input is required for prose generation.')
      return
    }

    setGeneratingProse(true)
    try {
      const selectedChars = characters.filter(c => selectedCharactersForProse.includes(c.id))
      const chapterExcerpt = getLastChapterChunk(chapterText)
      
      const contextPrompt = `
STORY CONTEXT:
Chapter Summary: ${chapterSummary}

Characters: ${selectedChars.map(c => `${c.name} (${c.traits || ''}) - ${c.backstory || ''}`).join('; ')}

Beats: ${beats.map((b, i) => `${i+1}. ${b.description}`).join('; ')}

Key Events: ${keyEvents.map((e, i) => `${i+1}. ${e.description}`).join('; ')}

Last Chapter Chunk (most recent ${LAST_CHAPTER_CHUNK_CHARS} chars):
${chapterExcerpt}

World-Building: ${worldElements.map(w => `[${w.category}] ${w.description}`).join('; ')}

---
${aiProsePrompt}

Scene Input: ${aiProseInput}
`
      
      // Route through MCP so the LLM gets full tool access (get_story, update_beat, query_context, etc.)
      // while still letting the user pick the exact model they want.
      const result = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: story.id,
          chapter_id: currentChapter.id,
          prompt: contextPrompt,
          context_type: 'prose',
          model: aiProseModel
        }
      })
      const content = result?.result?.data?.content || result?.result?.content || result?.content || 'No prose output returned by the model.'
      setAiProseResult(content)

      // Log the tool calls returned by the MCP server
      const toolCalls = result?.tool_calls || result?.result?.tool_calls || [{
        tool: 'generate_prose',
        args: { model: aiProseModel, context_type: 'prose' },
        time: new Date().toLocaleTimeString()
      }]
      setMCPToolCalls(prev => [...prev, ...toolCalls])
    } catch (err) {
      console.error('Failed to generate prose:', err)
      setAiProseResult('Generation failed. Check API key/model or try again with a shorter input.')
    } finally {
      setGeneratingProse(false)
    }
  }

  const handleGenerateBeatExpansion = async () => {
    if (!aiBeatPrompt.trim()) {
      alert('System Prompt is required for beat expansion.')
      return
    }
    if (!aiBeatInput.trim()) {
      alert('Beat / Scene Input is required for beat expansion.')
      return
    }

    setGeneratingBeat(true)
    try {
      const selectedChars = characters.filter(c => selectedCharactersForBeat.includes(c.id))
      const chapterExcerpt = getLastChapterChunk(chapterText)
      
      const contextPrompt = `
STORY CONTEXT:
Chapter Summary: ${chapterSummary}

Characters: ${selectedChars.map(c => `${c.name} (${c.traits || ''}) - ${c.backstory || ''}`).join('; ')}

Beats: ${beats.map((b, i) => `${i+1}. ${b.description}`).join('; ')}

Key Events: ${keyEvents.map((e, i) => `${i+1}. ${e.description}`).join('; ')}

Last Chapter Chunk (most recent ${LAST_CHAPTER_CHUNK_CHARS} chars):
${chapterExcerpt}

World-Building: ${worldElements.map(w => `[${w.category}] ${w.description}`).join('; ')}

---
${aiBeatPrompt}

Beat/Scene to Expand: ${aiBeatInput}
`
      
      // Route through MCP so the LLM gets full tool access while preserving model choice
      const result = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: story.id,
          chapter_id: currentChapter.id,
          prompt: contextPrompt,
          context_type: 'beat',
          model: aiBeatModel
        }
      })
      const content = result?.result?.data?.content || result?.result?.content || result?.content || 'No beat expansion output returned by the model.'
      setAiBeatResult(content)

      // Log the tool calls returned by the MCP server
      const toolCalls = result?.tool_calls || result?.result?.tool_calls || [{
        tool: 'generate_prose',
        args: { model: aiBeatModel, context_type: 'beat' },
        time: new Date().toLocaleTimeString()
      }]
      setMCPToolCalls(prev => [...prev, ...toolCalls])
    } catch (err) {
      console.error('Failed to generate beat expansion:', err)
      setAiBeatResult('Beat expansion failed. Check API key/model or try again with a shorter input.')
    } finally {
      setGeneratingBeat(false)
    }
  }

  const handleQueryContext = async () => {
    if (!story) return
    setQuerying(true)
    try {
      const contextPrompt = `
STORY: ${story.title}
CHAPTER: ${chapterTitle}
SUMMARY: ${chapterSummary}

CHARACTERS: ${characters.map(c => `${c.name}: ${c.traits || ''} - ${c.backstory || ''}`).join('\n')}

BEATS: ${beats.map((b, i) => `${i+1}. ${b.description}`).join('\n')}

WORLD: ${worldElements.map(w => `[${w.category}] ${w.description}`).join('\n')}

KEY EVENTS: ${keyEvents.map((e, i) => `${i+1}. ${e.description}`).join('\n')}

CHAPTER TEXT (excerpt): ${chapterText.slice(0, 3000)}

---
QUESTION: ${queryPrompt}
`

      const result = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: story.id,
          prompt: contextPrompt,
          context_type: 'query',
          model: queryModel
        }
      })

      const content = result?.result?.data?.content || result?.result?.content || result?.content || 'No context returned.'
      setQueryResult(content)

      // Log the tool call for the debug panel
      setMCPToolCalls(prev => [...prev, {
        tool: 'query_context',
        args: { query: queryPrompt, model: queryModel },
        time: new Date().toLocaleTimeString()
      }])
    } catch (err) {
      console.error('Failed to query context:', err)
      setQueryResult('Query failed. Check console.')
    } finally {
      setQuerying(false)
    }
  }

  if (!story || !currentChapter) {
    return <div className="story-editor-page story-editor-loading">Loading...</div>
  }

  const debugContext = `
CHARACTER CONTEXT:
${characters.map(c => `${c.name}: ${c.traits || 'No traits'} - ${c.backstory || 'No backstory'}`).join('\n')}

BEATS (${beats.length}):
${beats.map((b, i) => `${i+1}. ${b.description}`).join('\n')}

WORLD ELEMENTS (${worldElements.length}):
${worldElements.map(w => `[${w.category}] ${w.description}`).join('\n')}

KEY EVENTS (${keyEvents.length}):
${keyEvents.map((e, i) => `${i+1}. ${e.description}`).join('\n')}

CHAPTER SUMMARY:
${chapterSummary || 'No summary'}

CHAPTER TEXT (first 500 chars):
${chapterText.slice(0, 500)}...
  `

  const sortedChapters = [...(story.chapters || [])].sort((a: any, b: any) => (a.order || 0) - (b.order || 0))

  return (
    <div className="story-editor-page">
      <div className="story-editor-container">
        <header className="editor-topbar">
          <button
            type="button"
            className="se-back-btn"
            onClick={() => navigate('/stories')}
          >
            ← Stories
          </button>

          <div className="editor-title-wrap">
            <h2 className="editor-title">Edit Story: {story.title}</h2>
            <p className="editor-subtitle">{story.description || 'No description provided.'}</p>
          </div>

          {saveMessage && <span className="se-save-message">{saveMessage}</span>}
        </header>

        <div className="chapter-switcher">
          {sortedChapters.map((chapter: any) => (
            <button
              key={chapter.id}
              type="button"
              className={`chapter-tab ${chapter.id === currentChapter.id ? 'active' : ''}`}
              onClick={() => switchToChapter(chapter)}
            >
              {chapter.title}
            </button>
          ))}
          <button
            type="button"
            className="chapter-tab chapter-tab-new"
            onClick={handleAddChapter}
          >
            + New Chapter
          </button>
        </div>

        <div className="main-editor-layout">
          <div className="editor-left-pane">
            <section className="editor-card">
              <div className="editor-card-header">
                <input
                  type="text"
                  value={chapterTitle}
                  onChange={(e) => setChapterTitle(e.target.value)}
                  className="chapter-title-input"
                  placeholder="Chapter title"
                />
                <button
                  type="button"
                  className="se-btn se-btn-primary"
                  onClick={handleSaveChapter}
                >
                  Save Chapter
                </button>
              </div>

              <textarea
                className="chapter-text-area"
                value={chapterText}
                onChange={(e) => setChapterText(e.target.value)}
                placeholder="Write your chapter here..."
              />
            </section>

            <section className="editor-card">
              <div className="editor-card-header">
                <h3 className="editor-card-title">Chapter Summary</h3>
                <div className="editor-card-actions">
                  <button
                    type="button"
                    className="se-btn se-btn-secondary"
                    onClick={handleSummarizeChapter}
                  >
                    Auto-Summarize
                  </button>
                  <button
                    type="button"
                    className="se-btn se-btn-primary"
                    onClick={handleSaveSummary}
                  >
                    Save Summary
                  </button>
                </div>
              </div>

              <textarea
                value={chapterSummary}
                onChange={(e) => setChapterSummary(e.target.value)}
                className="story-textarea story-summary-area"
                placeholder="Chapter summary"
              />
            </section>

            <CollapsibleSection title="AI Prose Generator" icon="✨">
              <div className="story-form-grid">
                <label className="story-label" htmlFor="ai-prose-prompt">System Prompt</label>
                <p className="story-help">Instructions for writing style, POV, tone, and constraints.</p>
                <textarea
                  id="ai-prose-prompt"
                  value={aiProsePrompt}
                  onChange={(e) => setAiProsePrompt(e.target.value)}
                  className="story-textarea"
                  rows={3}
                />

                <label className="story-label" htmlFor="ai-scene-input">Scene Input</label>
                <p className="story-help">What should happen now: action, context, and any must-include details.</p>
                <textarea
                  id="ai-scene-input"
                  value={aiProseInput}
                  onChange={(e) => setAiProseInput(e.target.value)}
                  className="story-textarea"
                  rows={3}
                  placeholder="Describe the scene you want generated"
                />

                <div className="story-collapsible-control">
                  <button
                    type="button"
                    onClick={() => setCharactersExpandedForProse(!charactersExpandedForProse)}
                    className="story-collapse-btn"
                  >
                    <span className="story-collapse-arrow">{charactersExpandedForProse ? '▼' : '▶'}</span>
                    <span className="story-label">Select Characters</span>
                    {selectedCharactersForProse.length > 0 && (
                      <span className="story-selection-count">({selectedCharactersForProse.length} selected)</span>
                    )}
                  </button>
                </div>
                {charactersExpandedForProse && (
                  <>
                    <p className="story-help">Optional. Selected characters are injected into context for continuity.</p>
                    {characters.length === 0 ? (
                      <div className="story-empty-inline">No characters available yet. Add characters in the Characters panel to enable selection.</div>
                    ) : (
                      <div className="story-chip-grid">
                        {characters.map(c => (
                          <label key={c.id} className="story-chip">
                            <input
                              type="checkbox"
                              className="se-checkbox"
                              checked={selectedCharactersForProse.includes(c.id)}
                              onChange={(e) => {
                                if (e.target.checked) {
                                  setSelectedCharactersForProse(prev => [...prev, c.id])
                                } else {
                                  setSelectedCharactersForProse(prev => prev.filter(charId => charId !== c.id))
                                }
                              }}
                            />
                            <span>{c.name}</span>
                          </label>
                        ))}
                      </div>
                    )}
                  </>
                )}

                <label className="story-label" htmlFor="ai-prose-model">Model</label>
                <p className="story-help">Any model from the backend list, including MiMo V2 Pro.</p>
                <select
                  id="ai-prose-model"
                  value={aiProseModel}
                  onChange={(e) => setAiProseModel(e.target.value)}
                  className="story-select"
                >
                  {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>

                <button
                  type="button"
                  className="se-btn se-btn-primary se-btn-block"
                  onClick={handleGenerateProse}
                  disabled={generatingProse}
                >
                  {generatingProse ? 'Generating...' : 'Generate Prose'}
                </button>

                <label className="story-label" htmlFor="ai-prose-output">Generated Prose Output</label>
                <p className="story-help">Model output appears here. You can edit before inserting into chapter text.</p>
                <textarea
                  id="ai-prose-output"
                  value={aiProseResult}
                  onChange={(e) => setAiProseResult(e.target.value)}
                  className="story-textarea story-output-area"
                  rows={8}
                  placeholder="No prose output yet. Generate prose to populate this box."
                />
                <div className="story-inline-actions">
                  <button
                    type="button"
                    className="se-btn se-btn-secondary"
                    onClick={() => appendOutputToChapter(aiProseResult, 'Prose')}
                  >
                    Insert Into Chapter
                  </button>
                  <button
                    type="button"
                    className="se-btn se-btn-secondary"
                    onClick={() => void copyOutput(aiProseResult, 'Prose output')}
                  >
                    Copy Output
                  </button>
                </div>
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="AI Beat / Scene Expansion" icon="📝">
              <div className="story-form-grid">
                <label className="story-label" htmlFor="ai-beat-prompt">System Prompt</label>
                <p className="story-help">Instructions for how to expand beats: pacing, detail depth, dialogue focus.</p>
                <textarea
                  id="ai-beat-prompt"
                  value={aiBeatPrompt}
                  onChange={(e) => setAiBeatPrompt(e.target.value)}
                  className="story-textarea"
                  rows={3}
                />

                <label className="story-label" htmlFor="ai-beat-input">Beat / Scene Input</label>
                <p className="story-help">A short beat outline or scene sketch that you want expanded.</p>
                <textarea
                  id="ai-beat-input"
                  value={aiBeatInput}
                  onChange={(e) => setAiBeatInput(e.target.value)}
                  className="story-textarea"
                  rows={3}
                  placeholder="Enter beat or scene outline"
                />

                <div className="story-collapsible-control">
                  <button
                    type="button"
                    onClick={() => setCharactersExpandedForBeat(!charactersExpandedForBeat)}
                    className="story-collapse-btn"
                  >
                    <span className="story-collapse-arrow">{charactersExpandedForBeat ? '▼' : '▶'}</span>
                    <span className="story-label">Select Characters</span>
                    {selectedCharactersForBeat.length > 0 && (
                      <span className="story-selection-count">({selectedCharactersForBeat.length} selected)</span>
                    )}
                  </button>
                </div>
                {charactersExpandedForBeat && (
                  <>
                    <p className="story-help">Optional. Selected character notes are included in the expansion context.</p>
                    {characters.length === 0 ? (
                      <div className="story-empty-inline">No characters available yet. Add characters in the Characters panel to enable selection.</div>
                    ) : (
                      <div className="story-chip-grid">
                        {characters.map(c => (
                          <label key={c.id} className="story-chip">
                            <input
                              type="checkbox"
                              className="se-checkbox"
                              checked={selectedCharactersForBeat.includes(c.id)}
                              onChange={(e) => {
                                if (e.target.checked) {
                                  setSelectedCharactersForBeat(prev => [...prev, c.id])
                                } else {
                                  setSelectedCharactersForBeat(prev => prev.filter(charId => charId !== c.id))
                                }
                              }}
                            />
                            <span>{c.name}</span>
                          </label>
                        ))}
                      </div>
                    )}
                  </>
                )}

                <label className="story-label" htmlFor="ai-beat-model">Model</label>
                <p className="story-help">Choose the model used for expansion. MiMo V2 Pro is available.</p>
                <select
                  id="ai-beat-model"
                  value={aiBeatModel}
                  onChange={(e) => setAiBeatModel(e.target.value)}
                  className="story-select"
                >
                  {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>

                <button
                  type="button"
                  className="se-btn se-btn-primary se-btn-block"
                  onClick={handleGenerateBeatExpansion}
                  disabled={generatingBeat}
                >
                  {generatingBeat ? 'Generating...' : 'Expand Beat'}
                </button>

                <label className="story-label" htmlFor="ai-beat-output">Beat Expansion Output</label>
                <p className="story-help">Expanded beat output appears here and can be edited before use.</p>
                <textarea
                  id="ai-beat-output"
                  value={aiBeatResult}
                  onChange={(e) => setAiBeatResult(e.target.value)}
                  className="story-textarea story-output-area"
                  rows={8}
                  placeholder="No beat expansion output yet. Run expansion to populate this box."
                />
                <div className="story-inline-actions">
                  <button
                    type="button"
                    className="se-btn se-btn-secondary"
                    onClick={() => appendOutputToChapter(aiBeatResult, 'Beat expansion')}
                  >
                    Insert Into Chapter
                  </button>
                  <button
                    type="button"
                    className="se-btn se-btn-secondary"
                    onClick={() => void copyOutput(aiBeatResult, 'Beat output')}
                  >
                    Copy Output
                  </button>
                </div>
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="Query Context Mode" icon="❓">
              <div className="story-form-grid">
                <label className="story-label" htmlFor="query-context">Question</label>
                <textarea
                  id="query-context"
                  value={queryPrompt}
                  onChange={(e) => setQueryPrompt(e.target.value)}
                  className="story-textarea"
                  rows={3}
                  placeholder="Ask a question about this story context"
                />

                <label className="story-label" htmlFor="query-model">Model</label>
                <select
                  id="query-model"
                  value={queryModel}
                  onChange={(e) => setQueryModel(e.target.value)}
                  className="story-select"
                >
                  {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>

                <button
                  type="button"
                  className="se-btn se-btn-primary se-btn-block"
                  onClick={handleQueryContext}
                  disabled={querying}
                >
                  {querying ? 'Querying...' : 'Ask Question'}
                </button>

                {queryResult && (
                  <div className="story-result">
                    <pre>{queryResult}</pre>
                  </div>
                )}
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="AI Context Inspector" icon="🔍">
              <pre className="debug-context-block">
                {debugContext}
              </pre>
            </CollapsibleSection>

            <CollapsibleSection title="MCP Tool Calls" icon="🛠️" badge={mcpToolCalls.length}>
              <div className="debug-context-block" style={{ maxHeight: '300px', overflowY: 'auto' }}>
                {mcpToolCalls.length === 0 ? (
                  <p style={{ color: 'var(--color-text-secondary)', fontStyle: 'italic' }}>
                    No tool calls yet. Generate something to see which MCP tools the LLM used.
                  </p>
                ) : (
                  mcpToolCalls.map((call, i) => (
                    <div key={i} style={{ marginBottom: '1rem', padding: '0.75rem', background: 'var(--color-surface)', borderRadius: '6px' }}>
                      <div style={{ fontWeight: 'bold', marginBottom: '0.25rem' }}>
                        {call.tool} <span style={{ fontSize: '0.75rem', color: '#666' }}>({(call.time || '')})</span>
                      </div>
                      <pre style={{ fontSize: '0.8rem', margin: 0, whiteSpace: 'pre-wrap' }}>
                        {JSON.stringify(call.args, null, 2)}
                      </pre>
                      {call.result && (
                        <div style={{ marginTop: '0.5rem', fontSize: '0.8rem', color: '#0a0' }}>
                          ✓ Result received
                        </div>
                      )}
                    </div>
                  ))
                )}
              </div>
              <button
                type="button"
                onClick={() => setMCPToolCalls([])}
                className="se-btn se-btn-secondary"
                style={{ marginTop: '0.5rem', fontSize: '0.8rem' }}
              >
                Clear Log
              </button>
            </CollapsibleSection>
          </div>

          <div className="editor-right-pane">
            <CollapsibleSection title="Characters" icon="👤" badge={characters.length}>
              <CharacterGenerator
                storyId={story.id}
                models={models}
                onGenerated={() => {
                  setSaveMessage('Character generated!')
                  setTimeout(() => setSaveMessage(''), 3000)
                }}
              />

              <div className="generator-divider"><span>manual entry</span></div>

              <div className="story-item-card">
                <input
                  type="text"
                  value={newCharacterName}
                  onChange={(e) => setNewCharacterName(e.target.value)}
                  className="story-input"
                  placeholder="New character name"
                />
                <textarea
                  value={newCharacterTraits}
                  onChange={(e) => setNewCharacterTraits(e.target.value)}
                  className="story-textarea"
                  placeholder="Traits"
                  rows={2}
                />
                <textarea
                  value={newCharacterBackstory}
                  onChange={(e) => setNewCharacterBackstory(e.target.value)}
                  className="story-textarea"
                  placeholder="Backstory"
                  rows={2}
                />
                <div className="story-item-actions">
                  <button
                    type="button"
                    onClick={handleAddCharacter}
                    className="se-btn se-btn-primary"
                  >
                    Add Character
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setNewCharacterName('')
                      setNewCharacterTraits('')
                      setNewCharacterBackstory('')
                    }}
                    className="se-btn se-btn-secondary"
                  >
                    Clear
                  </button>
                </div>
              </div>

              <div className="story-item-list">
                {characters.map(char => (
                  <div key={char.id} className="story-item-card">
                    <input
                      id={`char-name-${char.id}`}
                      type="text"
                      defaultValue={char.name}
                      className="story-input"
                      placeholder="Name"
                    />
                    <textarea
                      id={`char-traits-${char.id}`}
                      defaultValue={char.traits || ''}
                      className="story-textarea"
                      placeholder="Traits"
                      rows={2}
                    />
                    <textarea
                      id={`char-backstory-${char.id}`}
                      defaultValue={char.backstory || ''}
                      className="story-textarea"
                      placeholder="Backstory"
                      rows={2}
                    />
                    <div className="story-item-actions">
                      <button
                        type="button"
                        onClick={() => handleUpdateCharacter(char.id)}
                        className="se-btn se-btn-secondary"
                      >
                        Update
                      </button>
                      <button
                        type="button"
                        onClick={() => handleDeleteCharacter(char.id, char.name)}
                        className="se-btn se-btn-danger"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="Beats" icon="🎬" badge={beats.length}>
              <div className="story-item-card">
                <input
                  type="text"
                  value={newBeatDesc}
                  onChange={(e) => setNewBeatDesc(e.target.value)}
                  className="story-input"
                  placeholder="New beat description"
                  onKeyDown={(e) => { if (e.key === 'Enter') handleAddBeat() }}
                />
                <div className="story-item-actions">
                  <button
                    type="button"
                    onClick={handleAddBeat}
                    className="se-btn se-btn-primary"
                  >
                    Add Beat
                  </button>
                  <button
                    type="button"
                    onClick={() => setNewBeatDesc('')}
                    className="se-btn se-btn-secondary"
                  >
                    Clear
                  </button>
                </div>
              </div>

              <div className="story-item-list">
                {[...beats].sort((a, b) => a.order - b.order).map(beat => (
                  <div key={beat.id} className="story-item-card">
                    <div className="story-split-inputs">
                      <input
                        id={`beat-order-${beat.id}`}
                        type="number"
                        defaultValue={beat.order}
                        className="story-input story-input-small"
                      />
                      <input
                        id={`beat-desc-${beat.id}`}
                        type="text"
                        defaultValue={beat.description}
                        className="story-input"
                        placeholder="Beat description"
                      />
                    </div>
                    <div className="story-item-actions">
                      <button
                        type="button"
                        onClick={() => handleUpdateBeat(beat.id)}
                        className="se-btn se-btn-secondary"
                      >
                        Update
                      </button>
                      <button
                        type="button"
                        onClick={() => handleDeleteBeat(beat.id)}
                        className="se-btn se-btn-danger"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="World Building" icon="🌍" badge={worldElements.length}>
              <WorldbuildingGenerator
                storyId={story.id}
                chapterId={currentChapter.id}
                models={models}
                onGenerated={() => {
                  setSaveMessage('Setting generated!')
                  setTimeout(() => setSaveMessage(''), 3000)
                }}
              />

              <div className="generator-divider"><span>manual entry</span></div>

              <div className="story-item-card">
                <select
                  value={newWorldCategory}
                  onChange={(e) => setNewWorldCategory(e.target.value)}
                  className="story-select"
                >
                  <option value="">Select category...</option>
                  <option value="Settings">Settings</option>
                  <option value="Cultures">Cultures</option>
                  <option value="Magic and Tech">Magic and Tech</option>
                  <option value="History">History</option>
                  <option value="Races">Races</option>
                  <option value="Geography">Geography</option>
                  <option value="Politics">Politics</option>
                  <option value="Economy">Economy</option>
                  <option value="Religion">Religion</option>
                </select>
                <textarea
                  value={newWorldDesc}
                  onChange={(e) => setNewWorldDesc(e.target.value)}
                  className="story-textarea"
                  placeholder="Description"
                  rows={2}
                />
                <div className="story-item-actions">
                  <button
                    type="button"
                    onClick={handleAddWorldElement}
                    className="se-btn se-btn-primary"
                  >
                    Add Element
                  </button>
                  <button
                    type="button"
                    onClick={() => { setNewWorldCategory(''); setNewWorldDesc('') }}
                    className="se-btn se-btn-secondary"
                  >
                    Clear
                  </button>
                </div>
              </div>

              <div className="story-item-list">
                {worldElements.map(elem => (
                  <div key={elem.id} className="story-item-card">
                    <input
                      id={`world-cat-${elem.id}`}
                      type="text"
                      defaultValue={elem.category}
                      className="story-input"
                      placeholder="Category"
                    />
                    <textarea
                      id={`world-desc-${elem.id}`}
                      defaultValue={elem.description}
                      className="story-textarea"
                      rows={2}
                      placeholder="Description"
                    />
                    <div className="story-item-actions">
                      <button
                        type="button"
                        onClick={() => handleUpdateWorldElement(elem.id)}
                        className="se-btn se-btn-secondary"
                      >
                        Update
                      </button>
                      <button
                        type="button"
                        onClick={() => handleDeleteWorldElement(elem.id)}
                        className="se-btn se-btn-danger"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </CollapsibleSection>

            <CollapsibleSection title="Key Events" icon="⭐" badge={keyEvents.length}>
              <div className="story-item-card">
                <input
                  type="text"
                  value={newEventDesc}
                  onChange={(e) => setNewEventDesc(e.target.value)}
                  className="story-input"
                  placeholder="New key event description"
                  onKeyDown={(e) => { if (e.key === 'Enter') handleAddKeyEvent() }}
                />
                <div className="story-item-actions">
                  <button
                    type="button"
                    onClick={handleAddKeyEvent}
                    className="se-btn se-btn-primary"
                  >
                    Add Event
                  </button>
                  <button
                    type="button"
                    onClick={() => setNewEventDesc('')}
                    className="se-btn se-btn-secondary"
                  >
                    Clear
                  </button>
                </div>
              </div>

              <div className="story-item-list">
                {[...keyEvents].sort((a, b) => a.order - b.order).map(event => (
                  <div key={event.id} className="story-item-card">
                    <div className="story-split-inputs">
                      <input
                        id={`event-order-${event.id}`}
                        type="number"
                        defaultValue={event.order}
                        className="story-input story-input-small"
                      />
                      <input
                        id={`event-desc-${event.id}`}
                        type="text"
                        defaultValue={event.description}
                        className="story-input"
                        placeholder="Event description"
                      />
                    </div>
                    <div className="story-item-actions">
                      <button
                        type="button"
                        onClick={() => handleUpdateKeyEvent(event.id)}
                        className="se-btn se-btn-secondary"
                      >
                        Update
                      </button>
                      <button
                        type="button"
                        onClick={() => handleDeleteKeyEvent(event.id)}
                        className="se-btn se-btn-danger"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </CollapsibleSection>

            <CollapsibleSection
              title={mcpConfig.enabled ? "MCP 連線中" : "MCP 已停用"}
              icon="🔌"
              badge={mcpConfig.enabled ? 1 : undefined}
            >
              <p className="story-help" style={{ marginBottom: '1rem' }}>
                透過 Model Context Protocol 將此故事的資料與工具提供給外部 AI 用戶端使用。
                連線後，AI 可以查詢角色、情節、產生內容，而無需手動複製粘貼。
              </p>

              <div className="story-form-grid">
                <label className="story-label" htmlFor="mcp-enabled">啟用 MCP</label>
                <p className="story-help">啟用後，外部 AI 可以透過此端點存取故事資料。</p>
                <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                  <input
                    id="mcp-enabled"
                    type="checkbox"
                    checked={mcpConfig.enabled}
                    onChange={(e) => handleMCPConfigChange({ enabled: e.target.checked })}
                  />
                  <span style={{ fontSize: '0.85rem' }}>
                    {mcpConfig.enabled ? '已啟用' : '已停用'}
                  </span>
                </div>

                <label className="story-label" htmlFor="mcp-provider">AI 提供者</label>
                <p className="story-help">決定生成時使用的模型提供者。</p>
                <select
                  id="mcp-provider"
                  className="story-select"
                  value={mcpConfig.provider}
                  onChange={(e) => handleMCPConfigChange({ provider: e.target.value })}
                >
                  <option value="openrouter">OpenRouter (Claude, Gemini, DeepSeek...)</option>
                  <option value="gemini">Google Gemini</option>
                  <option value="openai">OpenAI</option>
                </select>

                <label className="story-label" htmlFor="mcp-model">模型</label>
                <p className="story-help">可用模型取決於所選提供者。</p>
                <input
                  id="mcp-model"
                  type="text"
                  className="story-input"
                  value={mcpConfig.model}
                  onChange={(e) => handleMCPConfigChange({ model: e.target.value })}
                  placeholder="default"
                />

                <label className="story-label" htmlFor="mcp-system-prompt">系統提示詞</label>
                <p className="story-help">
                  附加給 MCP session 的額外系統提示詞。例如：&quot;你是一個協助編劇的 AI 助手&quot;。
                </p>
                <textarea
                  id="mcp-system-prompt"
                  className="story-textarea"
                  value={mcpConfig.system_prompt}
                  onChange={(e) => handleMCPConfigChange({ system_prompt: e.target.value })}
                  rows={3}
                  placeholder="額外的系統提示詞（可選）"
                />
              </div>

              <div style={{ marginTop: '1rem', padding: '0.75rem', background: 'var(--color-surface)', borderRadius: '6px' }}>
                <label className="story-label" style={{ marginBottom: '0.25rem' }}>MCP 端點</label>
                <code style={{ fontSize: '0.8rem', wordBreak: 'break-all', color: 'var(--color-text-secondary)' }}>
                  POST /api/mcp?story_id={storyId}
                </code>
                <p className="story-help" style={{ marginTop: '0.5rem' }}>
                  外部 AI 用戶端可使用此端點呼叫 MCP 工具。需附上 JWT 認證。
                </p>
              </div>

              <button
                type="button"
                onClick={saveMCPConfig}
                className="se-btn se-btn-primary"
                style={{ marginTop: '0.75rem', width: '100%' }}
              >
                {mcpSaveMsg || '儲存 MCP 設定'}
              </button>
            </CollapsibleSection>
          </div>
        </div>
      </div>
    </div>
  )
}
