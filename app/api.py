from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from pages.router import api_router

origins = ["*"]
api_router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(api_router, port=8001, host='0.0.0.0')