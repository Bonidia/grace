from datetime import datetime
from typing import List

from beanie import Document, Indexed, Link
from beanie.odm.fields import PydanticObjectId

from app.models.resume import Resume

class Tag(Document):
    
    name: Indexed(str)
    description: str
    timestamp_added: datetime = datetime.utcnow()
    user_id: PydanticObjectId
    resumes: List[Link[Resume]]

    class Settings:
        name = 'tags'