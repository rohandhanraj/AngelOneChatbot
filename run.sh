set -e

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🌐 Installing Playwright dependencies using npx..."
npx playwright install --with-deps
