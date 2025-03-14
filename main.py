from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_table, delete_table
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("dropped DB")
    await create_table()
    print("created clear DB")
    yield
    print("Stopped")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)






