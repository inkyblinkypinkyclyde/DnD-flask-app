from flask import Flask
from controllers.character_controller import characters_blueprint


app = Flask(__name__)
app.register_blueprint(characters_blueprint)

@app.route('/')
def home():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True, port=5001)