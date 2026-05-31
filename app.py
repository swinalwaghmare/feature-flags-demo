from flask import Flask, render_template
import json

app = Flask(__name__)

def get_flags():
    with open("flags.json") as f:
        return json.load(f)
    
@app.route("/")
def home():
    flags = get_flags()
    return render_template("index.html", flags=flags)

@app.route("/dashboard")
def dashboard():
    flags = get_flags()
    if not flags.get("new_dashboard"):
        return "Feature not available yet!", 403
    return render_template("new_feature.html")

if __name__ == "__main__":
    app.run(debug=True)