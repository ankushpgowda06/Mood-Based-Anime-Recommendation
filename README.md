# 🎭 Anime Mood-Based Clustering & Recommendation System

## 🎯 Project Overview  
This project aims to recommend anime based on a user’s **mood**, **age**, and **preferred format (movie or series)** using **Unsupervised Learning**. By combining anime metadata and synopsis information, we created a mood-based filtering system that clusters anime into **7 mood categories** using **K-Means**. The final model is deployed as a **Streamlit web app** and hosted on **Streamlit Cloud** for live usage.

🔴 **Live App**: [https://your-streamlit-app-url.streamlit.app](https://mood-based-anime-recommendation.streamlit.app/)  
📹 **Video Demo**: [https://drive.google.com/your-video-link](https://drive.google.com/file/d/1IgB3EO-7TxAcyJDHA7-Dw5VWIXEz0RId/view?usp=sharing)

---

## 📊 Dataset Overview  
Two datasets from **Kaggle** were used and merged based on `MAL_ID`:

- `anime.csv`: Contains anime metadata like `name`, `type`, `episodes`, `rating`, `genres`, etc.
- `anime_with_synopsis.csv`: Includes the `synopsis` for each anime.

---

## 🧹 Data Preprocessing  
- Merged datasets on `MAL_ID` to combine **genres** and **synopsis**.
- Cleaned missing values and removed redundant columns.
- Created a new text feature: `genre + synopsis`.
- Vectorized this text using **TF-IDF Vectorizer**.
- Plotted **Elbow Curve** to determine optimal `k` value for clustering.
- Used **K-Means Clustering** to create **7 mood-based clusters**.
- Manually mapped clusters to moods like Nostalgic, Weird Humor etc.
- Saved final dataset to CSV for app integration.

---

## 🧠 Modeling & Clustering
- **TF-IDF Vectorization** used for text-based feature transformation.
- **K-Means Clustering** (k=7) used for unsupervised mood grouping.
- Final cluster labels mapped to:
  - Nostalgic, Weird Humor
  - Emotional Rollercoaster
  - Curiosity, Suspense, Deep
  - Cool Characters with Edge
  - Adventurous, Unconventional Plots
  - Dark, Serious, Intense
  - Optimistic, Motivational
---

## 🎨 Streamlit App Features  
Interactive app allows users to:
- Select **Mood**
- Choose **Format** (Movie or Series)
- Enter **Age**
- Receive **Top 5 personalized anime recommendations**

---

## 🚀 Deployment
- 🗂️ Data: Preprocessed dataset stored as CSV
- 🖥️ App: Built with **Streamlit**
- ☁️ Hosting: Deployed on **Streamlit Cloud**

---

## 💡 Future Improvements  
- Add a user login system for personalized history
- Incorporate more moods using sentiment analysis
- Introduce collaborative filtering based on user ratings

---

**Built with love for Anime, Machine Learning, and Personalization!**
