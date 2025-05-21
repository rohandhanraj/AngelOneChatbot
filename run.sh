set -e

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "📦 Installing Node.js dependencies..."
npm install

echo "🌐 Installing Playwright browsers..."
npx playwright install --with-deps