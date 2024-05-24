from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute-notebook')
def execute_notebook():
    try:
        # Execute the Jupyter Notebook
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "seen.ipynb"])
        return jsonify({"message": "Notebook executed successfully!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
