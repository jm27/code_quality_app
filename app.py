from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    # Get the code from the request
    code = request.json.get('code', '')

    # Dummy analysis TODO replace with real analysis later

    complexity = len(code) / 100 # Just a dummy placeholder complexity metric

    errors = code.count(';') # Simple error check since python doesn't have semicolons

    readability = max(0, 10  - complexity) # Just a dummy placeholder readability metric

    return jsonify({
        'complexity': round(complexity, 2),
        'errors': errors,
        'readability': round(readability, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)

