#  AI Health Analyzer

AI-powered health prediction app using Machine Learning + Groq API.

---

##  Features

- Disease prediction from symptoms  
- AI explanation & advice  
- Doctor recommendation  
- Clean Streamlit UI  

---

##  Project Structure

health_ai_project/
│
├── app/
│   └── app.py
│
├── data/
│
├── model/
│
├── requirements.txt
├── Dockerfile
└── README.md

---

##  Setup

pip install -r requirements.txt

---

##  API Key

export GROQ_API_KEY="your_api_key"

(For Windows)

set GROQ_API_KEY=your_api_key

---

##  Run

streamlit run app/app.py

---

##  Docker

docker build -t health-ai .

docker run -p 8501:8501 -e GROQ_API_KEY=your_key health-ai

---

##  Deploy

AWS | Azure | Google Cloud Run  

---

##  Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Groq API  

---

##  Author

Adarsh Singh






