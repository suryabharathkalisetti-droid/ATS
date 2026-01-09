from flask import Flask, request, jsonify, render_template
from google import genai

client = genai.Client(
    api_key="AIzaSyB0SIBpgry7TbD2XndXUjsIxW8PIGD0B"
)

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["message"]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

app.run(port=8080)