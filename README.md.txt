# 🥔 Potato Disease Classification

A full-stack deep learning application that classifies potato leaf diseases from uploaded images. The project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset and serves predictions through a FastAPI backend with a React frontend.

## Features

- Classifies potato leaf images into:
  - Healthy
  - Early Blight
  - Late Blight
- Deep learning model built using TensorFlow/Keras
- FastAPI backend for model inference
- React frontend for image upload and prediction
- REST API for real-time disease classification

---

## Project Structure

```
Potato-Disease-Classification/
│
├── app/                 # FastAPI backend
├── frontend/            # React frontend
├── training/            # Model training notebook
├── models/              # Trained Keras models
├── sample_images/       # Sample test images
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Tech Stack

### Backend
- FastAPI
- TensorFlow / Keras
- NumPy
- Pillow
- Uvicorn

### Frontend
- React
- Vite
- JavaScript
- HTML
- CSS

### Machine Learning
- CNN
- PlantVillage Dataset

---

## Dataset

The model was trained using the **PlantVillage** dataset containing images of potato leaves belonging to three classes:

- Healthy
- Early Blight
- Late Blight

Dataset:
https://www.kaggle.com/datasets/arjuntejaswi/plant-village

---

## Installation

### Clone Repository

```bash
git clone https://github.com/LokeshSharma891/Potato-Disease-Classification.git
cd Potato-Disease-Classification
```

---

## Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

---

## Model

The trained model is stored inside the `models` directory.

Current version:

```
model_v2.keras
```

---

## Results

The CNN model accurately classifies potato leaf diseases into the three supported categories and can perform inference on unseen leaf images through the web application.

---

## Future Improvements

- Deploy on Render or Railway
- Docker support
- Confidence score visualization
- Model quantization for faster inference
- Mobile-friendly UI

---

## Author

**Lokesh Sharma**

B.Tech Engineering Physics  
Delhi Technological University (DTU)

GitHub:
https://github.com/LokeshSharma891