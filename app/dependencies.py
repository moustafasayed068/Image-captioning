from app.services.caption_service import CaptionService


def get_caption_service() -> CaptionService:
    return CaptionService()
