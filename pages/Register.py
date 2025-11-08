import streamlit as st
import datetime
import pywhatkit
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="Register" ,page_icon="data_files/page_icon.png",layout="centered")

st.markdown(
"""<style>
  body {
    background: radial-gradient(circle at 20% 20%, #00f2fe, #0052cc 70%) fixed !important;
    width: 100%;
    height: 100%;
    font-family: 'Poppins', sans-serif;
  }
  .st-emotion-cache-1r4qj8v {
    background: none !important;
  }
  .background-circles {
    position: absolute;
    inset: 0;
    pointer-events: none;
  }
  .st-emotion-cache-1ffuo7c {
    display: none;
  }
  .st-emotion-cache-4rsbii{
    position: relative;
}
  .st-emotion-cache-1y4p8pa {
    max-width: 800px;
    width: 90%;
    animation: floatUp 1.5s ease-out;
    padding: 0rem 1rem 0rem;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .block-container .st-emotion-cache-0:first-of-type {
    backdrop-filter: blur(20px) saturate(120%);
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 0 32px 35px 35px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    transform-style: preserve-3d;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  .st-emotion-cache-zt5igj {
    left: 0;
    width: 100%;
    }
    .st-emotion-cache-6awftf,.st-emotion-cache-eczf16 {
    display: none;
    }
  .st-emotion-cache-0:first-of-type:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.2);
  }
   #welcome-back,#join-us{
    color: #fff;
    text-align: center;
    margin-bottom: 10px;
    font-size: 2.2rem;
    font-weight: 600;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding-bottom: 10px;
  }
  .st-emotion-cache-7ym5gk {
    width: 100%;
    padding: 14px;
    background: linear-gradient(135deg, #00f2fe 0%, #0052cc 100%);
    border: none;
    border-radius: 12px;
    color: #fff;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  .st-emotion-cache-7ym5gk:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
  }
  .st-emotion-cache-zh2fnc {
    width: auto;
  }
  .stElementContainer {
    position: relative;
  }
  p {
    font-size: 16px !important;
    color: white;
  }
  .st-b7 {
    background-color: transparent;
  }
  input {
    color: white !important;
    caret-color: white !important;
  }
  .st-emotion-cache-ua1rfn span {
    display: none;
  }
.st-cc {
    background-color: rgb(33 152 195 / 27%);
}
st-emotion-cache-4rsbii {
    width: 100%;
    overflow: hidden;
}
.st-c0, .st-c2, .st-c1, .st-bz{
 border:1px solid white !important;
}
.error_popup {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px 0;
    border-radius: 8px;
    background-color: rgb(255 0 0 / 76%);
    margin-bottom: 8px;
}
.error_popup p{
    margin: 0;
}
.st-emotion-cache-1xmp9w2  p{
    text-align: center;
}
.st-emotion-cache-1v0mbdj {
    padding: 10px;
   background: radial-gradient(circle at 20% 20%, #00f2fea1, #0052cc61 70%) fixed !important; 
    border-radius: 50%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}
.st-emotion-cache-9aoz2h  {
    position: absolute;
    top: -50px;
    right: -50%;
    align-items: center;
    transform: translate(-5%, -0%);
}
.st-emotion-cache-10trblm{
    margin-left:  0 !important;
}
.st-emotion-cache-12rj9lz,.st-emotion-cache-1li7dat,.st-emotion-cache-vk3wp9,header{
    display: none !important;
}
[data-testid="column"] .st-emotion-cache-0 {
  backdrop-filter: none !important;
  background: none !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  box-shadow: none !important;
}
[data-testid="column"] .st-emotion-cache-0:hover {
    transform: none;
    box-shadow: 0;
  }

</style>
"""
, unsafe_allow_html=True)


def Reg_msg(phone_num, user_name):

    msg_num = "+92" + phone_num[1:]
    message = (
        f"Welcome {user_name}! Your registration is complete, and your wallet is ready to use. "
        f"This confirmation comes from the Finance App team."
        """Welcome to SmartFinance. Your account has been successfully created.
          You now have access to the full suite of SmartFinance tools, including:
          Secure Digital Wallet for managing your funds
          Real-time Credit Score Monitoring
          Intelligent Financial Advisory System
          Advanced Fraud Detection and Protection
          Start managing your finances with confidence and security."""
    )
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute + 1  
    if minutes >= 60:
        minutes -= 60
        hours = (hours + 1) % 24 
    pywhatkit.sendwhatmsg(msg_num, message, hours, minutes)
    print("Your confirmation message was successfully delivered.")


def Reg(user_name,user_cnic, mobile_num,user_password):
    user_name = user_name 
    user_cnic = user_cnic
    mobile_num = mobile_num
    user_password = user_password
    with open (r"data_files\login_detail.txt","r") as login_file:
        login_data = login_file.readlines()
        match = False
        try: 
            for data in login_data:
                user_detail = data.strip().split(",")
                if user_detail[1] == user_cnic.strip():
                    match = True
        except Exception as e:
            st.markdown(
                            "<div class = 'error_popup'>{e}</p></div>"
                              ,unsafe_allow_html=True
                            )
        if match == False:
            with open (r"data_files\login_detail.txt","a") as append_data:
                append_data.write(f"\n{user_name},{user_cnic},{user_password},{mobile_num}")
                append_data.close()
                Reg_msg(mobile_num , user_name )
            with open (r"data_files\wallet.txt","a") as wallet_file:
                wallet_balance = "$0.00"
                wallet_file.write(f"\n{user_cnic},{wallet_balance},{mobile_num}")
        else :
            st.markdown(
                            "<div class = 'error_popup'><p>An account already exists for this CNIC.</p></div>"
                              ,unsafe_allow_html=True
                            )
    login_file.close()
    st.success(" 🎊 Awesome! Your account and wallet have been successfully created.")
    
    




st.image("data_files/logo.png", width=50)
st.title("Join Us")
col_1, col_2 = st.columns(2)
with col_1:
    user_name  = st.text_input("Enter your Name")
    mobile_num = st.text_input("Enter your Number")
with col_2:
    user_cnic = st.text_input("Enter your Cnic")
    user_password = st.text_input("Enter your Password")

if st.button("Sign Up"):
    Reg(user_name,user_cnic, mobile_num,user_password)
    switch_page("app")



