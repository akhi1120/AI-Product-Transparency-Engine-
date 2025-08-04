# AI Product Transparency Engine

## Overview

This project provides an AI-powered Product Transparency Checker. Users can enter a product description, receive intelligent follow-up questions, and (optionally) get a transparency score. The solution uses a Hugging Face transformer model via a FastAPI backend and a Streamlit frontend.

## Folder Structure

AI-Product-Transparency-Engine/
│
├── ai-service/       # FastAPI backend
│   ├── app.py
│   └── requirements.txt
│
├── frontend/         # Streamlit frontend
│   ├── app.py
│   └── requirements.txt

## Setup Instructions

### Backend (FastAPI)
1. Open a terminal and navigate to the backend folder:
    cd AI-Product-Transparency-Engine/ai-service

2. (Optional) Activate your virtual environment.

3. Install dependencies:
    pip install -r requirements.txt

4. Run the FastAPI server:
    uvicorn app:app --reload

   The API docs are available at: http://127.0.0.1:8000

### Frontend (Streamlit)
1. Open a new terminal and navigate to the frontend folder:
    cd AI-Product-Transparency-Engine/frontend

2. (Optional) Activate your virtual environment.

3. Install dependencies:
    pip install -r requirements.txt

4. Start the Streamlit app:
    streamlit run app.py

   The app will run at: http://localhost:8501

## Feature List

- AI-powered follow-up question generation based on product description.
- Transparency scoring (optional) for eco-friendly and organic keywords.
- PDF report generation from frontend.
- API documentation available at /docs (Swagger UI).
- Modular microservice architecture with clear separation between frontend and backend.

## AI Service Documentation

Backend Endpoints:

- POST /generate-questions  
  Request JSON: { "description": "string" }  
  Response JSON: { "questions": [list_of_questions] }

- POST /transparency-score  
  Request JSON: { "description": "string" }  
  Response JSON: { "score": int }

- GET /  
  Health check endpoint.

## Sample Product Entry + Example Report

Product Description: This organic face cream has no parabens and is cruelty-free.

Follow-up Questions:
- Which ingredient does this product contain?
- What kind of skin can I expect from this product?
- What is the rating for the ingredients and quality of this face cream?

A sample PDF report is included in /design/product_report.pdf.

## Reflection

> How did you use AI tools in development?
>
> I leveraged Hugging Face's transformers library to use the flan-t5-small language model for dynamic, context-aware follow-up question generation. Streamlit was used for building a user-friendly, interactive frontend, while FastAPI powered the backend microservice for efficient request handling.
>
> What principles guided your architecture, design, and product transparency logic?
>
> I followed modular design principles to separate the AI backend and the frontend, making it easy to maintain and extend. Product transparency logic was implemented through both AI-driven question generation and a keyword-based scoring system, with a focus on usability, accessibility, and clear API documentation. The solution is designed to be adaptable for a variety of product types and scalable for future enhancements.
