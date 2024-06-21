#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Configure Streamlit
mkdir -p ~/.streamlit
echo "[server]" > ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "port = \$PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml

# Start Streamlit
streamlit run main.py
