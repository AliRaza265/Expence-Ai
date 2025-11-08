import streamlit as st
from PIL import Image, UnidentifiedImageError
import cv2 as cv
import pandas as pd
import pytesseract as pts
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
st.set_page_config(page_title="Fraud-Detection",page_icon="data_files/page_icon.png",layout="centered")
st.markdown(
"""<style>
body {
   background: radial-gradient(circle at 20% 20%, #00f2fe, #0052cc 70%) fixed !important;
    width: 100%;
    height: 100%;
    font-family: 'Poppins', sans-serif;
}
.st-emotion-cache-1r4qj8v,.st-emotion-cache-1wrcr25 {
background: none !important;
overflow: auto;
}

.st-emotion-cache-zt5igj{
     left: 0; 
     width: 100% ;
}
.st-emotion-cache-10trblm{
   margin-left: 0;
}
header{
    display: none !important;
}
 .st-emotion-cache-1y4p8pa {
    max-width: 650px;
    width: 100%;
    animation: floatUp 1.5s ease-out;
    padding: 0rem 1rem 0rem;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .st-emotion-cache-0 ,.st-emotion-cache-1gulkj5,.st-emotion-cache-fis6aj{
    backdrop-filter: blur(20px) saturate(120%);
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 0 40px 30px 40px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    transform-style: preserve-3d;
    transition: transform 0.3s, box-shadow 0.3s;
  }
.st-emotion-cache-1gulkj5,.st-emotion-cache-fis6aj{
    padding: 1rem !important;
        border-radius: 10px;
}
.st-emotion-cache-7ym5gk:hover {
   background: #4083e7;
    color: white;
    border: none;
}
.st-emotion-cache-fis6aj{
    margin-top: 11px;
    padding: 5px 12px !important;
}
.st-emotion-cache-12xsiil{
margin-bottom: 0;
}
button:not(:disabled){
color: gray;
}
.st-emotion-cache-6rlrad,.st-emotion-cache-1aehpvj,.st-emotion-cache-1fttcpj,.st-emotion-cache-4mjat2,.uploadedFileName,.st-emotion-cache-1pbsqtx  {
    color: white !important;
    fill: white;
    }
    #wallet,#welcome-back,#join-us,#fruad-detection {
    color: #fff;
    text-align: center;
    margin-bottom: 10px;
    font-size: 2.2rem;
    font-weight: 600;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
    .st-emotion-cache-6awftf,.st-emotion-cache-eczf16,.st-emotion-cache-vk3wp9  {
    display: none;
    }
  .st-emotion-cache-0:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.2);
  }
.st-emotion-cache-l9bjmx p{
    color: white !important;
    font-size: 15px;
}
.st-emotion-cache-1v0mbdj  {
    padding: 10px;
   background: radial-gradient(circle at 20% 20%, #00f2fea1, #0052cc61 70%) fixed !important; 
    border-radius: 50%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}
.st-emotion-cache-1vucj53:nth-of-type(2) .st-emotion-cache-9aoz2h {
    position: absolute;
    top: -50px;
    right: -50%;
    align-items: center;
    transform: translate(-5%, -0%);
}
th ,td{
    color: white !important;
}
  
</style>"""
    ,unsafe_allow_html=True
) 
def frud_detect(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    _,thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
    Array = Image.fromarray(thresh)
    text = pts.image_to_string(Array)
    print(text)
    table_placeholder = st.empty()
    colmns = pd.DataFrame({
            "Product": pd.Series(dtype="str"),
            "Price": pd.Series(dtype="int"),
            "App-Price": pd.Series(dtype="int"),
            "Fruad %": pd.Series(dtype="float")
})
    table_placeholder.table(colmns)
    try:
        fruad_level = []
        for line in text.splitlines():
            if "pkr" in line.lower() and not "total" in line.lower() and not "gross total" in line.lower() and not "tax" in line.lower() and not "net total" in line.lower() and not "cash given" in line.lower()and not "change" in line.lower():
                product = line.split("PKR")
                product_name = product[0]
                product_price = int(product[1])
                url = f"https://www.naheed.pk/catalogsearch/result/?q={product_name.lower()}"
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2) 
                element = driver.find_element(By.CLASS_NAME,"after_special")
                app_price = int(element.text.replace("Rs."," ").strip())
                driver.quit()
       
                if product_price == app_price:
                    st.write(f"The price you entered and retrieved from the app is the same. Rs {app_price}")
                elif product_price > app_price:
                    price_persent = ((product_price - app_price) / app_price) * 100
                    print(f"The price you provided is over {price_persent:.2f}% higher than the app price Rs. {app_price}.")
                    fruad_level.append(f"{price_persent}")

                elif product_price < app_price:
                    price_persent = ((app_price - product_price) / app_price) * 100
                    print(f"The price you provided is over {price_persent:.2f}% Lower than the app price Rs. {app_price}.")
                    fruad_level.append(f"0")
                new_row = pd.DataFrame(
                    [[product_name, np.int32(product_price), np.int32(app_price),round(float(fruad_level[-1]), 2)]],
                    columns=["Product", "Price", "App-Price","Fruad %"]
                )

                colmns = pd.concat([colmns, new_row], ignore_index=True)
                table_placeholder.table(colmns)
        st.warning("📝 Note: This result is based on live website data and may not always be correct.")

    except Exception as e:
                print(e)
                st.error("The website is taking longer than expected to respond.", icon="🚨")


st.image("data_files/logo.png", width=50)
st.title("Fruad Detection")

file = st.file_uploader(
    "Upload an image",
    accept_multiple_files=False,
    type=["jpg", "png", "jpeg"]
)

if file is not None:
    image = Image.open(file)     
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    frud_detect(image)