# 🛍️ Product Recommendation System using Streamlit

A simple and interactive **Product Recommendation System** built using **Python**, **Streamlit**, **Pandas**, and **Scikit-learn**.

This app recommends products to users based on their historical ratings using **Collaborative Filtering** and shows product images in the UI.

---

## 📸 Demo

![App Screenshot](https://m.media-amazon.com/images/I/61LtuGzXeaL._SX679_.jpg)  
*(Sample product image; you can add a live GIF/demo later)*

---

## ✅ Features

- 🔽 User ID selection to fetch personalized recommendations  
- 🎯 Uses cosine similarity between users to find similar preferences  
- ✅ Excludes products already rated by the user  
- 🖼️ Displays product image thumbnails from URLs  
- 📊 Trending Products section for new users  

---

## 🧠 How It Works

- Reads `data.csv` containing user ratings and product info  
- Creates a pivot table (user vs products)  
- Calculates **cosine similarity** between users  
- Finds top similar users and their rated products  
- Filters out products the current user already rated  
- Displays top recommendations and product images  

---

## 🗂️ Folder Structure

🚀 How to Run Locally
🔧 Step 1: Clone the repo
bash
Copy
Edit
git clone https://github.com/kashishsharmae/recommendation-app.git
cd recommendation-app
📦 Step 2: Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or individually:

bash
Copy
Edit
pip install streamlit pandas scikit-learn
▶️ Step 3: Launch the app
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

☁️ Live App
Deployed on Streamlit Cloud 🚀
🔗 https://kashishsharmae-recommendation-app.streamlit.app

👨‍💻 Author
Kashish Sharma
🔗 GitHub: @kashishsharmae
🔗 LinkedIn: linkedin.com/in/kashishsharmae

