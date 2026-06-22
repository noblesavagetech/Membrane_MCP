import { useState } from 'react'
import { api } from '../../services/api'

const GENERATION_OPTIONS = [
  {
    id: 'thorough_setting',
    label: 'Deep Lore Master-File',
    description: 'Exhaustive, encyclopedic breakdown mapping history, economy, and society',
    parameters: ['setting_name', 'era_or_theme', 'physical_scale', 'demographics', 'key_pillars']
  },
  {
    id: 'full_setting',
    label: 'Full Setting Breakdown',
    description: 'Complete analysis of a location',
    parameters: ['location_type', 'scale', 'population', 'key_elements']
  },
  {
    id: 'physical_dimensions',
    label: 'Physical Dimensions',
    description: 'Size, layout, structural details',
    parameters: ['location_type', 'square_footage', 'floors']
  },
  {
    id: 'material_composition',
    label: 'Material Composition',
    description: 'Building materials, textures, surfaces',
    parameters: ['era', 'technology_level', 'climate']
  },
  {
    id: 'economic_function',
    label: 'Economic Function',
    description: 'Purpose, commerce, services',
    parameters: ['location_type', 'trade_goods', 'services']
  },
  {
    id: 'sensory_data',
    label: 'Sensory Data',
    description: 'Light, sound, smell, temperature',
    parameters: ['time_of_day', 'activity_level', 'weather']
  },
  {
    id: 'culture_society',
    label: 'Culture & Society',
    description: 'Customs, social structure, traditions',
    parameters: ['region', 'tech_level', 'historical_period']
  }
]

const PARAM_PLACEHOLDERS: Record<string, string> = {
  setting_name: 'e.g. The Iron Spire, Vespera',
  era_or_theme: 'e.g. Cyberpunk, High Fantasy, Post-apocalyptic',
  physical_scale: 'e.g. A bustling continent, a single tavern',
  demographics: 'e.g. 5M citizens, Elves & Dwarves',
  key_pillars: 'e.g. Magic tech, oppressive regime, neon-lights',
  location_type: 'e.g. Tavern, Market, Temple',
  scale: 'e.g. Small (20 sqm), Large (500 sqm)',
  population: 'e.g. 5-20 people',
  key_elements: 'e.g. central fountain, hidden basement',
  square_footage: 'e.g. 200 sqm',
  floors: 'e.g. 3',
  era: 'e.g. Medieval, Modern, Futuristic',
  technology_level: 'e.g. Pre-industrial, Steam-powered',
  climate: 'e.g. Tropical, Arid, Temperate',
  trade_goods: 'e.g. Spices, Weapons, Information',
  services: 'e.g. Lodging, Healing, Entertainment',
  time_of_day: 'e.g. Dawn, Midday, Midnight',
  activity_level: 'e.g. Bustling, Quiet, Abandoned',
  weather: 'e.g. Rainy, Clear, Sandstorm',
  region: 'e.g. Mountainous, Coastal, Urban',
  tech_level: 'e.g. Bronze Age, Industrial, Sci-fi',
  historical_period: 'e.g. Post-war, Golden Age, Decline'
}

interface WorldbuildingGeneratorProps {
  storyId: number
  chapterId: number
  models: { id: string; name: string }[]
  onGenerated: (content: string) => void
}

