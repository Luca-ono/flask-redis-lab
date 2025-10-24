from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    page_title = "Home Page"
    # In a real app, you might fetch data here
    return render_template('index.html', title=page_title)

@app.route('/about')
def about():
    page_title = "About Us"
    # Some logic maybe...
    return render_template('about.html', title=page_title)

@app.route('/contact')
def contact():
    page_title = "Contact Page"
    # Form logic might go here
    return render_template('contact.html', title=page_title)

# You only need this if running directly with "python app.py"
# For Docker, the CMD or ENTRYPOINT usually handles running the app
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)