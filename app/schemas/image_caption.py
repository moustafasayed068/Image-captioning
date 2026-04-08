from pydantic import BaseModel, HttpUrl


class ImageCaptionRequest(BaseModel):
    image_url: HttpUrl


class ImageCaptionResponse(BaseModel):
    image_url: HttpUrl
    caption: str
