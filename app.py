from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Scrape-Health!"

if __name__ != "__main__":
    # For Gunicorn (used by Render)
    application = app
else:
    app.run()
