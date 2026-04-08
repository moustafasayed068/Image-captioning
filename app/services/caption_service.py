from app.models.image_caption import ImageCaption


class CaptionService:
    def generate_caption(self, image_url: str) -> str:
        # Replace this placeholder logic with a real captioning model or API.
        return f"Generated caption for image: {image_url}"

    def create_caption(self, image_url: str) -> ImageCaption:
        caption = self.generate_caption(image_url)
        return ImageCaption(image_url=image_url, caption=caption)
