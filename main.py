from fastapi import FastAPI
from routes.blog_routes import blog_router

app = FastAPI(title="School Blog API")

app.include_router(blog_router)
