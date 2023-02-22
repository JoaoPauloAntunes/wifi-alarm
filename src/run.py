import uvicorn
from dotenv import load_dotenv
import os


load_dotenv(".env")


# command: python src/run.py 
# or: cd src && uvicorn main:app --host=localhost --port=8000 log_level=info
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=os.environ["HOST_IP_ADDRESS"], 
        port=8000, 
        log_level="info", 
        reload=os.getenv("APP_RELOAD", 'False').lower() in ('true', '1', 't')
    )
