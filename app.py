from flask import Flask

app =Flask(__name__)

@app.route("/")
def index():
    return "This is my Matrivume Application Pipeline"

if __name__ == "__main__":
    app.run(use_reloader=True)

