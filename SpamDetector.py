import pickle
import streamlit as st


model=pickle.load(open("model.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))


def main():
    st.title("Email Spam Classification Apps")
    st.subheader("Build with Streamlit & Python")
    msg=st.text_input("Enter a Text: ")
    if st.button("Predict"):
        data=[msg]
        vect=cv.transform(data).toarray()
        prediction=model.predict(vect)
        result=prediction[1]
        if result==1:
            st.error("This is a spam mail")
        else:
            st.success("This is an ham mail")
    
    main()