import requests
import streamlit as st
import pickle
import pandas as pd


def fetch_posters(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en_US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse =True,key=lambda x:x[1])[1:6]
    
    
    recommended_movies=[]
    recommend_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_posters(movie_id))
    return recommended_movies,recommend_posters

movies_list= pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity= pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

movie_name = st.selectbox('?',movies['title'].values)
if st.button('Recommend'):
    recommendations,posters=recommend(movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])