set -e

#echo "📦 Installing System dependencies..."
#apt-get install libgtk-4.so.1 \
#libgraphene-1.0.so.0 \
#libgstgl-1.0.so.0 \
#libgstcodecparsers-1.0.so.0 \
#libavif.so.15 \
#libenchant-2.so.2 \
#libsecret-1.so.0 \
#libmanette-0.2.so.0 \
#libGLESv2.so.2

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "📦 Installing Node.js dependencies..."
npm install

#echo "📦 Installing Playwright Linux system dependencies (user-space)..."
#npx playwright install-deps

echo "🌐 Installing Playwright browsers..."
npx playwright install