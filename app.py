import streamlit as st
from google import genai

# Initialize the new GenAI client
# Replace 'YOUR_API_KEY' with your actual key!
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 1. Build the User Interface
st.title("My First AI App 🤖")
st.write("A simple application to test my coding knowledge.")

# 2. Create an input box for the user
user_input = st.text_input("Ask me anything:")

# 3. Add the logic to trigger the AI
if st.button("Generate Answer"):
    if user_input:
        with st.spinner("The AI is thinking..."):
            # Use the new SDK syntax and the 2.5-flash model we saw in your list!
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_input,
            )
            
            # Display the result on the screen
            st.success("Done!")
            st.write(response.text)
    else:
        st.warning("Please type a question first.")