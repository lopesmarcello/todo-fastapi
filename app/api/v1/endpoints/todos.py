from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.core.database import SessionLocal
from app.models.todo import Todo as TodoModel
from app.models.user import User
from app.schemas.todo import Todo, TodoCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@router.post("/", response_model=Todo)
async def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = TodoModel(
        **todo_in.model_dump(),
        owner_id=current_user.id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=list[Todo])
async def read_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(TodoModel).filter(TodoModel.owner_id == current_user.id).all()

@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id and TodoModel.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_in: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id and TodoModel.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.title = todo_in.title
    todo.description = todo_in.description

    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}",)
async def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id and TodoModel.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return todo