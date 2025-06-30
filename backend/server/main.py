from flask import Flask, request, jsonify, render_template
from backend.app.workflows.rag_pipeline import rag_pipeline
import os
import asyncio

app = Flask(__name__, template_folder='../../frontend/templates', static_folder='../../frontend/static')

# Homepage
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Chat route
@app.route("/rag", methods=['POST'])
def run_rag():
    if "pdf" not in request.files or "query" not in request.form:
        return jsonify({"error": "Missing PDF or query"})
    
    file = request.files["pdf"]
    user_input = request.form["query"]
    use_semantic = request.form.get("use_semantic", "false").lower() == "false"

    print(f"[DEBUG] File: {file.filename}, Query: {user_input}")

    # Save uploaded file to a temp location
    file_path = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)
    file.save(file_path)

    try:
        answer = asyncio.run(rag_pipeline(file_path, user_input, use_semantic))
        os.remove(file_path) # Clean up to remove the file
        return jsonify({"answer": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("[INFO] Starting Flask server on http://127.0.0.1:7860")
    port = int(os.getenv("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=True)
