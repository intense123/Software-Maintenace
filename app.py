from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Flask App",
        "status": "running"
    })

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({
        "greeting": f"Hello, {name}!"
    })

@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({
        "sum": a + b
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Route not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
