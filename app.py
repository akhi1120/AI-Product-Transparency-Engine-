from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()  # This ensures /docs is enabled by default

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

class ProductInput(BaseModel):
    description: str

@app.post("/generate-questions")
def generate_questions(product: ProductInput):
    prompt = f"Generate three specific customer questions about this product: {product.description}"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids, 
        max_length=64, 
        num_return_sequences=3,
        do_sample=True, 
        top_k=50, 
        top_p=0.95
    )
    questions = [tokenizer.decode(o, skip_special_tokens=True) for o in outputs]
    return {"questions": questions}



@app.post("/transparency-score")
def transparency_score(product: ProductInput):
    score = 0
    keywords = ['organic', 'eco-friendly', 'sulfate-free', 'non-toxic', 'natural']
    for word in keywords:
        if word in product.description.lower():
            score += 20
    return {"score": min(score, 100)}

# Optional: Root endpoint just for health check/friendly message
@app.get("/")
def root():
    return {"message": "FastAPI backend is running! Go to /docs for API documentation."}
