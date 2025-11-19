from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from retrievers.wiki import get_wikipedia_summary

app = Flask(__name__)

# Load instruction-tuned model
model = pipeline("text2text-generation", model="google/flan-t5-base")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"answer": "Please enter a valid question."})

    # 🛑 Skip generic greetings
    greetings = {"hi", "hello", "hey", "hola", "namaste", "yo", "sup", "hii", "heyy"}
    if query.lower() in greetings:
        return jsonify({"answer": "👋 Hello! How can I assist you today?"})

    # Retrieve context from Wikipedia
    context = get_wikipedia_summary(query)

    # Smart prompt format
    if context:
        prompt = (
            f"Context: {context}\n\n"
            f"Question: {query}\n\n"
            f"Instruction: Answer clearly and informatively."
        )
    else:
        prompt = (
            f"Question: {query}\n\n"
            f"Instruction: Provide a clear and helpful answer."
        )

    try:
        output = model(prompt, max_new_tokens=200)[0]["generated_text"]
        return jsonify({"answer": output.strip()})
    except Exception as e:
        return jsonify({"answer": f"Error generating response: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
