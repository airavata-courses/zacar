from flask import Flask
from modules import get_track
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/tracked")
def tracked():
    return "Tracking Info"
 
if __name__ == "__main__":
    app.run()