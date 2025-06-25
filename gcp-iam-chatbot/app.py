from flask import Flask, request, jsonify
from mcp.recommender_client import get_iam_recommendations

app = Flask(__name__)

@app.route("/recommendations", methods=["GET"])
def recommendations():
    project_id = request.args.get("project_id")
    return jsonify(get_iam_recommendations(project_id))

if __name__ == "__main__":
    app.run(debug=True)