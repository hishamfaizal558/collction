# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from collect import Base
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request



from database import engine
from collect import Member  
from pydantic import BaseModel # Replace with your actual model
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

# This line creates all tables from your models
Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




class memberCreate(BaseModel):
    name: str
    phone: str
    payment_status: int

@app.get("/members")
def get_members(db: Session = Depends(get_db)):
    return db.query(Member).all()


@app.post("/members")
def create_member(member: memberCreate, db: Session = Depends(get_db)):
    phone = str(member.phone)
    db_member = db.query(Member).filter(Member.name == member.name, Member.phone == member.phone).first()
    if db_member:
        db_member.payment_status += member.payment_status
    else :
     db_member = Member(**member.dict())
     db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member  # Return the created members
