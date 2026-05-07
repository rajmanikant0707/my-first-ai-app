import streamlit as st
from google import genai

st.title("My First AI App 🤖")
user_input = st.text_input("Ask me anything:")

if st.button("Generate Answer"):
    # We use a try block to catch the secret and the error safely
    try:
        # Step A: Explicitly grab the key
        my_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=my_key)
        
        with st.spinner("Thinking..."):
            # Step B: Call the AI
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_input,
            )
            st.success("Done!")
            st.write(response.text)
            
    except KeyError:
        st.error("❌ The app cannot find 'GEMINI_API_KEY' in the Streamlit secrets. Please check the spelling in your settings.")
    except Exception as e:
        st.error("🚨 Here is the REAL error Google is sending us:")
        st.code(str(e))