export default function WorldbuildingGenerator({ storyId, chapterId, models, onGenerated }: WorldbuildingGeneratorProps) {
  const [selectedType, setSelectedType] = useState('')
  const [parameters, setParameters] = useState<Record<string, string>>({})
  const [useContext, setUseContext] = useState(true)
  const [model, setModel] = useState(models[0]?.id || 'anthropic/claude-sonnet-4.5')
  const [generating, setGenerating] = useState(false)
  const [result, setResult] = useState('')
  const [showResult, setShowResult] = useState(false)

  const selectedOption = GENERATION_OPTIONS.find(o => o.id === selectedType)

  const handleAutoGenerate = async () => {
    setGenerating(true)
    try {
      // Route through MCP so the LLM gets full tool access while preserving model choice
      const res = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: storyId,
          chapter_id: chapterId,
          generation_type: 'full_setting',
          parameters: {},
          use_context: true,
          model
        }
      })
      const content = res?.result?.data?.content || res?.result?.content || res?.content || 'Generation completed.'
      setResult(content)
      setShowResult(true)
      onGenerated(content)
    } catch (err) {
      console.error('Auto-generate failed:', err)
      setResult('Generation failed. Check API key/model.')
      setShowResult(true)
    } finally {
      setGenerating(false)
    }
  }

  const handleThoroughGenerate = async () => {
    setGenerating(true)
    try {
      // Route through MCP so the LLM gets full tool access while preserving model choice
      const res = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: storyId,
          chapter_id: chapterId,
          generation_type: 'thorough_setting',
          parameters: {},
          use_context: true,
          model
        }
      })
      const content = res?.result?.data?.content || res?.result?.content || res?.content || 'Generation completed.'
      setResult(content)
      setShowResult(true)
      onGenerated(content)
    } catch (err) {
      console.error('Thorough generate failed:', err)
      setResult('Generation failed. Check API key/model.')
      setShowResult(true)
    } finally {
      setGenerating(false)
    }
  }

  const handleParameterizedGenerate = async () => {
    if (!selectedType) return
    setGenerating(true)
    try {
      // Route through MCP so the LLM gets full tool access while preserving model choice
      const res = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: storyId,
          chapter_id: chapterId,
          generation_type: selectedType,
          parameters,
          use_context: useContext,
          model
        }
      })
      const content = res?.result?.data?.content || res?.result?.content || res?.content || 'Generation completed.'
      setResult(content)
      setShowResult(true)
      onGenerated(content)
    } catch (err) {
      console.error('Parameterized generate failed:', err)
      setResult('Generation failed. Check API key/model.')
      setShowResult(true)
    } finally {
      setGenerating(false)
    }
  }

  const updateParam = (key: string, value: string) => {
    setParameters(prev => ({ ...prev, [key]: value }))
  }

  return (
    <div className="generator-panel">
      <div className="generator-header gap-3 flex flex-col">
        <button
          type="button"
          className="se-btn se-btn-accent se-btn-block"
          onClick={handleAutoGenerate}
          disabled={generating}
        >
          {generating ? 'Generating...' : '🌍 Auto-Generate Setting'}
        </button>
        <button
          type="button"
          className="se-btn se-btn-primary se-btn-block"
          style={{ backgroundColor: '#4f46e5', color: '#fff' }}
          onClick={handleThoroughGenerate}
          disabled={generating}
        >
          {generating ? 'Generating...' : '🔍 Thorough Setting Generation'}
        </button>
      </div>

      <div className="generator-divider">
        <span>or customize</span>
      </div>

      <div className="generator-form">
        <select
          value={selectedType}
          onChange={(e) => {
            setSelectedType(e.target.value)
            setParameters({})
          }}
          className="story-select"
        >
          <option value="">Select generation type...</option>
          {GENERATION_OPTIONS.map(opt => (
            <option key={opt.id} value={opt.id}>
              {opt.label} — {opt.description}
            </option>
          ))}
        </select>

        {selectedOption && (
          <div className="generator-params">
            {selectedOption.parameters.map(param => (
              <div key={param} className="generator-param-row">
                <label className="story-label">{param.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}</label>
                <input
                  type="text"
                  value={parameters[param] || ''}
                  onChange={(e) => updateParam(param, e.target.value)}
                  className="story-input"
                  placeholder={PARAM_PLACEHOLDERS[param] || ''}
                />
              </div>
            ))}
          </div>
        )}

        <div className="generator-options-row">
          <label className="story-chip">
            <input
              type="checkbox"
              className="se-checkbox"
              checked={useContext}
              onChange={(e) => setUseContext(e.target.checked)}
            />
            <span>Use story context</span>
          </label>

          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            className="story-select generator-model-select"
          >
            {models.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
          </select>
        </div>

        {selectedType && (
          <button
            type="button"
            className="se-btn se-btn-primary se-btn-block"
            onClick={handleParameterizedGenerate}
            disabled={generating}
          >
            {generating ? 'Generating...' : `Generate ${selectedOption?.label}`}
          </button>
        )}
      </div>

      {showResult && result && (
        <div className="generator-result">
          <div className="generator-result-header">
            <span className="story-label">Generated Output</span>
            <button
              type="button"
              className="se-btn se-btn-secondary se-btn-sm"
              onClick={() => setShowResult(false)}
            >
              Hide
            </button>
          </div>
          <pre className="generator-result-text">{result}</pre>
          <div className="story-inline-actions">
            <button
              type="button"
              className="se-btn se-btn-secondary"
              onClick={() => navigator.clipboard.writeText(result)}
            >
              Copy Output
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
