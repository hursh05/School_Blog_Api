from fastapi import APIRouter, HTTPException
from models import Blog
from crud import create_blog, get_blogs, get_blog_by_id, update_blog, delete_blog

blog_router = APIRouter()

@blog_router.post("/blogs/")
async def create_new_blog(blog: Blog):
    blog_id = await create_blog(blog.dict())
    return {"id": blog_id, "message": "Blog created successfully"}

@blog_router.get("/blogs/")
async def fetch_blogs():
    return await get_blogs()

@blog_router.get("/blogs/{blog_id}")
async def fetch_blog(blog_id: str):
    blog = await get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@blog_router.put("/blogs/{blog_id}")
async def update_existing_blog(blog_id: str, blog: Blog):
    updated = await update_blog(blog_id, blog.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog updated successfully"}

@blog_router.delete("/blogs/{blog_id}")
async def delete_existing_blog(blog_id: str):
    deleted = await delete_blog(blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}
