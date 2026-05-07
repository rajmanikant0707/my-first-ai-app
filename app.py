import streamlit as st
from google import genai

st.title("My First AI App 🤖")
user_input = st.text_input("Ask me anything:")
if st.button("Generate Answer"):
    if user_input:
        with st.spinner("The AI is thinking..."):
            # Notice how these three lines below are perfectly aligned on the left
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=user_input,
            )
            st.success("Done!")
            st.write(response.text)
            
    except KeyError:
        st.error("❌ The app cannot find 'GEMINI_API_KEY' in the Streamlit secrets. Please check the spelling in your settings.")
    except Exception as e:
        st.error("🚨 Here is the REAL error Google is sending us:")
        st.code(str(e))
