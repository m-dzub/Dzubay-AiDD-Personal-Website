from flask import Flask, render_template, request, redirect, url_for

# Serve static files directly from the project root so existing `assets/` and `images/` folders work
app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In a real site you'd send/store the message. Here we'll just redirect to thanks.
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return redirect(url_for('thanks'))
    return render_template('contact.html')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)
