from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
   # url = random.choice(images)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
