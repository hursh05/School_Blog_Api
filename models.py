from pydantic import BaseModel, Field
from typing import Optional

class Blog(BaseModel):
    title: str = Field(..., title="Title of the blog")
    content: str = Field(..., title="Content of the blog")
    author: str = Field(..., title="Author of the blog")
    tags: Optional[list[str]] = Field(default=[], title="Tags for the blog")
