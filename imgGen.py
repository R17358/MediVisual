import streamlit as st
import requests
import io
from PIL import Image
import numpy as np
import time


API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.content
    except requests.exceptions.JSONDecodeError:
        return {"error": "Response could not be decoded as JSON"}

def ImageGenerator(prompt):
    output = query({"inputs": prompt})
    image = Image.open(io.BytesIO(output))
    filename = f'image_{int(time.time())}.jpg'
    image.save(filename)
    return image, filename
