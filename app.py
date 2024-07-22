from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

@app.route('/')
def index():
    return redirect(url_for('edit_profile'))

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    message = ""
    if request.method == 'POST':
        user_data['name'] = request.form['name']
        user_data['email'] = request.form['email']
        # Normally you should hash the password and save it securely
        password = request.form['password']
        message = "Profile updated successfully!"

    return render_template('edit_profile.html',
                           name=user_data['name'],
                           email=user_data['email'],
                           message=message)

if __name__ == '__main__':
    app.run(debug=True)

