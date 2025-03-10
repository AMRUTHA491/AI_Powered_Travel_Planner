import streamlit as st
import base64
from datetime import date
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# logic 1

from langchain_core.prompts import ChatPromptTemplate
template=ChatPromptTemplate(
    messages=[('system',"""You are an intelligent travel planner assistant. Your task is to generate a structured and well-organized itinerary.
    for every travel option(train,fight,cab,bus) give the travel time,details,operators,pros and cons."""),
              ('human',"i want to book tickets to travel from {source} to {destination} by {mode} in the range ₹{min_price} and ₹{max_price} on {selected_date}.give me details regarding other mode of travel as well.give next steps regarding my choosen travel mode")],
    partial_variables={"destination":"BLR"})


#logic 2

from langchain_google_genai import ChatGoogleGenerativeAI

model=ChatGoogleGenerativeAI(google_api_key=api_key,model='gemini-2.0-flash')


# logic 3

from langchain_core.output_parsers import StrOutputParser

output_parser=StrOutputParser()

#building chain

chain = template | model | output_parser

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        img_bytes = image_file.read()
        encoded_string = base64.b64encode(img_bytes).decode()

    banner_html = f"""
    <style>
    .top-banner {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: 100% 100%; /* Stretch to fill */
        background-position: top center;
        background-repeat: no-repeat;
        height: 200px;
        width: 100%;
        margin-bottom: 20px;
    }}
    </style>
    <div class="top-banner"></div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)

# Display the image banner first
set_background(r'C:\Users\user\Downloads\Datasets\Datasets\AI_Powered_Travel_Planner\travel.jpg')


# Display content after the image
st.markdown('## 🌍✈️ AI-Powered Smart Trip Planner')
st.write('Plan your trip effortlessly with AI-generated travel options and estimated costs!')
source = st.text_input('Source Location :', placeholder='Enter location where you want to start your journey.......')
destination = st.text_input('Destination Location :', placeholder='Enter location where you want to go.......')

min_date = date.today()
selected_date = st.date_input("Travel date:", date.today(), min_value=min_date)

options = ['Train', 'Bus', 'Flight', 'Cab']
mode = st.selectbox('Mode of Travel :', options, placeholder='Select mode of travel......')
min_price = 500
max_price = 50000  # Adjust as needed

# Create the price range slider
price_range = st.slider(
    "Select Price Range:",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),  # Initial range
    step=1,  # Adjust the step size as needed
    format="₹%d" # add the $ symbol
)
min_value,max_value=price_range
button = st.button('For details click here')

if button:

    st.markdown(
    """
    <div style="
        background-color:rgb(199, 249, 201); 
        padding: 10px; 
        border-radius: 10px; 
        text-align: left;
        color: #006400;
        font-size: 15px;">
        ✨ Best Travel Options and Estimated Costs:
    </div>
    """, 
    unsafe_allow_html=True
    )
    st.markdown('#### ✈️ Suggested Trip Insights Just for You!')

    input_={'source':source,'destination':destination,'mode':mode,'min_price':min_value,'max_price':max_value,'selected_date':selected_date}
    
    output=chain.invoke(input_)
    st.write(output)

    st.markdown('### 🗺️ Goople map to navigate from destination:')
    st.info("📍 Click the button below to open Google Maps and measure the distance between your desired destination and destination location, including nearby hotels, restaurants, and other points of interest.")  
    maps_url = "https://www.google.com/maps"
    st.link_button("Open Google Maps", maps_url)


