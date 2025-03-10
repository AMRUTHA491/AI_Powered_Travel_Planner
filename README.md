# AI-Powered Travel Planner 🌍✈️

A **Smart Travel Assistant** powered by **Google Gemini API** and **Streamlit**.  
This tool helps users plan their trips effortlessly by providing **AI-generated travel options and estimated costs**. 

## 🚀 Features  
✅ **AI-Powered Travel Suggestions** – Get multiple travel options based on your source, destination, and budget.  
✅ **Price Range Slider** – Adjust your travel budget and get relevant travel options.  
✅ **Google Maps Integration** – Navigate to your destination with ease.  
✅ **Beginner-Friendly Interface** – Uses **Streamlit** for an easy-to-use, interactive experience.


## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/AI_Powered_Travel_Planner.git
cd AI_Powered_Travel_Planner
```  
### 2️⃣ Create a Virtual Environment (Optional but Recommended)  

#### ➤ **Run the following command to create a virtual environment:**  
```sh
python -m venv venv
```
### ➤ Activate the Virtual Environment  

#### 🖥️ **On macOS/Linux:**  
```sh
source venv/bin/activate
```
### ➤ Activate the Virtual Environment  

#### 🖥️ **On Windows:**  
```sh
venv\Scripts\activate
```
### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```
### 4️⃣ Set Up API Key  

#### ➤ **Create a `.env` file in the project folder**  
1. Inside your project directory, create a new file named `.env`.  
2. Open the `.env` file and add your **Google Gemini API Key** in the following format:  

```sh
GEMINI_API_KEY=your_api_key_here
```
5️⃣ **Add Your Image for Banner (Optional)**

If you want to use your custom image for the app's banner, follow these steps:

1. **Add the image to your project directory**  
   - Place your desired image (e.g., `travel.jpg`) inside the project folder.

2. **Update the path in the `set_background()` function**  
   - Open the `app.py` file.
   - Find the `set_background()` function.
   - Update the path to match the location of your image
     
## ▶️ Run the Application  

Run the following command to start the Streamlit app:  

```sh
streamlit run app.py
```
## 🛠 Technologies Used

- **Python** 🐍 – Core programming language
- **Google Gemini AI** 🤖 – AI model used for travel suggestions
- **Streamlit** 🎨 – Web framework for interactive UI
- **dotenv** 🛠 – For managing environment variables
- **langchain** 💬 – For handling prompts and model output

## 🏆 How It Works

1️⃣ **Enter** the source and destination locations.  
2️⃣ **Select** your travel mode, date, and budget.  
3️⃣ **Click** the "For details" button.  
4️⃣ The AI will **provide** you with travel options, estimated costs, and further steps. 

## 📜 License  

This project is **open-source**. Feel free to **use, modify, and contribute**! 🚀  
