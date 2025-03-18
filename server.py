from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-this'  # Needed for flash messages

# Basic routes
@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/game")
def game():
    return render_template("game.html", title="Play Chess")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/rules")
def rules():
    return render_template("rules.html", title="Chess Rules")

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Here you would normally process the form data
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would normally process the login
        flash('Logged in successfully!')
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In')

if __name__ == "__main__":
    app.run(debug=True)
