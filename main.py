import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



text = st.text_input('あなたの趣味を教えてください。') # テキスト入力
'あなたの趣味は', text, 'です。' # テキスト表示

