import streamlit as st

def generate_message(role, company, ending_choice):
    message1 = f"""Hello,  
    
I hope you're doing well! I’m Neel, a final-year B.Tech student at Jain University, Bangalore. I recently came across "{role}" role at {company} and found it a great fit for my skills and interests.

Since you have experience at {company}, I’d love to hear your thoughts on the role and any advice you might have. Also, if you think my profile aligns, I’d truly appreciate a referral."""
    
    message2 = ending_choice
    
    return message1, message2

st.title("Message Generator")
role = st.text_input("Enter the Role:")
company = st.text_input("Enter the Company:")

ending_options = [
    "Besides, experience section in your profile is truly inspiring! 😊. Looking forward to your insights. Thanks in advance!",
    "Besides, About section in your profile is so much engaging 😊! Looking forward to your insights. Thanks in advance!",
    "Besides, Your profile is truly inspiring! 😊 Looking forward to your insights. Thanks in advance!"
]

choice = st.radio("Choose an ending:", ending_options)

if st.button("Generate Message"):
    message1, message2 = generate_message(role, company, choice)
    st.text_area("Generated Message (Main Part)", message1, height=150)
    st.button("Copy Main Message", on_click=lambda: st.session_state.update({"copy_message1": message1}))
    
    st.text_area("Generated Message (Ending)", message2, height=100)
    st.button("Copy Ending Message", on_click=lambda: st.session_state.update({"copy_message2": message2}))
