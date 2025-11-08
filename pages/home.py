import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="Home",page_icon="data_files/page_icon.png",layout="centered")
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
  .st-emotion-cache-1ffuo7c ,header{
    display: none !important;
  }
 .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        color: white;
        padding: 25px 30px;
        font-size: 22px;
        font-weight: 600;
        z-index: 9999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    .nav-links a {
        color: #FFFFFF;
        text-decoration: none;
        margin-left: 20px;
        font-size: 18px;
        transition: color 0.3s;
    }

    .nav-links a:hover {
        color: #00BFFF;
    }
.st-emotion-cache-1w723zb{
     padding: 0px !important; 
     max-width: 100%;
}

  div[data-testid="element-container"]:nth-child(2) {
    top: 5px !important;
    z-index: 999999 !important;
    margin-left: 45px !important;
    width: 200px !important;
}
.st-emotion-cache-1kyxreq{
width: 200px !important;
}
.st-emotion-cache-1y4p8pa {
    padding: 0;
}
div[data-testid="stHorizontalBlock"] {
    padding: 45px 30px 0 ;
    gap: 2rem;
}

.st-emotion-cache-6awftf {
   display: none !important;
}
.content {
    padding-top: 90px;
    }
.st-emotion-cache-7czcpc{
      z-index: 99999;
      margin-left: 40px;
      margin-top: 4px;
    }
    .logo {
    margin-left: 66px;
    font-size: 24px;
}
 div[data-testid="stHorizontalBlock"] div[data-testid="stVerticalBlock"] {
    backdrop-filter: blur(20px) saturate(120%);
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 30px 0px 30px 30px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    transform-style: preserve-3d;
    transition: transform 0.3s, box-shadow 0.3s;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
  }
  div[data-testid="stHorizontalBlock"] div[data-testid="stVerticalBlock"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.2);
  }

 .st-emotion-cache-18kf3ut {
     padding: 50px 20px 0;
}
.st-emotion-cache-1n76uvr .st-emotion-cache-17ypgft:nth-child(2) {
    position: absolute;
    width: 100%;
    height: 100%;
}



div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:nth-of-type(2) button {
    background: none;
    border-radius: 10px;
    border: none;
}
div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:nth-of-type(2) button p {
    font-size: 26px;
    color: white;
    font-weight: 500;
}
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        text-align: center;
        padding: 16px 0;
        font-size: 18px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
    }
   
    .st-emotion-cache-1y4p8pa{
         max-width: 100%;
    }
    .content {
        padding-top: 100px;
        padding-bottom: 60px;
    }
   div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:nth-of-type(2) {
    position: absolute;
    align-items: center;
    top: 0 !important;
    margin-left: 0 !important;
    width: 100% !important;
    height: 100%;
}
div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:nth-of-type(2) .stButton,div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:nth-of-type(2) button {
    width: 100%;
    height: 100%;
}
.st-emotion-cache-vk3wp9 {
display: none;
}

</style>
"""
, unsafe_allow_html=True)


logo = st.image("data_files/logo.png", width=50)
st.markdown("""
    <div class="header">
        <div class="logo">Expence Ai</div>
        <div class="nav-links">
            <a href="pages/hello.py">Credit Score</a>
            <a href="#Fruad_Detection">Fruad Detection</a>            
            <a href="#Chatbot">Finance Advisor</a>
            <a href="#Wallet">E-wallet</a>
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2= st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.image("data_files/credits_score.PNG", width=100)
    if st.button("Credit Score", key="b1"):
        switch_page("credit_score")

with col2:
    st.image("data_files/fruad_detect.PNG", width=100)
    if st.button("Fruad Detection", key="b2"):
        switch_page("fruad")

with col3:
    st.image("data_files/wallet.PNG", width=100)
    if st.button("E-wallet", key="b3"):
        switch_page("wallet")

with col4:
    st.image("data_files/bot.PNG", width=100)
    if st.button("Finance Advisor", key="b4"):
        switch_page("wallet")



st.markdown("""
    <div class="footer">
        © 2025 My Wallet App — All Rights Reserved
    </div>
""", unsafe_allow_html=True)

