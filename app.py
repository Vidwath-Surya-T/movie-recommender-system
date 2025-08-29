import requests
import streamlit as st
import pickle
import pandas as pd
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies=movies_list['title'].values


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies:
        movie_id=i[0]
        #fetch poster from API
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
    "How would you like to be contacted?",
    movies,
)
st.write("You selected:", selected_movie_name)
if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for r in recommendations:
        st.write(r)
