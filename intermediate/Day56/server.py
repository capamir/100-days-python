from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    template_name = 'index.html'
    return render_template(template_name)

@app.route('/page')
def identity():
    template_name = 'identity.html'
    return render_template(template_name)


if __name__ == "__main__":
    app.run(debug=True)
