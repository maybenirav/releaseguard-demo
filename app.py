from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from the ReleaseGuard demo app!"


if __name__ == "__main__":
    app.run()
