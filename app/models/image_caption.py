from dataclasses import dataclass
from datetime import datetime


@dataclass
class ImageCaption:
    image_url: str
    caption: str
    created_at: datetime = datetime.utcnow()
