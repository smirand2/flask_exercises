from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Common layout template
@app.route('/')
def home():
    return render_template('layout.html')

# Route for displaying the result
@app.route('/result', methods=['GET', 'POST'])
def result():
    number = request.args.get('number')

    if number is None:
        return "Error: No number parameter provided."

    try:
        number = int(number)
        if number % 2 == 0:
            result_text = "Even"
        else:
            result_text = "Odd"
    except ValueError:
        number = str(number)
        result_text = "Not an integer"

    return render_template('result.html', number=number, result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
