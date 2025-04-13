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
                f"明日の天気を教えて"
            ),
        },
    ]

response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
)
data = """
ChatCompletion(id='3db8e292-26de-44e3-987a-6b62a4557394', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='明日（2025年4月14日）の天気について、日本各地の概要を以下に示します：\n\n### 日本の天気\n- **北海道・東北地方**: 雲が多く、一部地域で雨が予想されています。気温はやや低めです[1][2][3]。\n- **関東甲信地方**: 午前中を中心に雨が降る地域がありますが、午後には回復し晴れるところもあります[2][3]。\n- **東海地方**: 引き続き雨が降る予想です。太平洋沿岸では降り方が強まる可能性があります[1][2][3]。\n- **近畿地方**: 朝から雨が続く見込みですが、徐々に回復してきます[3][8]。\n- **中国・四国地方**: 晴れ間が広がり、天気は安定してきます[1][3]。\n- **九州地方**: 午前中は曇りがちですが、午後には晴れるところが多くなります[1][3]。\n- **沖縄地方**: 曇り時々晴れの予報で、概ね穏やかな天気になりそうです[1][2][3]。\n\n### 各都市の予想気温（最低 / 最高）\n- **札幌**: 8℃ / 17℃[2]\n- **仙台**: 7℃ / 9℃[2]\n- **東京**: 12℃ / 14℃[2]\n- **名古屋**: 14℃ / 16℃[2]\n- **大阪**: 14℃ / 18℃[2]\n- **広島**: 12℃ / 19℃[1][2]\n- **福岡**: 10℃ / 16℃[1][2]\n- **那覇**: 15℃ / 18℃[2]\n\n全般的に気温は春らしく、関東では雨が予想されるため、傘を持参すると安心です。', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None), delta={'role': 'assistant', 'content': ''})], created=1744530971, model='sonar-pro', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=458, prompt_tokens=30, total_tokens=488, completion_tokens_details=None, prompt_tokens_details=None, citation_tokens=5746, num_search_queries=1), citations=['https://www.jma.go.jp/bosai/forecast/', 'https://tenki.jp', 'https://weather.yahoo.co.jp/weather/', 'https://www.accuweather.com/ja/us/new-york/10021/weather-forecast/349727', 'https://weather.yahoo.co.jp/weather/world/US/72503/', 'https://weathernews.jp/onebox/40.71427/-74.00597/?q=%24New+York+City&v=%249b4ebde4151d75310691168d0e92020a550d66358fd5f5a&lang=ja', 'https://tenki.jp/world/7/92/72503/', 'https://weathernews.jp/s/forecast/'])
"""

import re

match = re.search(r"content='([^']+)'", data)
if match:
    answer = match.group(1)

answer # テキスト表示

