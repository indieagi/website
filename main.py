from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/events/jug-island-picnic')
def jug_island_picnic():
    return render_template('events/jug-island-picnic.html')

@app.route('/events/intro-to-full-stack-llm')
def intro_to_full_stack_llm():
    return render_template('events/intro-to-full-stack-llm.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))