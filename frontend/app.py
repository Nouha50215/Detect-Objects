# Streamlit web interface (prototype UI)

import streamlit as st
import requests
import base64
from PIL import Image
import io

st.title("Object Detection Web App 🚀")

backend_url = "http://127.0.0.1:8000/detect"

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded:
    files = {"file": uploaded.getvalue()}
    response = requests.post(backend_url, files=files)
    data = response.json()

    st.subheader("Detections:")
    st.json(data["detections"])

    # Show annotated image
    img_bytes = base64.b64decode(data["image"])
    img = Image.open(io.BytesIO(img_bytes))
    st.image(img, caption="Detected Objects")
