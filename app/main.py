from fastapi import FastAPI

from app.db.database import initial_db


initial_db()

app = FastAPI(title="Project Name")


