import uvicorn
from app.chat import socket_app


if __name__ == "__main__":
    uvicorn.run(socket_app, host="127.0.0.1", port=8000)
