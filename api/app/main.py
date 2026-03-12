from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, projects, dpr

Base.metadata.create_all(bind=engine) 

app = FastAPI(title="Construction API", version="1.0.0")

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(dpr.router)

@app.get("/")
def root():
    return {"message": "Construction API is running"}