import streamlit as st
from google import genai

# Look how simple this is now! No st.secrets mentioned at all.
# The SDK will automatically look for your key in the background.
client = genai.Client()

st.title("My First AI App 🤖")

user_input = st.text_input("Ask me anything:")

if st.button("Generate Answer"):
    if user_input:
        with st.spinner("The AI is thinking..."):
            # Call the AI
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_input,
            )
            st.success("Done!")
            st.write(response.text)
    else:
        st.warning("Please type a question first.")
