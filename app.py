import streamlit as st
import pickle

movies= pickle.load(open("movies_list.pkl","rb"))
similarity= pickle.load(open("similarity.pkl","rb"))
movies_titles = movies["title"].values
st.header("Movie Recommender System")
select_value=st.selectbox("Select movie from the dropdown",movies_titles)

def recommend_movie(movie):
   
    index = movies[movies["title"] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movies=[]
    for i in distance[1:6]:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

if st.button("Show Recommendation"):
    movie_re=recommend_movie(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_re[0])
    with col2:
        st.text(movie_re[1])
    with col3:
        st.text(movie_re[2])
    with col4:
        st.text(movie_re[3])
    with col5:
        st.text(movie_re[4])