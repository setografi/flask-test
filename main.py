from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Optionally pass data to the template
    title = "My Flask App"
    message = "Hello World!"
    if request.method == 'POST':
        input_text = request.form['input_text']
        return render_template('index.html', input_text=input_text)
    return render_template('index.html', title=title, message=message, input_text=None)

if __name__ == '__main__':
    app.run(debug=True)
