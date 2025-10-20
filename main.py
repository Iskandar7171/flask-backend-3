from flask import Flask
app = Flask("__name__")
@app.route("/")
def home():
    return "salom dunyo"

@app.route("/")

if __name__ == '__main__':1
    app.run(debug=True)