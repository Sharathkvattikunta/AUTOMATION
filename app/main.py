cat > app/main.py << 'EOF'
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                         env=os.getenv('ENVIRONMENT', 'development'),
                         version=os.getenv('VERSION', '1.0.0'))

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF
