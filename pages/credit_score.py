import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,accuracy_score,precision_score,recall_score,r2_score,f1_score
from sklearn.metrics import precision_score
st.set_page_config(page_title="Wallet",page_icon="data_files/page_icon.png",layout="centered")
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
  .st-emotion-cache-vk3wp9,header{
  display: none !important;
  }
  #wallet,#welcome-back,#join-us,#credit-score {
    color: #fff;
    text-align: center;
    margin-bottom: 10px;
    font-size: 2.2rem;
    font-weight: 600;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .st-emotion-cache-7ym5gk,.btns button {
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
  .st-emotion-cache-7ym5gk:hover,.btns button:hover {
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
.st-emotion-cache-6kgcsu:nth-of-type(4) .st-c0,.st-emotion-cache-6kgcsu:nth-of-type(4) .st-c2,.st-emotion-cache-6kgcsu:nth-of-type(4) .st-c1,.st-emotion-cache-6kgcsu:nth-of-type(4) .st-bz{
 border:1px solid white !important;
}
.st-emotion-cache-3uj0rx a {
    color: rgb(16 62 104);
    }
.st-emotion-cache-1v0mbdj  {
    padding: 10px;
   background: radial-gradient(circle at 20% 20%, #00f2fea1, #0052cc61 70%) fixed !important; 
    border-radius: 50%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}
.st-emotion-cache-6kgcsu:nth-of-type(2) .st-emotion-cache-9aoz2h {
    position: absolute;
    top: -50px;
    right: -50%;
    align-items: center;
    transform: translate(-13%, -0%);
}
.st-emotion-cache-12rj9lz{
display: none;
}
.st-emotion-cache-10trblm{
    margin-left:  0 !important;
}
.st-emotion-cache-12rj9lz,.st-emotion-cache-1li7dat{
display: none;
}
.st-emotion-cache-y4bq5x{
    justify-content: center;
}
.st-emotion-cache-183lzff {
font-family: 'Poppins', sans-serif;
font-size: 18px;
color: white;
margin-top: 20px;
}
</style>
"""
, unsafe_allow_html=True)

def Credit_score(user_cnics):
        try:
            # filtering data with the help of pandas
            file = pd.read_csv(r"data_files\sample_data.csv")
            find_missing_data = file.isnull().sum()
            filtering_data = file.dropna(subset=["CNIC","Age","Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents","Credit Score"])
            # print(filtering_data)
            # using label encoder to encode the values
            encoder = LabelEncoder()
            file["Monthly Income"] = encoder.fit_transform(file["Monthly Income"])
            file["Property (sqft)"] = encoder.fit_transform(file["Property (sqft)"])
            file["Bank Balance"] = encoder.fit_transform(file["Bank Balance"])
            file["Loan Amount"] = encoder.fit_transform(file["Loan Amount"])
            file["Loan History"] = encoder.fit_transform(file["Loan History"])
            file["Defaulted Before"] = encoder.fit_transform(file["Defaulted Before"])
            file["Number of Dependents"] = encoder.fit_transform(file["Number of Dependents"])
            # print(file[["Bank Balance","Monthly Income","Property (sqft)","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]])
            # using standered scale for scale data
            scaler_object =  StandardScaler()
            data_scling = scaler_object.fit_transform(file[["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]])
            # print(data_scling)
            data_frame = pd.DataFrame(data_scling , columns=["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"])
            # print(data_frame)
            # using model selection for tes and train data
            X = data_frame[["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]]
            y = file["Credit Score"]
            y_truth = []
            y_binary = [1 if score >= 700 else 0 for score in y] 
            X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)
            # print(X_train)
            # print(X_test)
            # print(y_train)
            # print(y_test)
            # using linear regression  to prediction 
            model_object = LinearRegression()
            model_object.fit(X_train,y_train)
            result = model_object.predict(X)
            # print(result)
            # use matrix to checking compatability of the model 
            mae = mean_absolute_error(y,result)
            mse = mean_squared_error(y,result)
            rmse = np.sqrt(mse)
            result_binary = [1 if score >= 700 else 0 for score in result]
            print("mean_absolute_error : " , mae)
            print("mean_squared_error : " , mse)
            print("root_mean_squared_error : " , rmse)
            print("accuracy_score : " ,accuracy_score(y_binary,result_binary))
            print("precision_score : " , precision_score(y_binary,result_binary))
            print("f1_score : " , f1_score(y_binary,result_binary))
            print("recall_score: " , recall_score(y_binary,result_binary))
            print("r2_score : " , r2_score(y,result) )
            # get data from test_data_file 
            read_file = pd.read_csv(r"data_files\test_data.csv")
            for i in read_file["CNIC"]:
                 print(i)
                 if i == user_cnics:
                         print(i)
                         row = read_file.loc[read_file["CNIC"] == user_cnics]
                         st.text("Snapshot")
                         st.write(row[["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents" ]].reset_index(drop=True))

            # data_encoding 
            read_file["Monthly Income"] = encoder.fit_transform(read_file["Monthly Income"])
            read_file["Property (sqft)"] = encoder.fit_transform(read_file["Property (sqft)"])
            read_file["Bank Balance"] = encoder.fit_transform(read_file["Bank Balance"])
            read_file["Loan Amount"] = encoder.fit_transform(read_file["Loan Amount"])
            read_file["Loan History"] = encoder.fit_transform(read_file["Loan History"])
            read_file["Defaulted Before"] = encoder.fit_transform(read_file["Defaulted Before"])
            read_file["Number of Dependents"] = encoder.fit_transform(read_file["Number of Dependents"])
            # print(read_file[["CNIC","Monthly Income","Bank Balance","Property (sqft)","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]])
            # data scaling
            scling_data = scaler_object.fit_transform(read_file[["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]])
            test_data_frame = pd.DataFrame(scling_data , columns=["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"])
            test_data_frame["CNIC"] = read_file["CNIC"].values
            # print(test_data_frame)
            # get the values from data_file
            user_cnic = user_cnics
            chose_row =  read_file.loc[ read_file["CNIC"] == user_cnic].copy()
            # print(chose_row)
            values = chose_row[["Monthly Income","Property (sqft)","Bank Balance","Loan Amount","Loan History","Defaulted Before","Number of Dependents"]]
            predicted_score = model_object.predict(values)
            score = int(predicted_score[0])
           
            if score < 430:
                st.error(f"😞 Credit Score {predicted_score[0]:.2f}  (Poor)")

            elif 430 <= score < 730:
                st.warning(f"🙂 Credit Score {predicted_score[0]:.2f} (Average)")

            elif score >= 730:
                st.success(f"😄 Credit Score {predicted_score[0]:.2f} (Excellent)")
        except Exception as e:
                print(e)
                st.error(f"Error.{e}", icon="🚨")

st.image("data_files/logo.png", width=50)
st.title("Credit score")
user_cnic = st.text_input("Enter your Cnic")
if st.button("Enter"):
   Credit_score(user_cnic)







