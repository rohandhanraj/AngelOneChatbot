set -e

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "📦 Installing Node.js dependencies..."
npm install

#echo "📦 Installing Playwright Linux system dependencies (user-space)..."
#npx playwright install-deps

echo "🌐 Installing Playwright browsers..."
npx playwright install