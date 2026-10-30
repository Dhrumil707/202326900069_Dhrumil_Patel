from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float = Field(..., ge=0, le=100)


students = []

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/students')
def create_student(student: Student, response: Response):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail='Student ID already exists')

    students.append(student)
    response.status_code = 201
    return {'isSuccess': True, 'message': 'Student Created Successfully', 'student': student}


@app.get('/students')
def get_students(course: Optional[str] = None):
    if course is None:
        return students

    result = []
    for s in students:
        if s.course == course:
            result.append(s)
    return result


@app.get('/student/students/{id}')
@app.get('/students/{id}')
def get_student(id: int):
    for s in students:
        if s.id == id:
            return s

    raise HTTPException(status_code=404, detail='Student Not Found')

@app.put('/students/{id}')
def update_student(id: int, student: Student):
    for i in range(len(students)):
        if students[i].id == id:
         
            if student.id != id:
                raise HTTPException(status_code=400, detail='Student ID must match URL ID')

            students[i] = student
            return {'isSuccess': True, 'message': 'Student Updated Successfully', 'student': student}

    raise HTTPException(status_code=404, detail='Student Not Found')


@app.delete('/students/{id}')
def delete_student(id: int):
    for s in students:
        if s.id == id:
            students.remove(s)
            return {'isSuccess': True, 'message': 'Student Deleted Successfully'}

    raise HTTPException(status_code=404, detail='Student Not Found')
