import streamlit as st
from datetime import datetime
from openai import OpenAI
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


# 1. Assistant
# 2. User
# 3. Chat History

# Add-on Features

# 1. Sidebar
# 2. Clear Chat
# 3. Timestamps
# 4. Selection of Models
# 5. Temperature
# 6. Chat Statistics

load_dotenv()

# ========== Streamlit Page Configuration ==========

st.set_page_config(  
    page_title = "Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Chatbot")
st.caption("Powered by Streamlit")

# API Keys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# API Clients

openai_client = None
gemini_client = None

if OPENAI_API_KEY:
    openai_client = OpenAI(api_key = OPENAI_API_KEY)

if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key = GEMINI_API_KEY)

# Session State

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "Role": "Assistant",
            "Content": "Hey, How can I help you?",
            "Time": datetime.now().strftime("%I:%M %p")
        }
    ]

def current_time():
    return datetime.now().strftime("%I:%M %p")  # %I - Hour (12 Hr format), %M - Mintues, %p - AM or PM

# ========== Side Bar ==========

with st.sidebar:
    st.header("⚙️ Settings")

# SelectBox to select the LLM's

    model = st.selectbox("Choose Model",["Echo Bot", "Open AI", "Gemini AI"])

# Model Temperature

temperature = st.slider(
    "Temperature", min_value = 0.0, max_value = 1.0, value = 0.7
)
st.divider()

# ========== Clearing Chat History ==========

if st.button("🗑️ Clear Chat", use_container_width = True):
    st.session_state.messages = [
        {
            "Role": "Assistant",
            "Content": "Hey, How can I help you?",
            "Time": current_time()
        }
    ]

    st.rerun()
st.divider()

# ========== Chat Statistics ==========

st.subheader("📊 Chat Statistics")

user_count = sum(
    1 for msg in st.session_state.messages if msg["Role"] == "User"
)

assistant_count = sum(
    1 for msg in st.session_state.messages if msg["Role"] == "Assistant"
)

total_count = len(st.session_state.messages)

st.metric("User Messages", user_count)
st.metric("Assistant Messages", assistant_count)
st.metric("Total Messages", total_count)

st.divider()

# Current Time

st.subheader("🕒 Current Time")

st.info(current_time())

# Download Chat

st.subheader("💾 Download Chat")

chat_history = ""

for msg in st.session_state.messages:
    chat_history += (
        f"{msg['Role'].title()}"
        f"({msg['Time']})\n"
        f"{msg['Content']}\n\n"
    )

st.download_button(
    "⬇️ Download Chat",
    chat_history, 
    file_name = "chat.history.txt", mime = "text/plain", use_container_width = True
)

# ========== Generate Response ==========

def generate_response(user_message):

    # ECHO BOT

    if model == "Echo Bot":

        response = f"You said: {user_message}"

        for word in response.split():
            yield word + " "

        return

    # OPEN AI

    if model == "Open AI":

        if openai_client is None:

            yield (
                "❌ Open AI key not found.\n\n"
                "Please add OPENAI_API_KEY to your .env file"
            )

            return

        messages = []

        for msg in st.session_state.messages:

            if msg["Role"] == "User":

                messages.append({
                    "Role": "user",
                    "Content": content
                })

            elif msg["Role"] == "Assistant":

                if content == "Hey, how can I help you?":
                    continue

                messages.append({
                    "Role": "Assistant",
                    "Content": content
                })

    try:
        stream = openai_client.chat.completions.create(
            model = "gpt-5-mini",
            messages = messages,
            temperature = temperature,
            stream = True
        )

        for chunk in stream:

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                yield content

    except Exception as e:

        yield f"❌ OpenAI Error: {str(e)}"

    return

    # ========== GEMINI AI ==========

    if model == "Gemini AI":

        if gemini_client is None:

            yield (
                "❌ Gemini API key not found.\n\n"
                "Please add GEMINI_API_KEY to your .env file"
            )

            return

        # Build Gemini Conservation

            contents = []

            for msg in st.session_state.messages:

                # Skip empty messages

                if not msg["Content"]:
                    continue

                if msg["Role"] == "User":

                    contents.append(types.Content(
                        role = "user", 
                        parts = [types.Part
                                (text = msg["Content"])]
                    ))

                elif msg["Role"] == "Assistant":

                    contents.append(types.Content(
                        role = "model", parts = [types.Part.from_text(text = msg["Content"])]
                    ))

        # Create Chat

        chat = gemini_client.chats.create(model = "gemini-3.6-flash",
                                          history = contents, config = types.GenerateContentConfig(temperature = temperature))

        # Stream Gemini Response

        response_stream = chat.send_message_stream(message = user_message)

        for chunk in response_stream:
            if chunk.text:
                yield chunk.text

    except Exception as e:

        yield f"❌ Gemini Error: {str(e)}"

    return

st.divider()

# ========== Displaying the previous messages ==========

for message in st.session_state.messages:

    role = message["Role"].lower()

    if role not in ["User", "Assistant"]:

        role = "Assistant"

    with st.chat_message(role):
        st.write(message["Content"])
        st.caption(message["Time"])

# ========== User Input ==========

user_message = st.chat_input("Type the message here.....")

if user_message:

    user_time = current_time()

    # Displaying the user message

    with st.chat_message("user"):
        st.write(user_message)
        st.caption(user_time)

    # Storing user message

    st.session_state.messages.append(
        {
            "Role": "User",
            "Content": user_message,
            "Time": user_time
        }
    )

# Generate Assistant Response

assistant_time = current_time()

# ========== Assistant Response ==========

with st.chat_message("assistant"):

# Sreaming the response

    with st.spinner("Generating Response...."):
        bot_response = st.write_stream(
            generate_response(user_message)
        )
    st.caption(assistant_time)

# Save the complete response

st.session_state.messages.append(
    {
        "Role": "Assistant",
        "Content": bot_response,
        "Time": assistant_time
    }
)


# =========================================================================================================================================================
