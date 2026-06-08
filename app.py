from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"sistema": "POS Cafetería Independiente", "estado": "Activo y escalando"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
