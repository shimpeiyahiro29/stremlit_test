import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from openai import OpenAI


text = st.text_input('質問したいことを聞いてね') # テキスト入力



YOUR_API_KEY = "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"  # ご自身の API キーに置き換えてください
client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {
            "role": "user",
            "content": (
                text
            ),
        },
    ]

response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
)

if
response.choices[0].message.content# テキスト表示

