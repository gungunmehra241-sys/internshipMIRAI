import streamlit as st
st.title("THE AI MULTIVERSE OF KNOWLEDGE!!")
writer = st.selectbox("Select the author : ",["Jane Austen","William Shakespeare","Charles Dickens","George Orwell","Haruki Murakami"])
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("Gemini_Api_Key"))
novel =  st.text_input("Write the name of the novel you are planning to read.")
if st.button("SEND"):
    if novel:
        ai_instructions=f"you have to give reviews on the book {novel}"
        with st.spinner("Connecting to the multiverse!...."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )
            st.success("Review received")
            st.write(response.text)
    else :
        st.warning("Please type the name first")
