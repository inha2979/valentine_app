from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.get("/")
def index():
    # cache-bust image with a simple query string if you change the file later
    return render_template("index.html", img_url=url_for("static", filename="valentine.jpg"))

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
