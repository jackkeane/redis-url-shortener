import redis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize Redis (Assumes Redis is running on localhost)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form.get('url')
        if long_url:
            # 1. Create a unique ID
            url_id = r.incr('url_id')
            short_code = hex(url_id)[2:]
            
            # 2. Store in Redis Hash (key: 'links', field: short_code)
            r.hset('links', short_code, long_url)
            
            # 3. Construct the full short URL
            short_url = f"{request.host_url}{short_code}"
            
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Retrieve original URL from Redis
    long_url = r.hget('links', short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)