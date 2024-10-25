import streamlit as st
import google.generativeai as genai

api_key=st.secrets["GEN_API_KEY"]
# Configure the Generative AI API
genai.configure(api_key=api_key) 

# Streamlit App layout
st.title("OMAN AI")

# Text input for user query
question = st.text_input("Enter Your Query:")

# Generate response when button is clicked
if st.button("Generate Response"):
    if question:
        # Define model and generate response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        
        # Display the response in the Streamlit app
        st.subheader("AI Response:")
        st.write(response.text)
    else:
        st.error("Please enter a query first!")
