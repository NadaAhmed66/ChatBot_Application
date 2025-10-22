# 💬 AI Chatbot using Google Gemini API & Streamlit

This project is a simple **AI Chatbot** built with **Streamlit** and **Google Gemini (Generative AI)**.
It allows users to interact with an AI model directly from a web interface, maintaining chat history and generating real-time responses.

---

## 🚀 Features

* 🧠 Uses **Google Gemini 2.5 Flash** for fast, high-quality text generation
* 💻 Built with **Streamlit** for an interactive web UI
* 💬 Keeps chat history within the session
* ⚡ Simple, lightweight, and easy to deploy

---

## 🧩 Tech Stack

* **Python 3.10+**
* **Streamlit**
* **Google Generative AI SDK (`google-generativeai`)**

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/chatbot-gemini.git
   cd chatbot-gemini
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # for macOS/Linux
   venv\Scripts\activate      # for Windows
   ```

3. **Install dependencies**

   ```bash
   pip install streamlit google-generativeai
   ```

4. **Add your Google API key**

   * Replace the value of `api` in `chatbot.py` with your actual API key:

     ```python
     api = "YOUR_API_KEY_HERE"
     ```

   **⚠️ Important:** Never expose your API key publicly (e.g., in GitHub).
   Instead, you can load it securely from Streamlit secrets or environment variables:

   ```python
   import os
   api = os.getenv("GOOGLE_API_KEY")
   ```

---

## ▶️ Run the App

In the terminal, run:

```bash
streamlit run chatbot.py
```

Then open the local URL displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 🧠 How It Works

1. The user enters a message in the Streamlit chat input.
2. The app sends the message to the **Gemini 2.5 Flash model** via the Google Generative AI API.
3. The model generates a text response.
4. Streamlit displays both user and assistant messages, keeping the conversation history in memory.

---

## 🛠 File Structure

```
chatbot-gemini/
│
├── chatbot.py        # Main Streamlit app
├── README.md         # Project documentation
└── requirements.txt  # (Optional) Dependencies list
```

Example `requirements.txt`:

```
streamlit
google-generativeai
```

---

## 💡 Future Improvements

* Add support for image or voice input
* Save chat history to a file or database
* Deploy the app on **Streamlit Cloud** or **Render**

---

## 🧾 License

This project is open-source under the **MIT License** — feel free to modify and use it for your own projects.

