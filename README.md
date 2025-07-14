# Waste Classifier App

Upload an image of waste to classify it as **Biodegradable** or **Non-Biodegradable**, and receive custom recycling tips.

## 🚀 Deploy Instructions (Backend)

1. Upload your `waste_classifier.keras` model file to this repo.
2. Go to [https://render.com](https://render.com) and connect this repo.
3. It will detect `render.yaml` and deploy the FastAPI backend.
4. Once deployed, use the `/predict/` endpoint to classify images.

## 🌐 Frontend (Optional)

Deploy `frontend/index.html` on GitHub Pages or Netlify.
Edit the `fetch()` URL to your Render backend.