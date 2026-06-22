from typing import Optional
from sqlalchemy.orm import Session, joinedload
from models import BeatScene, Chapter, Character, KeyEvent, Story, WorldBuildingElement
from services.openrouter_service import openrouter_service

class StoryService:
    def __init__(self, db: Session):
        self.db = db

    # ============ STORY CRUD ============
    def list_stories(self, user_id: int):
        return self.db.query(Story).filter(Story.user_id == user_id).all()

    def get_story(self, story_id: int, user_id: int) -> Optional[Story]:
        self.db.expire_all()  # Fresh data
        return self.db.query(Story).options(
            joinedload(Story.chapters), 
            joinedload(Story.characters)
        ).filter(Story.id == story_id, Story.user_id == user_id).first()

    def create_story(self, user_id: int, title: str, description: str = "") -> Story:
        story = Story(user_id=user_id, title=title, description=description)
        self.db.add(story)
        self.db.commit()
        self.db.refresh(story)
        # Auto-create first chapter
        chapter = Chapter(story_id=story.id, title=f"{title} - Chapter 1", order=1)
        self.db.add(chapter)
        self.db.commit()
        self.db.refresh(story)
        return story

    def update_story(self, story_id: int, user_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if story:
            for key, value in kwargs.items():
                if hasattr(story, key):
                    setattr(story, key, value)
            self.db.commit()
            self.db.refresh(story)
        return story

    def delete_story(self, story_id: int, user_id: int) -> bool:
        story = self.get_story(story_id, user_id)
        if not story:
            return False
        self.db.delete(story)
        self.db.commit()
        return True

    # ============ CHAPTER CRUD ============
    def create_chapter(self, story_id: int, user_id: int, title: str = "Untitled Chapter"):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        max_order = self.db.query(Chapter).filter(Chapter.story_id == story_id).count()
        chapter = Chapter(story_id=story_id, title=title, order=max_order + 1)
        self.db.add(chapter)
        self.db.commit()
        self.db.refresh(chapter)
        return chapter

    def update_chapter(self, chapter_id: int, story_id: int, user_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        chapter = self.db.query(Chapter).filter(Chapter.id == chapter_id, Chapter.story_id == story_id).first()
        if chapter:
            for key, value in kwargs.items():
                if hasattr(chapter, key):
                    setattr(chapter, key, value)
            self.db.commit()
            self.db.refresh(chapter)
        return chapter

    # ============ CHARACTER CRUD ============
    def list_characters(self, story_id: int, user_id: int):
        story = self.get_story(story_id, user_id)
        return story.characters if story else []

    def create_character(self, story_id: int, user_id: int, name: str, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        character = Character(story_id=story_id, name=name, **kwargs)
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def update_character(self, char_id: int, story_id: int, user_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        char = self.db.query(Character).filter(Character.id == char_id, Character.story_id == story_id).first()
        if char:
            for key, value in kwargs.items():
                if hasattr(char, key):
                    setattr(char, key, value)
            self.db.commit()
            self.db.refresh(char)
        return char

    def delete_character(self, char_id: int, story_id: int, user_id: int) -> bool:
        story = self.get_story(story_id, user_id)
        if not story:
            return False
        char = self.db.query(Character).filter(Character.id == char_id, Character.story_id == story_id).first()
        if char:
            self.db.delete(char)
            self.db.commit()
            return True
        return False

    # ============ BEATS CRUD ============
    def create_beat(self, chapter_id: int, description: str, order: int = 0):
        beat = BeatScene(chapter_id=chapter_id, description=description, order=order)
        self.db.add(beat)
        self.db.commit()
        self.db.refresh(beat)
        return beat

    def get_beats(self, chapter_id: int):
        return self.db.query(BeatScene).filter(BeatScene.chapter_id == chapter_id).order_by(BeatScene.order).all()

    def update_beat(self, beat_id: int, **kwargs):
        beat = self.db.query(BeatScene).filter(BeatScene.id == beat_id).first()
        if beat:
            for key, value in kwargs.items():
                if hasattr(beat, key):
                    setattr(beat, key, value)
            self.db.commit()
            self.db.refresh(beat)
        return beat

    def delete_beat(self, beat_id: int) -> bool:
        beat = self.db.query(BeatScene).filter(BeatScene.id == beat_id).first()
        if beat:
            self.db.delete(beat)
            self.db.commit()
            return True
        return False

    # ============ WORLD BUILDING CRUD ============
    def create_world_element(self, chapter_id: int, category: str, description: str):
        elem = WorldBuildingElement(chapter_id=chapter_id, category=category, description=description)
        self.db.add(elem)
        self.db.commit()
        self.db.refresh(elem)
        return elem

    def get_world_elements(self, chapter_id: int):
        return self.db.query(WorldBuildingElement).filter(WorldBuildingElement.chapter_id == chapter_id).all()

    def update_world_element(self, elem_id: int, **kwargs):
        elem = self.db.query(WorldBuildingElement).filter(WorldBuildingElement.id == elem_id).first()
        if elem:
            for key, value in kwargs.items():
                if hasattr(elem, key):
                    setattr(elem, key, value)
            self.db.commit()
            self.db.refresh(elem)
        return elem

    def delete_world_element(self, elem_id: int) -> bool:
        elem = self.db.query(WorldBuildingElement).filter(WorldBuildingElement.id == elem_id).first()
        if elem:
            self.db.delete(elem)
            self.db.commit()
            return True
        return False

    # ============ KEY EVENTS CRUD ============
    def create_key_event(self, chapter_id: int, description: str, order: int = 0):
        event = KeyEvent(chapter_id=chapter_id, description=description, order=order)
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def get_key_events(self, chapter_id: int):
        return self.db.query(KeyEvent).filter(KeyEvent.chapter_id == chapter_id).order_by(KeyEvent.order).all()

    def update_key_event(self, event_id: int, **kwargs):
        event = self.db.query(KeyEvent).filter(KeyEvent.id == event_id).first()
        if event:
            for key, value in kwargs.items():
                if hasattr(event, key):
                    setattr(event, key, value)
            self.db.commit()
            self.db.refresh(event)
        return event

    def delete_key_event(self, event_id: int) -> bool:
        event = self.db.query(KeyEvent).filter(KeyEvent.id == event_id).first()
        if event:
            self.db.delete(event)
            self.db.commit()
            return True
        return False

    # ============ AI METHODS ============
    def _resolve_model(self, model: Optional[str]) -> str:
        return model if model else "default"

    def _format_story_context(
        self,
        story: Story,
        chapter: Chapter,
        characters: list,
        beats: list,
        key_events: list,
        world_elements: list,
    ) -> str:
        character_text = "\n".join(
            [f"- {c.name}: traits={c.traits or ''}; backstory={c.backstory or ''}" for c in characters]
        ) or "- None"

        beats_text = "\n".join([f"{idx + 1}. {b.description}" for idx, b in enumerate(beats)]) or "- None"
        events_text = "\n".join([f"{idx + 1}. {e.description}" for idx, e in enumerate(key_events)]) or "- None"
        world_text = "\n".join([f"- [{w.category}] {w.description}" for w in world_elements]) or "- None"

        chapter_excerpt = (chapter.text or "")[-2500:]

        return (
            f"Story Title: {story.title}\n"
            f"Story Description: {story.description or ''}\n\n"
            f"Chapter Title: {chapter.title or ''}\n"
            f"Chapter Summary: {chapter.summary or ''}\n\n"
            f"Characters:\n{character_text}\n\n"
            f"Beats:\n{beats_text}\n\n"
            f"Key Events:\n{events_text}\n\n"
            f"World Building:\n{world_text}\n\n"
            f"Chapter Excerpt:\n{chapter_excerpt}"
        )

    async def summarize_chapter(
        self,
        chapter_id: int,
        story_id: int,
        user_id: int,
        model: str = "default",
    ) -> str:
        story = self.get_story(story_id, user_id)
        if not story:
            return ""

        chapter = self.db.query(Chapter).filter(Chapter.id == chapter_id, Chapter.story_id == story_id).first()
        if not chapter:
            return ""

        summary = await self.generate_chapter_summary(chapter.text or "", model=self._resolve_model(model))
        chapter.summary = summary
        self.db.commit()
        self.db.refresh(chapter)
        return summary

    async def generate_prose(
        self,
        chapter: Chapter,
        story: Story,
        characters: list,
        beats: list,
        key_events: list,
        world_elements: list,
        prompt: str,
        model: str = "default",
    ) -> str:
        context = self._format_story_context(story, chapter, characters, beats, key_events, world_elements)
        messages = [
            {
                "role": "system",
                "content": "You are an expert fiction writing assistant. Use the provided context to produce high-quality prose and keep continuity.",
            },
            {
                "role": "user",
                "content": f"{context}\n\nUser Request:\n{prompt}",
            },
        ]
        return await openrouter_service.chat(messages, model=self._resolve_model(model), max_tokens=8192)

    async def generate_from_prompt(self, prompt: str, model: str = "default") -> str:
        """Pass a pre-built prompt directly to the LLM (frontend already assembled full context)."""
        messages = [
            {
                "role": "system",
                "content": "You are an expert fiction writing assistant. Follow the instructions provided exactly.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]
        return await openrouter_service.chat(messages, model=self._resolve_model(model), max_tokens=8192)

    async def query_context(
        self,
        story_id: int,
        user_id: int,
        prompt: str,
        chapter_id: Optional[int] = None,
        model: str = "default",
    ) -> str:
        story = self.get_story(story_id, user_id)
        if not story:
            return "Story not found."

        chapter = None
        if chapter_id is not None:
            chapter = self.db.query(Chapter).filter(Chapter.id == chapter_id, Chapter.story_id == story_id).first()
        elif story.chapters:
            chapter = sorted(story.chapters, key=lambda c: c.order or 0)[0]

        if not chapter:
            return "Chapter not found."

        beats = self.get_beats(chapter.id)
        key_events = self.get_key_events(chapter.id)
        world_elements = self.get_world_elements(chapter.id)
        context = self._format_story_context(story, chapter, story.characters, beats, key_events, world_elements)

        messages = [
            {
                "role": "system",
                "content": "You are a story analysis assistant. Answer questions using only the provided story context.",
            },
            {
                "role": "user",
                "content": f"{context}\n\nQuestion:\n{prompt}",
            },
        ]
        return await openrouter_service.chat(messages, model=self._resolve_model(model))

    async def generate_chapter_summary(self, chapter_text: str, model: str = "google/gemini-3.1-flash-lite-preview") -> str:
        """Summarize chapter text using AI"""
        if not chapter_text:
            return ""
        summary = await openrouter_service.summarize_text(chapter_text, model=model)
        return summary

    async def generate_character_development(self, story: Story, character_name: str, context: str):
        """Generate character development suggestions"""
        prompt = f"Story: {story.title}\n\nDevelop the character: {character_name}\n\nContext: {context}"
        messages = [
            {"role": "system", "content": "You are a character development expert for fiction writers."},
            {"role": "user", "content": prompt}
        ]
        response = ""
        async for chunk in openrouter_service.stream_chat(messages):
            response += chunk
        return response

    async def generate_plot_suggestions(self, story: Story, current_state: str):
        """Generate plot progression suggestions"""
        prompt = f"Story: {story.title}\nDescription: {story.description}\n\nCurrent state: {current_state}\n\nSuggest plot developments:"
        messages = [
            {"role": "system", "content": "You are a plot development expert for fiction writers."},
            {"role": "user", "content": prompt}
        ]
        response = ""
        async for chunk in openrouter_service.stream_chat(messages):
            response += chunk
        return response

    async def generate_scene_beats(self, chapter_summary: str, existing_beats: list):
        """Generate scene beat suggestions"""
        beats_text = "\n".join([f"{i+1}. {b.description}" for i, b in enumerate(existing_beats)])
        prompt = f"Chapter summary: {chapter_summary}\n\nExisting beats:\n{beats_text}\n\nSuggest additional scene beats:"
        messages = [
            {"role": "system", "content": "You are a scene structure expert. Provide beat suggestions as a numbered list."},
            {"role": "user", "content": prompt}
        ]
        response = ""
        async for chunk in openrouter_service.stream_chat(messages):
            response += chunk
        return response

    async def generate_world_building(self, story: Story, category: str, context: str):
        """Generate world-building elements"""
        prompt = f"Story: {story.title}\n\nCategory: {category}\n\nContext: {context}\n\nGenerate world-building details:"
        messages = [
            {"role": "system", "content": "You are a world-building expert for fiction writers."},
            {"role": "user", "content": prompt}
        ]
        response = ""
        async for chunk in openrouter_service.stream_chat(messages):
            response += chunk
        return response

    # ============ CHARACTER GENERATION ============
    BODY_TYPES = [
        "Hourglass", "Pear-Shaped", "Apple-Shaped", "Rectangle", "Inverted Triangle",
        "Triangle", "Spoon-Shaped", "Diamond-Shaped", "V-Shaped", "Oval-Shaped",
        "Trapezoid", "Heart-Shaped", "Bell-Shaped", "Column", "Ectomorph",
        "Mesomorph", "Endomorph", "Athletic", "Stocky", "Lanky",
        "Curvy", "Petite", "Big-Boned", "Plump", "Lean"
    ]

    CHARACTER_PROMPTS = {
                "full_profile": (
                            "Character Profile Generation Prompt\n"
                            "Create a character profile for an aged fictional character of a specified ethnicity. The profile must be structured into the distinct sections\n"
                            "\n"
                            "System Instruction:\n"
                            "\n"
                            "You are a meticulous character biographer. For every field, provide specific, concrete, realistic details. If the user does not specify something, you must invent a logical, precise detail — never leave anything vague or generic. \n"
                            "Section 1: Physical Profile & Personality (Exactly Two Paragraphs, at least 5 sentences each)\n"
                            "\n"
                            "- Paragraph 1 (Physical + Core Traits)State in this exact order: current age, exact height, exact weight, body type, race, skin tone, specific ethnicity, 2–3 notable physical features, current natural hair color + style, eye color. Then clearly state their current occupation. End the paragraph by naming 4–6 dominant personality traits and 2–3 recurring behavioral patterns (use short, direct phrases).\n"
                            "- Paragraph 2 (Interaction & Mannerisms)Describe how they interact with others (warm/distant, blunt/polite, dominating/reserved, etc.) and their most noticeable mannerisms (physical habits, gestures, tics, posture quirks). Then define their specific speaking style using 3–5 concrete characteristics (examples: clipped sentences, frequent curses, long pauses, uses diminutives, heavy sarcasm, vintage slang, very formal grammar, trails off, repeats phrases, etc.).\n"
                            "\n"
                            "Tone Constraint (applies to both paragraphs):\n"
                            "\n"
                            "Use direct, plain, factual language only. No metaphors, no poetic descriptions, no adjectives like \"striking\", \"soulful\", \"commanding presence\", \"ethereal\". Write like a clinical police or casting dossier. That version forces visible, tangible mannerisms into every profile while keeping the output clean and consistent.\n"
                            "\n"
                            "**Section 2: Background, Education & Interests (Two Paragraphs)**\n"
                            "\n"
                            "- **Paragraph 1:** Detail education history. Name a **specific, real-world institution** (e.g., \"Arizona State University\") and the **specific degree** obtained (e.g., \"B.A. in Journalism\"). List current occupation and key relationships.\n"
                            "- **Paragraph 2:** List specific hobbies, interests, and favorite music genre. Name specific icons. Provide the Year, Make, Model, and Color of their vehicle.\n"
                            "\n"
                            "**Section 3: Speaking style (Colon List)**\n"
                            "Describe speaking style. The language should be direct and straightforward, avoiding metaphors or any \"flowery\" language.\n"
                            "Speaking Style: Describe the typical cadence, volume, pitch, and rate of speech. Include any observable speech impediments or unique vocal qualities (e.g., breathiness, raspiness, clarity of articulation). Specify any regional accents (e.g., Southern, New Yorker, New England) or distinct speech patterns, including specific slang or cultural vernacular.\n"
                            "- Vocabulary and Sentence Structure: Characterize the complexity of vocabulary used, the typical length and structure of sentences, and the frequency and type of slang or colloquialisms employed.\n"
                            "- Emotional Responses: Provide four distinct examples of how the character speaks when experiencing different emotions:\n"
                            "    - Happy Response:\n"
                            "    - Angry Response:\n"
                            "    - Sad Response:\n"
                            "    - Neutral/Everyday Response:\n"
                            "\n"
                            "**Section 4: Residency & Environment (One Paragraph)**\n"
                            "\n"
                            "- **Geography:** State a real US State and a real City.\n"
                            "- **Fictional Neighborhood:** Invent a fictional neighborhood name. Write exactly two sentences describing the atmosphere and visual details of this neighborhood.\n"
                            "- **Fictional District:** Invent a fictional district name that contains the neighborhood. Write exactly two sentences describing the socio-economics or reputation of this district.\n"
                            "- **Dwelling:** Explicitly state if the person lives in a house, apartment, condo, or mobile home, followed by a brief description of the building's exterior.\n"
                            "\n"
                            "**CRITICAL INSTRUCTIONS FOR AUTO-GENERATION:**\n"
                            "1. Generate the ENTIRE profile (all sections) in a single response. DO NOT ask the user which section they want. Just output the full profile.\n"
                            "2. If a specific character name is not provided, you MUST invent a fitting and realistic First and Last Name for them based on their implied background/ethnicity.\n"
                            "3. NEVER use pronouns (he/she/they/him/her/theirs, etc.) to refer to the character anywhere in the profile. You must consistently use the character's first name or alias instead of pronouns. This is a strict formatting rule.\n"
                            "\n"
                            "**Section 5: Physical Description (Colon List)**\n"
                            "Physical Description — nothing else.\n"
                            "\n"
                            "Format strictly as a colon list with nested bullets where needed.\n"
                            "Focus exclusively on observable, tangible physical characteristics and exact inch measurements. Use plain, simple language for vivid descriptions. Include shapes with front, side, and rear views where helpful, plus relatable analogies like simple geometric terms (sphere, oval, curve, arc, teardrop, heart-shape) or everyday/fruit comparisons (halved cantaloupe under tension, loose drape, hanging avocado halves, inverted pear) — mix as needed for clear visuals.\n"
                            "\n"
                            "MANDATORY RULES:\n"
                            "• Keep all language simple and straightforward — no uncommon or technical words like frustum, ovoid, ellipsoid, meridian, pole, projection, vector, axis, truncated, radius.\n"
                            "• Avoid vague terms like round, wide, or full — expand with easy descriptions (e.g., \"curved like a gentle S\", \"bulging like a basketball swell\").\n"
                            "• Include circumference, width, or length measurements in inches at key points.\n"
                            "• Describe muscle/fat distribution, bone structure, and textures in basic terms (e.g., even soft padding, thick layer creating curves, minimal visible muscle).\n"
                            "• Detail transitions to adjacent parts with plain words (gentle taper, smooth blend, sharp crease).\n"
                            "• Add visible surface details (dimples, cellulite, veins) only as plain facts.\n"
                            "• For female torso: Detail breasts in and out of bra, including shape/volume, areola color, nipple shape/size.\n"
                            "• For male torso: Detail chest in and out of shirt; if chubby/overweight/fat, describe chest as breast-like with shape/size.\n"
                            "• Make it easy to read and visual, like describing a photo to a friend — no interpretations or stories.\n"
                            "\n"
                            "**Section 5: Physical Description**\n"
                            "\n"
                            "- General Build: Age in years, height in inches, weight in pounds, overall body type (e.g., slim athletic, soft curvy, stocky muscular) with simple analogies.\n"
                            "- Head and Face:\n"
                            "    - Skull shape and size (e.g., oval with gentle curves, width in inches)\n"
                            "    - Skin texture and tone (e.g., smooth even tone, light freckles)\n"
                            "    - Eye shape and color (e.g., almond-shaped, deep blue)\n"
                            "    - Eyebrows and lashes (shape, thickness, e.g., arched and thick)\n"
                            "    - Nose shape and size (e.g., straight bridge with flared base, length in inches)\n"
                            "    - Lips shape and size (e.g., full lower lip, width in inches)\n"
                            "    - Cheeks shape (e.g., rounded with soft padding)\n"
                            "    - Hair texture, color, and style (e.g., wavy and thick, dark brown, shoulder-length)\n"
                            "    - Jawline shape (e.g., square with gentle angles)\n"
                            "- Neck and Shoulders:\n"
                            "    - Neck shape and size (e.g., circumference in inches, straight column-like)\n"
                            "    - Shoulders shape and size (e.g., width in inches, sloped with even padding)\n"
                            "    - Visible muscle and bone structure (e.g., minimal muscle showing, collarbones lightly visible)\n"
                            "- Torso and Core:\n"
                            "    - Overall torso shape and size (e.g., hourglass with gentle curves, length in inches from shoulders to hips)\n"
                            "    - Chest/waist/hip measurements (e.g., 38-30-40 inches)\n"
                            "    - Chest (in shirt/out of shirt for males; in bra/out of bra for females):\n"
                            "        - Shape and look (front/side/rear + simple analogies)\n"
                            "        - Measurements (width/circumference at fullest)\n"
                            "        - Fullness and padding pattern\n"
                            "        - Front/side/rear specifics\n"
                            "        - How it connects to shoulders and midsection\n"
                            "        - Surface details (areola color, nipple shape/size in inches, e.g., round pink areolas 2 inches wide, cylindrical nipples 0.5 inches long)\n"
                            "    - Midsection shape and size (e.g., soft rounded belly, circumference at waist and navel)\n"
                            "    - Back shape (e.g., gentle curve like an S, with even padding)\n"
                            "- Arms:\n"
                            "    - Overall shape and look (front/side/rear + simple analogies)\n"
                            "    - Key measurements (upper arm circumference relaxed, forearm widest, wrist)\n"
                            "    - Biceps:\n"
                            "        - Shape (e.g., gentle rounded swell)\n"
                            "        - Size (circumference in inches)\n"
                            "        - Muscle definition (e.g., minimal, hidden under padding)\n"
                            "        - Fat distribution (e.g., even soft layer, some dimpling)\n"
                            "        - Bone structure (e.g., not prominent)\n"
                            "    - Forearms:\n"
                            "        - Shape (e.g., tapered like a soft cone)\n"
                            "        - Size (circumference in inches at widest)\n"
                            "        - Muscle definition (e.g., minimal, padded)\n"
                            "        - Fat distribution (e.g., thick even softness)\n"
                            "        - Bone structure (e.g., lightly visible)\n"
                            "- Hands:\n"
                            "    - Overall shape and size (e.g., length/width in inches)\n"
                            "    - Fingers (length, thickness, padding, e.g., long slender with soft tips)\n"
                            "    - Palms (width, padding, e.g., wide with thick cushion)\n"
                            "    - Knuckles (prominence, coverage, e.g., lightly raised under even fat)\n"
                            "    - Muscle and bone structure (e.g., veins faintly visible, nails oval-shaped)\n"
                            "    - Considerations for build (e.g., thicker padding in plus-sized hands)\n"
                            "- Hips:\n"
                            "    - Shape and look (front/side/rear + simple analogies, e.g., gentle flare like an inverted pear)\n"
                            "    - Size (circumference in inches at widest)\n"
                            "    - Bone structure (e.g., wide-set bones spaced 12 inches)\n"
                            "    - Muscle/fat distribution (e.g., even heavy padding, love handles with soft folds, cellulite dimples)\n"
                            "    - Front/side/rear specifics\n"
                            "    - How it connects to waist and thighs\n"
                            "- Glutes:\n"
                            "    - Shape and look (front/side/rear + simple analogies, e.g., heart-shaped like twin peaches)\n"
                            "    - Size and volume (circumference in inches at fullest, protrusion in inches)\n"
                            "    - Muscle tone (e.g., soft with minimal firmness)\n"
                            "    - Fat distribution (e.g., heavy lower fullness, soft jiggle)\n"
                            "    - Front/side/rear specifics\n"
                            "    - How it connects to hips, lower back, and thighs\n"
                            "- Thighs:\n"
                            "    - Shape and look (front/side/rear + simple analogies, e.g., thick columns with outer curve)\n"
                            "    - Size (circumference in inches at widest, mid, above knee)\n"
                            "    - Muscle/fat distribution (e.g., thick inner padding, outer sweep, cellulite patterns, rubbing contact)\n"
                            "    - Front/side/rear specifics\n"
                            "    - Inner thigh gap or contact (e.g., no gap, soft touching)\n"
                            "    - How it connects to hips and knees\n"
                            "    - Surface details (contours, dimpling)\n"
                            "- Legs (Lower Legs):\n"
                            "    - Shape and look (front/side/rear + simple analogies, e.g., tapered like slender cones)\n"
                            "    - Size (circumference in inches at calf peak, mid-shin, ankle)\n"
                            "    - Muscle definition (e.g., gentle calf bulge like an inverted teardrop)\n"
                            "    - Bone structure (e.g., straight shin line)\n"
                            "    - Fat distribution (e.g., even light padding)\n"
                            "    - Front/side/rear specifics\n"
                            "    - How it connects to thighs and ankles\n"
                            "- Ankles:\n"
                            "    - Shape and size (circumference in inches)\n"
                            "    - Bone structure and prominence (e.g., bony knobs visible, or soft padded coverage)\n"
                            "- Feet:\n"
                            "    - Shape and size (length/width in inches, US/EU sizing)\n"
                            "    - Arch height (e.g., medium curve)\n"
                            "    - Toes (length, shape, padding, e.g., straight with soft rounded tips)\n"
                            "    - Bone/muscle structure (e.g., thin soles vs. thick padded)\n"
                            "    - Considerations for build (e.g., wider and softer in plus-sized feet)\n"
                            "    \n"
                            "    Physical Description — nothing else.\n"
                            "    \n"
                            "     Section 5.5: Physical attributes and Style.\n"
                            "    \n"
                            "    Format strictly as a colon list with nested bullets where needed.\n"
                            "    Focus exclusively on observable, tangible physical characteristics and exact inch measurements. Use plain, simple language for vivid descriptions. Include shapes with front, side, and rear views where helpful, plus relatable analogies like simple geometric terms (sphere, oval, curve, arc, teardrop, heart-shape) or everyday/fruit comparisons (halved cantaloupe under tension, loose drape, hanging avocado halves, inverted pear) — mix as needed for clear visuals.\n"
                            "    \n"
                            "    MANDATORY RULES:\n"
                            "    • Keep all language simple and straightforward — no uncommon or technical words like frustum, ovoid, ellipsoid, meridian, pole, projection, vector, axis, truncated, radius.\n"
                            "    • Avoid vague terms like round, wide, or full — expand with easy descriptions (e.g., \"curved like a gentle S\", \"bulging like a basketball swell\").\n"
                            "    • Include circumference, width, or length measurements in inches at key points.\n"
                            "    • Describe muscle/fat distribution, bone structure, and textures in basic terms (e.g., even soft padding, thick layer creating curves, minimal visible muscle).\n"
                            "    • Detail transitions to adjacent parts with plain words (gentle taper, smooth blend, sharp crease).\n"
                            "    • Add visible surface details (dimples, cellulite, veins) only as plain facts.\n"
                            "    \n"
                            "    • Make it easy to read and visual, like describing a photo to a friend — no interpretations or stories.\n"
                            "    \n"
                            "- Genitals: If male, penis length and width in inches (relaxed and erect if relevant).\n"
                            "- Specific Features: Any scars (location, size, shape), tattoos (design, placement, size), birthmarks (color, shape, location).\n"
                            "- Clothing and Movement: Describe typical clothing styles for at least four various occasions (e.g., casual, formal, work-specific, sleepwear), detailing fit, fabric textures, and common accessories. Describe typical footwear for various occasions (e.g., casual sneakers, formal shoes, work boots, slippers), including material, heel height, and wear patterns. Describe foot size (US sizing) Describe typical posture (e.g., slumped, erect, leaning) and characteristic movements (e.g., gait, gestures, fidgets, speed of movement, fluidity or stiffness).\n"
                            " Section 6: Sexual Profile & Kinks — nothing else.\n"
                            "\n"
                            "Format strictly as a colon list with nested bullets where needed.\n"
                            "Use plain, direct, explicit language — be specific, realistic, and varied. No vague terms like \"adventurous\" or \"passionate\" without concrete examples.\n"
                            "\n"
                            "MANDATORY STRUCTURE & REQUIREMENTS:\n"
                            "\n"
                            "**Section 6: Sexual Profile & Kinks**\n"
                            "\n"
                            "- Sexual orientation: Explicitly state (heterosexual, homosexual, bisexual, pansexual, asexual, demisexual, etc.). Include any nuances (e.g., \"heteroflexible\", \"mostly heterosexual with occasional same-sex attraction\").\n"
                            "- Primary attraction patterns: Describe the types of people this character is most strongly sexually and romantically drawn to. Be specific about:\n"
                            "    - Gender presentation/expression (e.g., hyper-feminine women, masculine men, androgynous people, etc.)\n"
                            "    - Body types they find hottest (use plain descriptive terms like \"curvy hourglass\", \"lean athletic\", \"soft thick thighs and wide hips\", \"tall muscular\", \"chubby soft belly\", \"petite and toned\")\n"
                            "    - Personality traits that turn them on (e.g., confident and teasing, shy and eager to please, dominant and commanding, nurturing and sweet, bratty and defiant, quiet and intense)\n"
                            "    - Any other turn-ons (age range relative to them, height differences, scent, voice type, etc.)\n"
                            "- Libido level: Low, average, high, or hypersexual. Include a short note on frequency/desire (e.g., \"high — wants sex daily\", \"average — 3–4 times a week is ideal\").\n"
                            "- Primary role in bed: Dominant, submissive, switch, service top, power bottom, brat tamer, etc. Add a short explanation of how they express it.\n"
                            "- Favorite kinks/fetishes: List 4–8 specific, explicit ones. Include at least one uncommon or niche kink. Be graphic and clear (e.g., \"impact play with belts\", \"breeding kink\", \"forced orgasm\", \"pet play with collars and leashes\", \"edging and denial\", \"somnophilia with consent\", \"body worship (especially thighs/ass)\").\n"
                            "- Hard limits: List 2–5 absolute no-gos. Be explicit (e.g., \"no blood play\", \"no age play\", \"no scat\", \"no non-consensual roleplay even in fantasy\").\n"
                            "- Preferred body contact: Describe in detail the ways they most love to touch others and be touched (e.g., \"loves gripping big booty cheeks hard\", \"craves having their neck kissed and bitten\", \"prefers slow full-body grinding\", \"enjoys hair-pulling\", \"likes being pinned down by strong arms\").\n"
                            "- Erogenous zones: List the top 3–5 most sensitive spots on their own body, ranked by intensity if possible, with how they like them stimulated (e.g., \"1. Inner thighs — light teasing licks\", \"2. Nipples — sucking and pinching\", \"3. Neck — biting and sucking marks\").\n"
                            "- Vocal tendencies during sex: Silent, quiet moans, loud, dirty talk, whimpering, growling, begging, etc. Include specific phrases they might say if relevant.\n"
                            "- Aftercare needs: Detail what they require or enjoy giving/receiving after sex (e.g., \"needs lots of cuddling and reassurance\", \"likes being praised and petted\", \"prefers quiet time alone for 10 minutes then closeness\", \"enjoys giving gentle massages\").\n"
                            "- Public/play party attitude: Exhibitionist, voyeur, strictly private, situational, or something in between. Include any specific scenarios they're open to (e.g., \"fine with discreet touching in public\", \"loves being watched but not filmed\", \"strictly bedroom only\").\n"
                            ),
                                                                                                                                            "physical_only": (
                                                                                                                                                        "Generate ONLY a detailed Physical Description — nothing else.\n"
                                                                                                                                                                    "Format strictly as a colon list with nested bullets where needed.\n"
                                                                                                                                                                                "Focus exclusively on observable, tangible physical characteristics.\n"
                                                                                                                                                                                            "Include: height (exact), weight (exact), body type, build, hair (color, texture, length, style), "
                                                                                                                                                                                                        "eyes (color, shape, notable features), skin (tone, texture, marks), face shape, "
                                                                                                                                                                                                                    "distinguishing marks (scars, tattoos, birthmarks), posture, gait, clothing style, "
                                                                                                                                                                                                                                "and overall first impression."
                                                                                                                                                                                                                                        ),
                                                                                                                                                                                                                                                "personality_background": (
                                                                                                                                                                                                                                                            "Generate ONLY Personality & Background sections — nothing else.\n"
                                                                                                                                                                                                                                                                        "Section 1 - Personality & Psychology: core personality traits (5+), fears, motivations, "
                                                                                                                                                                                                                                                                                    "moral compass, emotional patterns, stress responses, habits, pet peeves, humor style.\n"
                                                                                                                                                                                                                                                                                                "Section 2 - Background & History: birthplace, family structure, childhood events, "
                                                                                                                                                                                                                                                                                                            "education, career path, key relationships, defining life moments, losses/traumas, achievements.\n"
                                                                                                                                                                                                                                                                                                                        "Be specific and detailed. Use colon-lists with nested bullets."
                                                                                                                                                                                                                                                                                                                                ),
                                                                                                                                                                                                                                                                                                                                        "speaking_style": (
                                                                                                                                                                                                                                                                                                                                                    "Generate ONLY Speaking Style & Voice — nothing else.\n"
                                                                                                                                                                                                                                                                                                                                                                "Cover: vocabulary level, sentence structure preferences, accent or dialect markers, "
                                                                                                                                                                                                                                                                                                                                                                            "verbal tics or filler words, catchphrases, topics they gravitate toward, "
                                                                                                                                                                                                                                                                                                                                                                                        "communication style (direct/indirect, formal/casual), how they argue, how they comfort, "
                                                                                                                                                                                                                                                                                                                                                                                                    "how they flirt, how they express anger.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                "Include 3-5 example dialogue lines that showcase their unique voice.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                            "Format as colon-lists with nested bullets."
                                                                                                                                                                                                                                                                                                                                                                                                                                    ),
                                                                                                                                                                                                                                                                                                                                                                                                                                            "residency_environment": (
                                                                                                                                                                                                                                                                                                                                                                                                                                                        "Generate ONLY Residency & Environment — nothing else.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "Cover: type of dwelling (apartment, house, etc.), specific location/neighborhood, "
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "interior decoration style, cleanliness level, key possessions, what's on their nightstand, "
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "what's in their fridge, daily routine (morning to night), commute, "
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "favorite local spots, relationship with neighbors.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "Format as colon-lists with nested bullets."
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                }
    WORLDBUILDING_PROMPTS = {
        "thorough_setting": (
            "**Role:** Master World-Architect & Historian.\n\n"
            "**Objective:** Construct the single most definitive, exhaustive, and layered architectural-sociological-historical blueprint of the requested setting. Produce a “Deep Lore Master-File” that reads like the private reference manuscript a prize-winning novelist keeps beside their desk—dense, authoritative, and so complete that any writer can step into the setting and instantly understand its bones, its breath, its contradictions, and its living pulse. Maximize every single token by relentlessly expanding, interconnecting, and illuminating every element until the description feels encyclopedic yet still vividly alive.\n\n"
            "**Core Constraints:**\n\n"
            "1. **The Nominal Rule (Non-Negotiable):** In every single paragraph, without exception, refer to the entire setting by its full proper name exactly as provided in the input. Never once use any pronoun (“it,” “its,” “they,” “them”) or any generic placeholder (“the city,” “the station,” “this place,” “the location”). Every fact, every description, every implication must be explicitly anchored to the setting’s full name. Repeat the name naturally and frequently so the reader remains continuously immersed inside the named setting.\n"
            "2. **Analytical Density Over Narrative Fluff:** This is not storytelling. Never use second-person perspective, never write “as you walk,” “the air feels thick with,” or any scene-like prose. Instead, deliver precise, layered, analytical description that explains why the setting is the way it is. Combine the rigorous eye of an urban planner, a social historian, a materials scientist, and a sensory ethnographer. For every atmospheric detail, trace the socio-economic pressures, historical events, technological or magical constraints, and ecological realities that produced it. Turn every observation into cause-and-effect analysis.\n"
            "3. **Maximum Token Saturation & Robust Expansion Protocol:** Do not summarize anything. When any concept is introduced—markets, architecture, social classes, daily rhythms, power structures, sensory environment—immediately expand it into its full sub-components and interconnections. Example structure for expansion:\n"
            "    - Historical layers that created it\n"
            "    - Physical / architectural mechanics and materials\n"
            "    - Economic and supply-chain realities\n"
            "    - Social stratification and unspoken rules\n"
            "    - Power dynamics and who benefits\n"
            "    - Sensory reality (explained through chemistry, acoustics, light physics, biology)\n"
            "    - Temporal changes (hour-by-hour, season-by-season)\n"
            "    - Contradictions and hidden tensions\n"
            "    - How this element interacts with every other element in the setting\n"
            "    Keep drilling deeper and wider until the model’s token limit is reached while remaining coherent, logical, and useful for fiction writing.\n"
            "4. **Anti-Slop Protocol (Strict):** Eliminate all generic fantasy/cyberpunk filler words and phrases (“tapestry,” “vibrant,” “beacon,” “shrouded,” “testament to,” “echoes of,” “bustling,” “teeming,” “whispers,” “labyrinthine” used poetically, etc.). Use precise, grounded, educated language only. If the setting is dark, specify lumen levels, light-scattering particles, and the exact materials that absorb or reflect light. If it smells, name the volatile compounds, their sources, and how they interact with human (or non-human) physiology. Be literary in structure and rhythm, but never purple, never vague, never clichéd.\n"
            "5. **Holistic Interconnection Mandate:** Every paragraph must explicitly link the current element back to at least two other major aspects of the setting (history to economy, architecture to social behavior, sensory data to power structures, etc.). This creates a dense web of understanding so the reader sees the setting as a single, breathing organism rather than isolated facts.\n\n"
            "**Output Format:**\n\n"
            "One continuous, unbroken block of high-density descriptive prose. No titles, no headers, no bullet points, no introductions, no disclaimers, no concluding remarks. Begin the very first sentence with the setting’s full proper name and never deviate from the constraints above. Write at maximum possible length and depth while staying sharply focused and analytically rich."
        ),
        "full_setting": (
            "You are a meticulous sociologist and environmental analyst. Provide an exhaustive breakdown "
            "of this setting/location. ALWAYS start off by naming the setting clearly. DO NOT use pronouns like 'it', 'its', 'they', or 'them' to refer to the setting; ONLY use the setting's proper name instead.\n\n"
            "Cover ALL of the following sections in maximum detail:\n"
            "1. Physical Dimensions (size, layout, structural details, rooms/areas)\n"
            "2. Material Composition (building materials, textures, surfaces, age/condition)\n"
            "3. Sensory Data (lighting, sounds, smells, temperature, air quality)\n"
            "4. Economic Function (purpose, commerce, services, costs, clientele)\n"
            "5. Culture & Society (customs, social hierarchy, traditions, unwritten rules)\n"
            "6. History & Significance (origin, past events, reputation, future trajectory)\n\n"
            "Format each section with a clear heading and colon-lists with nested bullets. Be extremely specific and provide as much detail as possible, utilizing the maximum token output available to create a rich, breathing world."
        ),
        "physical_dimensions": (
            "Generate ONLY Physical Dimensions for this setting — nothing else.\n"
            "Cover: total area/square footage, number of floors/levels, room-by-room layout, "
            "ceiling heights, doorways and passages, windows and natural light sources, "
            "outdoor spaces, hidden areas, structural condition, architectural style.\n"
            "Format as colon-lists with nested bullets."
        ),
        "material_composition": (
            "Generate ONLY Material Composition — nothing else.\n"
            "Cover: primary building materials (walls, floor, ceiling), surface textures, "
            "furniture materials, decorative elements, technology present, "
            "signs of wear or damage, repairs/modifications, age indicators.\n"
            "Format as colon-lists with nested bullets."
        ),
        "economic_function": (
            "Generate ONLY Economic Function — nothing else.\n"
            "Cover: primary purpose/function, goods or services offered, pricing/costs, "
            "typical clientele, operating hours, staff/employees, revenue sources, "
            "competition, supply chains, economic health.\n"
            "Format as colon-lists with nested bullets."
        ),
        "sensory_data": (
            "Generate ONLY Sensory Data — nothing else.\n"
            "Cover: lighting (natural and artificial, quality, shadows), sounds (ambient, "
            "intermittent, notable), smells (dominant, subtle, seasonal), temperature and humidity, "
            "air quality and movement, tactile textures visitors encounter, "
            "visual focal points, time-of-day variations.\n"
            "Format as colon-lists with nested bullets."
        ),
        "culture_society": (
            "Generate ONLY Culture & Society — nothing else.\n"
            "Cover: social hierarchy/power structure, customs and rituals, unwritten rules, "
            "common greetings/interactions, taboos, celebrations, conflicts, "
            "relationship to outsiders, notable figures, collective values, "
            "how information spreads, justice/dispute resolution.\n"
            "Format as colon-lists with nested bullets."
        ),
    }

    async def generate_character_profile(
        self,
        story: Story,
        generation_type: str,
        parameters: dict,
        use_context: bool,
        model: str = "default",
    ) -> str:
        import random
        system_prompt = self.CHARACTER_PROMPTS.get(generation_type, self.CHARACTER_PROMPTS["full_profile"])

        # Extract name, height, weight, guidance BEFORE the generic loop
        name = parameters.pop("name", None)
        guidance = parameters.pop("guidance", None)
        height = parameters.pop("height", None)
        weight = parameters.pop("weight", None)

        # Build parameter instructions from remaining params
        param_lines = []
        for key, value in parameters.items():
            if value:
                label = key.replace("_", " ").title()
                param_lines.append(f"{label}: {value}")

        # If body_type not specified for full or physical, pick random
        if generation_type in ("full_profile", "physical_only") and not parameters.get("body_type"):
            param_lines.append(f"Body Type: {random.choice(self.BODY_TYPES)}")

        user_content = ""
        
        # Non-negotiable constraints go first
        constraints = []
        if name:
            constraints.append(f"Name: {name}")
        if height:
            constraints.append(f"Height: {height}")
        if weight:
            constraints.append(f"Weight: {weight}")
        
        if constraints:
            user_content += "MANDATORY — use these EXACT values, do NOT change or substitute them:\n"
            user_content += "\n".join(f"- {c}" for c in constraints)
            user_content += "\n\n"
        
        if not name:
            user_content += "CRITICAL: The user did NOT provide a name. You MUST invent a realistic, fitting First and Last Name based on their implied background and use it consistently. NEVER use pronouns.\n\n"
        else:
            user_content += "CRITICAL: NEVER use pronouns (he/she/they/him/her). You must consistently use the character's first name or alias instead. This is a strict formatting rule.\n\n"

        
        if use_context:
            chars_text = "\n".join(
                [f"- {c.name}: role={c.role or ''}, traits={c.traits or ''}" for c in (story.characters or [])]
            ) or "None yet"
            
            world_elements_text = []
            if story.chapters:
                for chapter in story.chapters:
                    for w in getattr(chapter, "worldbuilding", []):
                        world_elements_text.append(f"- [{w.category}] {w.description}")
            world_text = "\n".join(world_elements_text) or "None yet"
            
            user_content += f"Existing Story Context:\nStory: {story.title}\nDescription: {story.description or 'N/A'}\n\nWorldbuilding Elements:\n{world_text}\n\nExisting Characters:\n{chars_text}\n\n"

        if guidance:
            user_content += f"Author's Creative Direction:\n{guidance}\n\n"

        if param_lines:
            user_content += "User-Specified Parameters:\n" + "\n".join(param_lines) + "\n\n"

        user_content += "Generate the character profile now."

        print(f"[DEBUG] Raw parameters received: name={name}, height={height}, weight={weight}, guidance={guidance}")
        print(f"[DEBUG] Constraints: {constraints}")

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        # Use assistant prefill to force the model to start with the correct name/values
        prefill = ""
        if name or height or weight:
            if name:
                prefill = f"# {name}\n\n"
            else:
                prefill = "# " # Give it a header start to generate the name
                
            prefill += "## Section 1: Physical Profile & Personality\n"
            if name:
                prefill += f"Name: {name}\n"
            if height:
                prefill += f"Height: {height}\n"
            if weight:
                prefill += f"Weight: {weight}\n"
            
            # For Gemini and others on OpenRouter, they sometimes ignore trailing assistant
            # messages if they are not specifically expected, but prefilling is the way to go.
            messages.append({"role": "assistant", "content": prefill})

        result = await openrouter_service.chat(messages, model=self._resolve_model(model), max_tokens=8192)
        # Prepend prefill since the API only returns the continuation
        if prefill:
            result = prefill + result
        return result

    async def generate_worldbuilding_element(
        self,
        story: Story,
        chapter: Chapter,
        generation_type: str,
        parameters: dict,
        use_context: bool,
        model: str = "default",
    ) -> str:
        system_prompt = self.WORLDBUILDING_PROMPTS.get(generation_type, self.WORLDBUILDING_PROMPTS.get("full_setting", ""))

        param_lines = []
        for key, value in parameters.items():
            if value:
                label = key.replace("_", " ").title()
                param_lines.append(f"{label}: {value}")

        user_content = ""
        if use_context:
            world_elems = self.get_world_elements(chapter.id)
            world_text = "\n".join([f"- [{w.category}] {w.description}" for w in world_elems]) or "None yet"
            chars_text = "\n".join(
                [f"- {c.name}: {c.traits or ''}" for c in (story.characters or [])]
            ) or "None yet"
            user_content += (
                f"Existing Story Context:\nStory: {story.title}\nDescription: {story.description or 'N/A'}\n"
                f"Chapter: {chapter.title}\nChapter Summary: {chapter.summary or 'N/A'}\n"
                f"Existing World Elements:\n{world_text}\n"
                f"Characters:\n{chars_text}\n\n"
            )

        if param_lines:
            user_content += "User-Specified Parameters:\n" + "\n".join(param_lines) + "\n\n"

        # If no location type specified but context is available, instruct AI to derive setting from context
        if not parameters.get("location_type") and use_context:
            user_content += (
                "No specific location type was provided. Analyze the story context above — the title, "
                "description, existing characters, world elements, and chapter summary — and create a "
                "setting/location that organically fits this story's world, tone, and genre. "
                "The setting should complement existing elements and feel like a natural part of this narrative.\n\n"
            )

        user_content += "Generate the worldbuilding content now."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]
        
        prefill = ""
        setting_name = parameters.get("setting_name")
        if generation_type == "thorough_setting" and setting_name:
            prefill = f"{setting_name} "
            messages.append({"role": "assistant", "content": prefill})

        result = await openrouter_service.chat(messages, model=self._resolve_model(model), max_tokens=8192)
        if prefill:
            result = prefill + result
        return result
