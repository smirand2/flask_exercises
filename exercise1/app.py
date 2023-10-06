from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def show_current_time():
    current_time = datetime.datetime.now()

    return render_template('current_time.html', current_time=current_time.strftime("%c"))

if __name__ == '__main__':
    app.run(debug=True)