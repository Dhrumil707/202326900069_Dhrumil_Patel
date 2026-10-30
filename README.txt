STUDENT CRUD - FASTAPI (WITHOUT DATABASE)

A and B are implemented together in main.py.
Style: simple functions, for loops, Python list and response dictionaries.

FILES
main.py          Complete application
requirements.txt Packages needed to run it
README.txt       Run instructions and question-wise explanation

RUN IN POWERSHELL / TERMINAL
1. Extract the ZIP.
2. Open a terminal inside the Student_CRUD folder (where main.py is).
3. Install packages:
   python -m pip install -r requirements.txt
4. Run with auto-reload:
   uvicorn main:app --reload

If uvicorn is not recognised, use:
   python -m uvicorn main:app --reload

SWAGGER UI
http://127.0.0.1:8000/docs
Click an endpoint, then Try it out, enter data and click Execute.
The server command is uvicorn, not unicorn.

A(i) PYDANTIC MODEL
Student has id (int), name (str), course (str), marks (float).
Field(..., ge=0, le=100) makes marks required and allows 0 to 100 inclusive.
Invalid marks return HTTP 422 automatically.
IDs are entered by the user, as required by the model.

A(ii) ENDPOINTS
POST /students                 Add a student (HTTP 201)
GET /students                  List all students
GET /student/students/{id}     Fetch one student (question's exact URL)
GET /students/{id}             Fetch one student (standard alternative URL)
A missing student returns HTTP 404.
A duplicate ID returns HTTP 400.

B(i) ENDPOINTS
PUT /students/{id}             Update a student
DELETE /students/{id}          Delete a student
Both return HTTP 404 if the ID does not exist.
PUT replaces the full student, so send all four fields.
The request body's id must match the URL id; otherwise HTTP 400.

B(ii) OPTIONAL COURSE FILTER
GET /students                  All students
GET /students?course=BCA       Only students whose course is BCA
Filtering is an exact, case-sensitive match.
No matches return an empty list [].

B(iii) AUTO-RELOAD COMMAND AND SWAGGER URL
uvicorn main:app --reload
http://127.0.0.1:8000/docs
main = main.py; app = FastAPI object; --reload = restart after code changes.

EXAMPLE: POST /students
{
  "id": 1,
  "name": "Dhrumil",
  "course": "BCA",
  "marks": 85.5
}

EXAMPLE: PUT /students/1
{
  "id": 1,
  "name": "Dhrumil Patel",
  "course": "BCA",
  "marks": 90.0
}

TEST ORDER IN SWAGGER
1. POST the sample student.
2. GET /students.
3. GET /students with course BCA.
4. GET /student/students/1.
5. PUT /students/1 using the update example.
6. DELETE /students/1.
7. GET /students/1 again: returns HTTP 404.
8. POST with marks 101 or -1: returns HTTP 422.

IN-MEMORY STORAGE
No database is used. All records disappear when the server restarts,
including a restart caused by --reload. Run one server worker for this example.
