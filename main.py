import streamlit as st
import google.generativeai as genai
    
    
 
# 1. Setup API Key (Replace with your actual key or use secrets)
genai.configure(api_key="AIzaSyDwb2_B-q9T3_C1F5GskR0VITgPlCycJKc")
 
# 2. System Instructions: This "locks" the AI into a Math-only role
SYSTEM_PROMPT = """
You are a friendly and helpful Math Tutor for school students. Solve problems step-by-step. Explain the 'why' behind each step.
STRICT RULE: You only answer mathematics-related questions. 
If the user asks about anything else (history, science, general chat, coding, etc.), 
politely explain that you are a Math specialist and can only help with math problems.
Always show your work step-by-step.
"""
# 2. Configure the Model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    system_instruction=SYSTEM_PROMPT)


# 3. Streamlit UI
st.set_page_config(page_title="Math Whiz AI", page_icon="📐")
st.title("Math : Your AI Tutor")
st.markdown("Type your math problem below, and I'll help you solve it step-by-step!")

# User input
user_query = st.text_area("Enter your math question:", placeholder="e.g., Solve for x: 2x + 5 = 15")

if st.button("Solve it!"):
    if user_query:
        with st.spinner("Thinking... "):
            try:
                # Generate response
                response = model.generate_content(user_query)
                
                # Display solution
                st.success("Here is the solution:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question first!")

st.divider()
st.caption("Happy Learning! if you have any feedback, Let me Know!")