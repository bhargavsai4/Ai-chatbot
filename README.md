🤖 AI Chat Assistant — Flask + Transformers + Wikipedia

A modern, interactive chatbot web app powered by HuggingFace Transformers (Flan-T5) with real-time Wikipedia-enhanced context. This bot combines a friendly ChatGPT-style UI with an open-source backend and zero training required.

✨ Features

🔍 Retrieval-Augmented Generation (RAG): Wikipedia summaries power better answers

💬 Chat UI like ChatGPT: Stylish, responsive, and animated frontend

🤖 FLAN-T5 Transformer model: Handles general questions well without fine-tuning

🧠 Smart Prompting: Context-aware generation when possible

👋 Greeting Filtering: Ignores simple greetings and replies politely

⚡ Instant Answers: No backend DB, deploys with a single command

📁 Project Structure
chatbot-transformer/
├── app.py                 # Flask server and model logic
├── retrievers/wiki.py     # Wikipedia context fetcher
├── templates/index.html   # Chat UI (served by Flask)
├── static/
│   ├── style.css          # Chat layout and styling
│   └── script.js          # Message send/receive logic
├── requirements.txt       # Python dependencies
└── README.md              # You are here!

🧪 Demo (Try It Locally)

Clone this repo

Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser and go to:

http://localhost:5000

💬 Example Questions

“What is photosynthesis?”
“Who is Alan Turing?”
“What is the capital of France?”
“What is gravity?”

🧠 Powered By

Flan-T5 base
 (Hugging Face)

wikipedia Python package

Flask (backend API)

Vanilla HTML, CSS, JS (frontend)

📌 Future Improvements

🗃 Add memory & chat history

🌐 Add web search fallback (DuckDuckGo, Google)

💾 Store Q&A logs or trainable FAQ

🌈 Dark mode toggle

🧑‍💻 Swap models with OpenAI / Mistral / LLaMA via HuggingFace

📜 License

This project is MIT licensed and free to use for learning, demos, or personal projects.
Pull requests are welcome!
