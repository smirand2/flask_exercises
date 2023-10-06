from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store user registrations
user_registrations = {}

# List of hardcoded organizations
organizations = ['Org1', 'Org2', 'Org3', 'Org4', 'Org5']

@app.route('/')
def home():
    return render_template('home.html', organizations=organizations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    # Backend validation
    if not name or not organization or organization not in organizations:
        return "Invalid input. Please go back and try again."

    # Add the user to the dictionary
    user_registrations[name] = organization

    return redirect(url_for('users'))

@app.route('/users')
def users():
    # Preprocess the data to include an index
    user_list = [(index, name, organization) for index, (name, organization) in enumerate(user_registrations.items(), 1)]
    return render_template('users.html', user_list=user_list)

if __name__ == '__main__':
    app.run(debug=True)
