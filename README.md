# 🤖 AI Chatbot – Streamlit

A simple and interactive **AI Chatbot web application** built using **Python and Streamlit**. The application supports three response modes: **Echo Bot, OpenAI, and Google Gemini**.

It also includes chat history, streaming responses, temperature control, timestamps, chat statistics, and chat download functionality.

---

## 🚀 Features

* 🤖 **Echo Bot** – Returns the user's message as a response.
* 🧠 **OpenAI** – Generate AI responses using OpenAI models.
* ✨ **Google Gemini** – Generate AI responses using Gemini.
* 💬 **Chat History** – Maintains conversation history during the session.
* 🔄 **Streaming Responses** – Displays AI responses progressively.
* 🌡️ **Temperature Control** – Adjust the creativity of AI responses.
* 🕒 **Timestamps** – Displays the time of each message.
* 📊 **Chat Statistics** – Shows:

  * User message count
  * Assistant message count
  * Total message count
* 🗑️ **Clear Chat** – Reset the conversation.
* ⬇️ **Download Chat** – Download the conversation as a `.txt` file.
* 🔐 **Environment Variables** – API keys are stored securely using `.env`.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **OpenAI API**
* **Google Gemini API**
* **python-dotenv**

---

## 📁 Project Structure

```text
AI-Chatbot/
│
├── AI_Chatbot.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Chatbot.git
```

Navigate to the project directory:

```bash
cd AI-Chatbot
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install streamlit openai google-genai python-dotenv
```

---

## 🔑 API Key Configuration

Create a file named:

```text
.env
```

in the project root directory.

Add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### ⚠️ Security

Never hard-code API keys inside your Python code.

Do **not** commit `.env` to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run AI_Chatbot.py
```

Streamlit will open the chatbot in your browser.

---

## 🧩 How It Works

The application provides three model options.

### 1. Echo Bot

Select:

```text
Echo Bot
```

The chatbot simply returns the message entered by the user.

Example:

```text
User:
Hello

Bot:
You said: Hello
```

---

### 2. OpenAI

Select:

```text
Open AI
```

The application sends the conversation history to the OpenAI API and streams the generated response.

The OpenAI API key is loaded from:

```env
OPENAI_API_KEY
```

---

### 3. Google Gemini

Select:

```text
Gemini AI
```

The application sends the conversation history to Google Gemini and streams the generated response.

The Gemini API key is loaded from:

```env
GEMINI_API_KEY
```

---

## 🌡️ Temperature

The sidebar contains a temperature slider.

```text
0.0 ─────────────── 1.0
```

Lower temperature:

* More predictable responses
* Less variation

Higher temperature:

* More creative responses
* More variation

---

## 💬 Chat History

Messages are stored in Streamlit session state:

```python
st.session_state.messages
```

Each message contains:

```python
{
    "Role": "User",
    "Content": "Hello",
    "Time": "06:30 PM"
}
```

This allows the application to maintain the conversation while the Streamlit session is active.

---

## 📊 Chat Statistics

The sidebar displays:

```text
User Messages
Assistant Messages
Total Messages
```

These values are calculated from the current chat history.

---

## ⬇️ Download Chat

The **Download Chat** button allows users to save the conversation as:

```text
chat_history.txt
```

The downloaded file contains the role, timestamp, and message content.

---

## 🖥️ Application Interface

The application contains:

```text
┌─────────────────────────────────────────────┐
│                🤖 AI Chatbot                │
│                                             │
│  User: Hello                                │
│                                             │
│  Assistant: Hello! How can I help you?     │
│                                             │
│                                             │
│  Type your message here...                  │
└─────────────────────────────────────────────┘

Sidebar
├── Choose Model
├── Temperature
├── Clear Chat
├── Chat Statistics
├── Current Time
└── Download Chat
```

---

## 📦 requirements.txt

Create a `requirements.txt` file containing:

```text
streamlit
openai
google-genai
python-dotenv
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🚫 .gitignore

Create a `.gitignore` file:

```text
.env
venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

---

## 🔐 API Key Safety

API keys are sensitive credentials.

### Never do this:

```python
OPENAI_API_KEY = "sk-xxxxxxxx"
```

### Instead:

```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

And store the key in `.env`.

---

## 🐛 Troubleshooting

### API key not found

If you see:

```text
OpenAI API key not found
```

or:

```text
Gemini API key not found
```

check that your `.env` file contains:

```env
OPENAI_API_KEY=your_key
GEMINI_API_KEY=your_key
```

Then restart Streamlit.

---

### ModuleNotFoundError

If you see:

```text
ModuleNotFoundError
```

install the dependencies:

```bash
pip install -r requirements.txt
```

---

### Streamlit not recognized

Try:

```bash
python -m streamlit run Vijay_Chatbot.py
```

---

## 🔮 Future Improvements

Possible future enhancements:

* 🎙️ Voice input
* 🔊 Text-to-speech
* 📎 File upload
* 🖼️ Image understanding
* 🌐 Web search
* 👤 User authentication
* 💾 Persistent database chat history
* 🎨 Custom chatbot themes
* 🧠 System prompts
* 📱 Mobile-friendly interface
* 📈 Usage and token tracking
* 🗂️ Multiple conversations

---

## 🎯 Project Purpose

This project demonstrates how to build a **multi-model AI chatbot** using Python and Streamlit.

It is useful as a beginner/intermediate project for learning:

* Python
* Streamlit
* API integration
* Generative AI
* Conversation history
* Environment variables
* Streaming responses
* Basic chatbot UI development

---

## 👨‍💻 Author

**Sriram R**

AI/ML Enthusiast | Python | Machine Learning | Generative AI

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is available for educational and personal use.
