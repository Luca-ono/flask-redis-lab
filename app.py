from flask import Flask, render_template
import redis
import json
import time 

app = Flask(__name__)

# Connect to Redis - host is the service name in compose.yaml
try:
    r = redis.Redis(host='redis-server', port=6379, decode_responses=True)
    r.ping() # Check if the connection is successful
    print("Connected to Redis successfully!")
except redis.exceptions.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")
    r = None # Set r to None if connection fails

@app.route('/')
def home():
    cache_key = 'home' # Unique key for this route
    data = None
    if r:
        try:
            data_from_cache = r.get(cache_key)
            if data_from_cache is not None: data = json.loads(data_from_cache)
        except redis.exceptions.RedisError as e: print(f"Redis error getting cache for {cache_key}: {e}"); data = None
        except json.JSONDecodeError as e: print(f"Error decoding JSON from cache for {cache_key}: {e}"); data = None

    if data is not None and isinstance(data, dict) and 'time' in data and 'html' in data:
        if time.time() - data['time'] <= 600: # 600 seconds = 10 minutes
            print(f"Cache hit for route: /")
            return data['html']
        else: print(f"Cache expired for route: /")
    else: print(f"Cache miss for route: /")

    # --- CACHE MISS or EXPIRED ---
    print(f"Regenerating content for route: /")
    page_title = "Home Page"
    generated_html = render_template('index.html', title=page_title)

    if r:
        try: r.set(cache_key, json.dumps({'html': generated_html, 'time': time.time()}))
        except redis.exceptions.RedisError as e: print(f"Redis error setting cache for {cache_key}: {e}")

    return generated_html

@app.route('/about')
def about():
    cache_key = 'about' # Unique key
    data = None
    if r:
        try:
            data_from_cache = r.get(cache_key)
            if data_from_cache is not None: data = json.loads(data_from_cache)
        except redis.exceptions.RedisError as e: print(f"Redis error getting cache for {cache_key}: {e}"); data = None
        except json.JSONDecodeError as e: print(f"Error decoding JSON from cache for {cache_key}: {e}"); data = None

    if data is not None and isinstance(data, dict) and 'time' in data and 'html' in data:
        if time.time() - data['time'] <= 600:
            print(f"Cache hit for route: /about")
            return data['html']
        else: print(f"Cache expired for route: /about")
    else: print(f"Cache miss for route: /about")

    # --- CACHE MISS or EXPIRED ---
    print(f"Regenerating content for route: /about")
    page_title = "About Us"
    generated_html = render_template('about.html', title=page_title)

    if r:
        try: r.set(cache_key, json.dumps({'html': generated_html, 'time': time.time()}))
        except redis.exceptions.RedisError as e: print(f"Redis error setting cache for {cache_key}: {e}")

    return generated_html

@app.route('/contact')
def contact():
    cache_key = 'contact' # Unique key
    data = None
    if r:
        try:
            data_from_cache = r.get(cache_key)
            if data_from_cache is not None: data = json.loads(data_from_cache)
        except redis.exceptions.RedisError as e: print(f"Redis error getting cache for {cache_key}: {e}"); data = None
        except json.JSONDecodeError as e: print(f"Error decoding JSON from cache for {cache_key}: {e}"); data = None

    if data is not None and isinstance(data, dict) and 'time' in data and 'html' in data:
        if time.time() - data['time'] <= 600:
            print(f"Cache hit for route: /contact")
            return data['html']
        else: print(f"Cache expired for route: /contact")
    else: print(f"Cache miss for route: /contact")

    # --- CACHE MISS or EXPIRED ---
    print(f"Regenerating content for route: /contact")
    page_title = "Contact Page"
    generated_html = render_template('contact.html', title=page_title)

    if r:
        try: r.set(cache_key, json.dumps({'html': generated_html, 'time': time.time()}))
        except redis.exceptions.RedisError as e: print(f"Redis error setting cache for {cache_key}: {e}")

    return generated_html

# You only need this if running directly with "python app.py"
# For Docker, the CMD or ENTRYPOINT usually handles running the app
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)