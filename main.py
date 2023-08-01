from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events/intro-to-full-stack-llm')
def intro_to_full_stack_llm():
    return render_template('intro_to_full_stack_llm.html')

@app.route('/events/intro-to-full-stack-llm/notebook')
def notebook():
    return render_template('notebook.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))