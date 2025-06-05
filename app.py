from flask import Flask, request, jsonify
from crawl_and_summarize import summarize_url

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    data = request.get_json(force=True)
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        summary = summarize_url(url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'summary': summary})

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
