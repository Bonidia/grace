from datetime import datetime

from beanie import Document

class Resume(Document):
    
    timestamp_added: datetime = datetime.now()
    filename: str
    content: str
    user_id: int
    tag_id: int
    
    class Settings:
        name = 'resumes'