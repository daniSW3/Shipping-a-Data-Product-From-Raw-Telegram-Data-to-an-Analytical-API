from pydantic import BaseModel
from typing import List, Optional

class ProductMention(BaseModel):
    detected_object_class: str
    count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_text: str
    detection: Optional[str] = None

class ReportResponse(BaseModel):
    top_products: List[ProductMention]

class ChannelActivityResponse(BaseModel):
    channel_name: str
    activity: List[ChannelActivity]

class SearchResponse(BaseModel):
    messages: List[MessageSearchResult]
