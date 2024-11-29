from database import db

async def create_blog(blog_data):
    result = await db.blogs.insert_one(blog_data)
    return str(result.inserted_id)

async def get_blogs():
    blogs = await db.blogs.find().to_list(100)
    return blogs

async def get_blog_by_id(blog_id):
    return await db.blogs.find_one({"_id": blog_id})

async def update_blog(blog_id, update_data):
    result = await db.blogs.update_one({"_id": blog_id}, {"$set": update_data})
    return result.modified_count > 0

async def delete_blog(blog_id):
    result = await db.blogs.delete_one({"_id": blog_id})
    return result.deleted_count > 0
