import streamlit as st
import ollama

st.title("👀 Describe Image")
st.write("llama3.2-vision")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image")

    # Convert uploaded file to bytes
    image_bytes = uploaded_file.getvalue()

def chat_with_llm(user_query):

    # Send image to Ollama
    response = ollama.chat(
        model="llama3.2-vision",   
        messages=[
            {
                "role": "user",
                "content": user_query,
                "images": [image_bytes]  # Pass image as bytes inside a list
            }
        ]
    )

    return response

# Streamlit UI
with st.form("my_form"):
    text = st.text_area("Enter text:", "Ask anything..")
    submitted = st.form_submit_button("Submit")

    if submitted:
        response = chat_with_llm(text)
        st.info(response.message.content)

    
