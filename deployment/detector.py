from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import tensorflow as tf
import tensorflow_text as text  # Ensures compatibility for the BERT model
from pydantic import BaseModel
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = FastAPI()

# Load the model once at the start
model = tf.keras.models.load_model("C://Users//sathi//Career//Internship//AFAME//Spam SMS Detection//BERT//saved_model//spam_detection_model")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/", response_class=HTMLResponse)
async def predict(request: Request, message: str = Form(...)):
    prediction = model.predict([message])[0][0]  # Extract prediction value
    
    if prediction >= 0.5:
        spam_status = 'This has a high probability of being a spam message'
    else:
        spam_status = 'This is not likely to be a spam message'
    
    return spam_status
