import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="login_page",page_icon="data_files/page_icon.png",layout="centered")
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
    max-width: 400px;
    width: 90%;
    animation: floatUp 1.5s ease-out;
    padding: 0rem 1rem 0rem;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .st-emotion-cache-0 {
    backdrop-filter: blur(20px) saturate(120%);
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 0 30px 30px 40px;
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
  .st-emotion-cache-0:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.2);
  }
  .st-emotion-cache-vk3wp9{
  display: none;
  }
  #welcome-back,#join-us {
    color: #fff;
    text-align: center;
    margin-bottom: 10px;
    font-size: 2.2rem;
    font-weight: 600;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .st-emotion-cache-7ym5gk  {
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
  .st-emotion-cache-17ypgft,.st-emotion-cache-pb6fr7,.row-widget {
    width: 100% !important;
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
  header{
        display: none !important;
  }
.Reg {
    display: flex;
    gap: 5px;
}
.st-cc {
    background-color: rgb(33 152 195 / 27%);
}
st-emotion-cache-4rsbii {
    width: 100%;
    overflow: hidden;
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
.st-c0, .st-c2, .st-c1, .st-bz{
 border:1px solid white !important;
}
.st-emotion-cache-eqffof a {
    color: rgb(16 62 104);
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
    transform: translate(-13%, -0%);
}
.st-emotion-cache-10trblm{
    margin-left:  0 !important;
}
.st-emotion-cache-12rj9lz,.st-emotion-cache-1li7dat{
display: none;
}
</style>
"""
, unsafe_allow_html=True)

def Login(user_cnic,passward):
   cnic = user_cnic
   with open (r"data_files\login_detail.txt","r") as login_file:
        login_data = login_file.readlines()
        try: 
            match = False
            for data in login_data:
                user_detail = data.strip().split(",")
                if user_detail[1] == cnic.strip():
                    match = True
                    password = passward
                    if user_detail[2] == password.strip():
                      st.success("✅ Login successful!")
                      time.sleep(2)
                      switch_page("home")              
                    else :
                            st.markdown(
                            "<div class = 'error_popup'><p>Oops! Wrong Password</p></div>"
                            ,unsafe_allow_html=True
                            )
            if match == False:
                            st.markdown(
                            "<div class = 'error_popup'><p>Oops! Wrong Cnic</p></div>"
                              ,unsafe_allow_html=True
                            )
        except Exception as e:
            print(e)



st.image("data_files/logo.png", width=50)
st.title("Welcome Back")
user_cnic = st.text_input("Enter your Cnic")
user_pass = st.text_input("Enter your Password")
if st.button("Login"):
    Login(user_cnic, user_pass)
st.markdown(
    "<div class = 'Reg'><p>Don’t have an account yet?</p><a href='pages\\Register.py' target='_blank' class='custom-link'>Register Now</a></div>",
    unsafe_allow_html=True
)






