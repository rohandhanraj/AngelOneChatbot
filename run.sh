echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🌐 Installing Playwright and required browsers..."
playwright install --with-deps

echo "🚀 Launching Streamlit app..."
streamlit run app.py --server.port=10000