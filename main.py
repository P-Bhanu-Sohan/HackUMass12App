import streamlit as st
import openai
import time
from PIL import Image

# Streamlit page configuration
st.set_page_config(page_title="UMass Food Assistant", page_icon="🍴")

# Apply custom CSS to set the background color to pastel green and center the logo
st.markdown(
    """
    <style>
    /* Set background color for the main app */
    .stApp {
        background-color: #98FB98;
    }
    /* Center the image */
    .centered-image {
        display: block;
        margin: 0 auto;
        width: 50%;  /* Adjust as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# OpenAI API key setup
openai.api_key = ''
assistant_id = ''

# Function to send a message to the assistant
def send_message(thread_id, user_message):
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message,
    )

    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    while run.status != "completed":
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )

    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value

# Streamlit UI Setup
# Load the local image and display it centered
image_path = 'logo.png'  # Path to your local image
img = Image.open(image_path)
st.image(img, use_container_width=True, caption=None)  # Updated parameter to fix deprecation

# Center the title and subtitle
st.markdown("<h1 style='text-align: center;'>UMass Food Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your Personal UMass Dining Assistant, Helping you Eat Healthier!</p>", unsafe_allow_html=True)

# Initialize chat history in session state if not already initialized
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Create a container for the chat history
chat_container = st.container()

# Text input for user query with session state for auto-clearing
if "user_message" not in st.session_state:
    st.session_state.user_message = ""

# User input field
user_message = st.text_input("Ask me for food suggestions!", st.session_state.user_message)

# Button to send the message and handle the conversation
if st.button("Send") and user_message:
    # Check if the last message in the history is the same as the new message to avoid duplication
    if not st.session_state["chat_history"] or st.session_state["chat_history"][-1][1] != user_message:
        # Create a new thread for each session
        thread = openai.beta.threads.create()

        # Send the user message to the assistant
        response = send_message(thread.id, user_message)

        # Add the new exchange (user message and assistant response) to the history
        st.session_state["chat_history"].append(("User", user_message))
        st.session_state["chat_history"].append(("Assistant", response))

    # Clear the input box after sending the message
    st.session_state.user_message = ""

# Display the entire chat history
with chat_container:
    # Clear the previous content and display the history cleanly
    st.empty()  # Clear old content
    for role, message in st.session_state["chat_history"]:
        if role == "User":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Assistant:** {message}")