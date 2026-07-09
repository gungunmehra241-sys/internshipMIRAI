import streamlit as st
#UI Shell : Task 1

st.title("The Echoing Interface")
st.write("This webpage will require your name and a message")

#multi data collection : Task 2
userName = st.text_input("Enter your full name:")
userMessage = st.text_input("Write your message:")

# Action Gate :Task 3

transmit=st.button("TRANSMIT")

# Edge Cases: Task 4
if transmit:
    if not userName:
         st.error("Please provide your name.")
    elif not userMessage:
         st.warning("Please type a message to transmit.")
#Formatted output: Task 5
    else:
     st.success(f"Transmission successful! Greetings, {userName}."
                f"We received your message: {userMessage}")
     # Advanced Challenge: Token Cost Estimator
     char_count = len(userMessage)
     token_count = char_count // 4  
 
     st.info(f"System Check: Your message will consume approximately "
          f"{token_count} tokens from our context window.")
