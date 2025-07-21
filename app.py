import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    return df

df = load_data()

st.title("🛍️ Smart Product Recommendation System")

# Sidebar – Select User ID
user_ids = df['user_id'].unique().tolist()
selected_user = st.sidebar.selectbox("🔢 Select User ID", user_ids)

# Show dataset option
if st.checkbox("📊 Show Dataset"):
    st.dataframe(df)

# Show user’s past ratings
st.subheader(f"🧾 Past Ratings for User {selected_user}")
user_ratings = df[df['user_id'] == selected_user][['product_name', 'rating']]
st.table(user_ratings)

# Create Pivot Table
pivot = df.pivot_table(index='user_id', columns='product_name', values='rating').fillna(0)

# Calculate Similarity
similarity = cosine_similarity(pivot)

# Recommend Function
def recommend_products(user_id):
    if user_id not in pivot.index:
        return []

    sim_scores = list(enumerate(similarity[user_id - 1]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]
    similar_users = [i[0]+1 for i in sim_scores[:3]]

    recommended = []
    for user in similar_users:
        products = df[df['user_id'] == user][['product_name', 'image_url']].drop_duplicates().values.tolist()
        recommended.extend(products)

    already_rated = df[df['user_id'] == user_id]['product_name'].tolist()
    filtered = [item for item in recommended if item[0] not in already_rated]
    return list({(name, url) for name, url in filtered})  # remove duplicates

# Recommend Button
if st.button("🎯 Recommend Products"):
    recs = recommend_products(selected_user)
    if recs:
        st.subheader("✅ Recommended Products:")
        for name, img in recs:
            st.image(img, width=150, caption=name)
    else:
        st.warning("No recommendations found.")

# Handle Cold Start (New Users)
if df[df['user_id'] == selected_user].empty:
    st.info("👶 New user detected! Showing trending products:")
    trending = df.groupby('product_name')['rating'].mean().sort_values(ascending=False).head(3).index.tolist()
    for product in trending:
        img = df[df['product_name'] == product]['image_url'].values[0]
        st.image(img, width=150, caption=product)
