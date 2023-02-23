#Core Pkg

import streamlit as st
import streamlit.components.v1 as stc

# Load EDA
import pandas as pd
import joblib

#load data
books_model = joblib.load("user_books.pkl")
Books_name = books_model.columns


def item_based_recommender(book_name, user_book_df=books_model):
    book_name = user_book_df[book_name]
    return user_book_df.corrwith(book_name).sort_values(ascending=False).head(10)

item_based_recommender("Jurassic Park")




def main():

    st.title("Book Recommendation App")

    menu = ["Home","Recommend", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice =="Home":
        st.subheader("Home")
        st.dataframe(Books_name)

    elif choice =="Recommend":
        st.subheader("Recommend Books")

        # search_term =st.text_input("Search")
        search_term = st.selectbox("Search", Books_name)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    result = item_based_recommender(search_term, user_book_df=books_model)
                except:
                    result = "Not Found"
                st.write(result)



    else:
        st.subheader("About")
        st.text("Built wit pandas & streamlit")






if __name__ == "__main__":
    main()



