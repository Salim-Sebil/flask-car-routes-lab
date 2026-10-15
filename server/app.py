existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flatiron Cars"

@app.route('/<string:models>')
def get_model(models):
    if models in existing_models:
        return f"Flatiron {models} is in our fleet!"
    else:
        return f"No models called {models} exists in our catalog"

if __name__ == '__main__':
    app.run(port=5555, debug=True)