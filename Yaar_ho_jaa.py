import streamlit as st
import schedule
import time
import requests
import pandas as pd
import numpy as np
import pytz
from datetime import datetime

# Inject custom CSS to expand the layout
st.markdown(
    """
    <style>
    .full-width {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the full-width class for your content
st.markdown('<div class="full-width">Your content here</div>', unsafe_allow_html=True)


st.title('Navigate Your Trades')
