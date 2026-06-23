from flask import Flask, jsonify, render_template
import psutil, time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def stats():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "uptime": round((time.time() - psutil.boot_time()) / 3600, 1),
        "disk": psutil.disk_usage("/").percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
