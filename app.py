from flask import Flask, request, render_template
from modules import get_track
app = Flask(__name__, template_folder='templates')
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/tracked", methods = ['POST', 'GET'])
def tracked():
    if request.method == 'POST':
        get_track.config()
        t_id = request.form['tracking_number']
        result = get_track.get_tracking_info(t_id)
    return render_template("Tracking.html", result=result)
 
if __name__ == '__main__':
    app.run(debug=True)