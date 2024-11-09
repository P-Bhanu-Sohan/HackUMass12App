import openai
import time
import streamlit as st
from PIL import Image

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
st.set_page_config(page_title="UMass Food Assistant", page_icon="🍴")

backgroundColor="#FFCDD2"

# Load the local image and display it centered
image_path = 'maxresdefault.jpg'  # Path to your local images
img = Image.open(image_path)

# Display the image and center it with a larger size
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(img, width=500)  # Adjust width to make the image bigger or smaller
st.markdown("</div>", unsafe_allow_html=True)

# Center the title
st.markdown("<h1 style='text-align: center;'>UMass Food Assistant</h1>", unsafe_allow_html=True)

st.write("Feel free to ask about dining suggestions at UMass!")

# Text input for user query (no custom background, default style)
user_message = st.text_input("Ask me something about food:", "")

# Button to send the message
if st.button("Send"):
    if user_message:
        # Create a new thread for each session
        thread = openai.beta.threads.create()
        response = send_message(thread.id, user_message)
        st.write(f"Assistant: {response}")
    else:
        st.write("Please enter a message!")
