from flask import Flask, request, render_template
from modules import get_track
app = Flask(__name__, template_folder='templates')
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/", methods = ['POST'])
def tracked():
    try:
        result = []
        get_track.config()
        t_id = str(request.form['tracking_number'])
        t_id = t_id.split(',')
        for tracking_id in t_id:
            result.append(get_track.get_tracking_info(tracking_id))
        if result is None:
            return "ERROR 404"
        else:
            return render_template("Tracking.html", result=result)
    except Exception as e:
        return "Error"
 
if __name__ == '__main__':
    app.run(debug=True)