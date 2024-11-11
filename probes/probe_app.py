from flask import Flask, send_from_directory
import time
import os

app = Flask(__name__)

# Simulate a delayed startup time for the app
startup_delay = 15  # seconds
app_start_time = time.time()  # record the time the app started

# Health check endpoint for liveness probe
@app.route('/healthz')
def health():
    return "Healthy", 200

# Readiness check endpoint for readiness probe
@app.route('/readyz')
def ready():
    # Assume the app is "ready" only if it has been running for more than 10 seconds
    if time.time() - app_start_time > 10:
        return "Ready", 200
    else:
        return "Not ready", 503

# Root endpoint for general access
@app.route('/')
def index():
    return """
    <html>
    <head>
      <title>Kubernetes Probes Demo</title>
      <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
      <style>
        body {{
          background-image: url('/static/k8s-bg.jpg');
          background-size: cover;
          color: white;
          text-align: center;
          font-family: Arial, sans-serif;
        }}
        h1 {{
          margin-top: 20%;
          background-color: rgba(0, 0, 0, 0.5);
          padding: 20px;
          border-radius: 10px;
        }}
      </style>
    </head>
    <body>
    <center>
      <h1>Welcome to the Kubernetes Probes Demo App!</h1>
      <center>
    </body>
    </html>
    """

# Serve the favicon (Flask automatically serves static files from the static folder)
# No need for a custom route for this, Flask will do it automatically
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Serve the background image (Flask automatically serves static files from the static folder)
# No need for a custom route for this, Flask will do it automatically
@app.route('/k8s-bg.jpg')
def background_image():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'k8s-bg.jpg', mimetype='image/jpeg')

# Run the app after a simulated startup delay
if __name__ == '__main__':
    time.sleep(startup_delay)  # simulate startup time delay
    app.run(host='0.0.0.0', port=8080)
