import streamlit as st
import requests
from fpdf import FPDF

st.title("Product Transparency Checker")

def generate_pdf(description, questions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Product Transparency Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, f"Product Description: {description}")
    pdf.ln(5)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Follow-up Questions:", ln=True)
    pdf.set_font("Arial", size=10)
    for q in questions:
        pdf.multi_cell(0, 10, f"- {q}")
    pdf_file = "product_report.pdf"
    pdf.output(pdf_file)
    return pdf_file

desc = st.text_area("Enter Product Description")
questions = []
if st.button("Generate"):
    try:
        res = requests.post("http://localhost:8000/generate-questions", json={"description": desc})
        if res.status_code == 200:
            questions = res.json().get("questions", [])
            st.write("Follow-up Questions:")
            for q in questions:
                st.markdown(f"- {q}")
        else:
            st.error(f"Backend error: {res.status_code}")
            st.write(res.text)
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

# Only show PDF download button if questions were generated
if questions:
    pdf_file = generate_pdf(desc, questions)
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name="product_report.pdf",
            mime="application/pdf"
        )
