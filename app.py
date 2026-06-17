from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import os

app = FastAPI()

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# We will use static index.html or Jinja templates
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)

templates = Jinja2Templates(directory=templates_dir)

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "knn_model_fixed.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/predict")
async def predict(
    profile_pic: int = Form(...),
    nums_length_username: float = Form(...),
    fullname_words: int = Form(...),
    nums_length_fullname: float = Form(...),
    name_username: int = Form(...),
    description_length: int = Form(...),
    external_url: int = Form(...),
    private: int = Form(...),
    posts: int = Form(...),
    followers: int = Form(...),
    follows: int = Form(...)
):
    # Construct feature array instead of pandas DataFrame to save Vercel memory
    features = [[
        profile_pic,
        nums_length_username,
        fullname_words,
        nums_length_fullname,
        name_username,
        description_length,
        external_url,
        private,
        posts,
        followers,
        follows
    ]]
    
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    # probabilities[0] is the chance of Original (0)
    # probabilities[1] is the chance of Fake (1)
    
    if prediction == 1:
        result_text = "Fake Account"
        confidence = round(probabilities[1] * 100, 2)
    else:
        result_text = "Original Account"
        confidence = round(probabilities[0] * 100, 2)
    
    return {
        "prediction": result_text,
        "confidence": confidence
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
