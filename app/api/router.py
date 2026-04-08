from fastapi import APIRouter, Depends

from app.dependencies import get_caption_service
from app.schemas.image_caption import ImageCaptionRequest, ImageCaptionResponse
from app.services.caption_service import CaptionService

api_router = APIRouter()


@api_router.post("/caption", response_model=ImageCaptionResponse, tags=["captions"])
async def create_caption(
    request: ImageCaptionRequest,
    service: CaptionService = Depends(get_caption_service),
) -> ImageCaptionResponse:
    caption = service.generate_caption(request.image_url)
    return ImageCaptionResponse(image_url=request.image_url, caption=caption)
