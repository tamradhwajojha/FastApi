from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
   return {"message": "welcome to the FastAPI application!at venv"}

@app.get("/about")
def about():
   return {"message": "this is about page"}  

@app.get("/users")

def users():
   return {"users": ["rahul","akash","ram","shayam"]}