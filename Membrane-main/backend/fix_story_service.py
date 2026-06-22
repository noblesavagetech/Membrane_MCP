from main import get_session
from models import Story
from sqlalchemy.orm import joinedload
from services.story_service import StoryService

def get_story_fixed(self, story_id: int, user_id: int):
    return self.db.query(Story).options(joinedload(Story.chapters), joinedload(Story.characters)).filter(Story.id == story_id, Story.user_id == user_id).first()

StoryService.get_story = get_story_fixed
