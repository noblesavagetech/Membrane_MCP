import { useState } from 'react'
import { api } from '../../services/api'

const BODY_TYPES = [
  'Hourglass', 'Pear-Shaped', 'Apple-Shaped', 'Rectangle', 'Inverted Triangle',
  'Triangle', 'Spoon-Shaped', 'Diamond-Shaped', 'V-Shaped', 'Oval-Shaped',
  'Trapezoid', 'Heart-Shaped', 'Bell-Shaped', 'Column', 'Ectomorph',
  'Mesomorph', 'Endomorph', 'Athletic', 'Stocky', 'Lanky',
  'Curvy', 'Petite', 'Big-Boned', 'Plump', 'Lean'
]

const GENERATION_OPTIONS = [
  {
    id: 'full_profile',
    label: 'Full Character Profile',
    description: 'Generate all sections at once',
    parameters: ['age_range', 'ethnicity', 'gender', 'occupation', 'body_type']
  },
  {
    id: 'physical_only',
    label: 'Physical Description Only',
    description: 'Detailed physical attributes',
    parameters: ['age', 'height', 'weight', 'body_type', 'gender']
  },
  {
    id: 'personality_background',
    label: 'Personality & Background',
    description: 'Psychology, history, motivations',
    parameters: ['age', 'occupation', 'key_traits']
  },
  {
    id: 'speaking_style',
    label: 'Speaking Style & Voice',
    description: 'Dialogue patterns and verbal identity',
    parameters: ['age', 'accent', 'education_level', 'personality_type']
  },
  {
    id: 'residency_environment',
    label: 'Residency & Environment',
    description: 'Living situation and daily life',
    parameters: ['age', 'occupation', 'income_level', 'region']
  }
]

const PARAM_PLACEHOLDERS: Record<string, string> = {
  age_range: 'e.g. 25-35',
  age: 'e.g. 32',
  ethnicity: 'e.g. Japanese-American',
  gender: 'e.g. Female',
  occupation: 'e.g. Marine biologist',
  body_type: 'Select or leave blank for random',
  height: "e.g. 5'8\"",
  weight: 'e.g. 155 lbs',
  key_traits: 'e.g. stubborn, empathetic, witty',
  accent: 'e.g. Southern US',
  education_level: 'e.g. PhD, High school',
  personality_type: 'e.g. Introverted, analytical',
  income_level: 'e.g. Middle class',
  region: 'e.g. Pacific Northwest'
}

interface CharacterGeneratorProps {
  storyId: number
  models: { id: string; name: string }[]
  onGenerated: (content: string) => void
}

export default function CharacterGenerator({ storyId, models, onGenerated }: CharacterGeneratorProps) {
  const [selectedType, setSelectedType] = useState('')
  const [parameters, setParameters] = useState<Record<string, string>>({})
  const [useContext, setUseContext] = useState(true)
  const [model, setModel] = useState(models[0]?.id || 'anthropic/claude-sonnet-4.5')
  const [generating, setGenerating] = useState(false)
  const [result, setResult] = useState('')
  const [showResult, setShowResult] = useState(false)
  const [autoGuidance, setAutoGuidance] = useState('')
  const [autoName, setAutoName] = useState('')
  const [autoHeight, setAutoHeight] = useState('')
  const [autoWeight, setAutoWeight] = useState('')

  const selectedOption = GENERATION_OPTIONS.find(o => o.id === selectedType)

  const handleAutoGenerate = async () => {
    setGenerating(true)
    try {
      const autoParams: Record<string, string> = {}
      if (autoName.trim()) {
        autoParams.name = autoName.trim()
      }
      if (autoHeight.trim()) {
        autoParams.height = autoHeight.trim()
      }
      if (autoWeight.trim()) {
        autoParams.weight = autoWeight.trim()
      }
      if (autoGuidance.trim()) {
        autoParams.guidance = autoGuidance.trim()
      }
      console.log('[CharacterGenerator] Sending params:', JSON.stringify(autoParams))
      // Route through MCP so the LLM gets full tool access (get_story, update_character, etc.)
      const res = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: storyId,
          generation_type: 'full_profile',
          parameters: autoParams,
          use_context: useContext,
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

  const handleParameterizedGenerate = async () => {
    if (!selectedType) return
    setGenerating(true)
    try {
      const mergedParams = { ...parameters }
      if (autoName.trim()) mergedParams.name = autoName.trim()
      if (autoHeight.trim()) mergedParams.height = autoHeight.trim()
      if (autoWeight.trim()) mergedParams.weight = autoWeight.trim()
      if (autoGuidance.trim()) mergedParams.guidance = autoGuidance.trim()

      // Route through MCP so the LLM gets full tool access while preserving model choice
      const res = await api.post('/api/mcp', {
        method: 'generate',
        params: {
          story_id: storyId,
          generation_type: selectedType,
          parameters: mergedParams,
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
      <div className="generator-header-stack">
        <input
          type="text"
          value={autoName}
          onChange={(e) => setAutoName(e.target.value)}
          className="story-input"
          placeholder="Character name (leave blank for AI to decide)"
        />
        <div style={{ display: 'flex', gap: '8px' }}>
          <input
            type="text"
            value={autoHeight}
            onChange={(e) => setAutoHeight(e.target.value)}
            className="story-input"
            placeholder="Height (e.g. 5'10&quot;)"
            style={{ flex: 1 }}
          />
          <input
            type="text"
            value={autoWeight}
            onChange={(e) => setAutoWeight(e.target.value)}
            className="story-input"
            placeholder="Weight (e.g. 180 lbs)"
            style={{ flex: 1 }}
          />
        </div>
        <textarea
          value={autoGuidance}
          onChange={(e) => setAutoGuidance(e.target.value)}
          className="story-textarea"
          rows={2}
          placeholder="Quick guidance: e.g. 'A cynical ex-cop in her 40s who runs a pawn shop'"
        />
        <button
          type="button"
          className="se-btn se-btn-accent se-btn-block"
          onClick={handleAutoGenerate}
          disabled={generating}
        >
          {generating ? 'Generating...' : '🎲 Auto-Generate Character'}
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
                {param === 'body_type' ? (
                  <select
                    value={parameters[param] || ''}
                    onChange={(e) => updateParam(param, e.target.value)}
                    className="story-select"
                  >
                    <option value="">Random (auto-selected)</option>
                    {BODY_TYPES.map(bt => (
                      <option key={bt} value={bt}>{bt}</option>
                    ))}
                  </select>
                ) : (
                  <input
                    type="text"
                    value={parameters[param] || ''}
                    onChange={(e) => updateParam(param, e.target.value)}
                    className="story-input"
                    placeholder={PARAM_PLACEHOLDERS[param] || ''}
                  />
                )}
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
