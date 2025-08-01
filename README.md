
# AI Product Transparency Engine

This project provides an AI-powered product transparency checker, featuring:
- FastAPI backend using google/flan-t5-base
- Streamlit frontend for question generation and PDF download
- Setup instructions, features, API documentation, sample report, and reflection included

See `ai-service/` and `frontend/` folders for main code and requirements.

To run locally:
1. Install dependencies in each folder (`pip install -r requirements.txt`)
2. Run FastAPI backend: `uvicorn app:app --reload` from `ai-service`
3. Run Streamlit frontend: `streamlit run app.py` from `frontend`
4. Use the Streamlit UI and download a PDF report

Sample PDF report included in `/design`.

For details, see the full README provided earlier.
