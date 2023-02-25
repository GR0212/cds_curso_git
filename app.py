
import streamlit as st

def main():
    df = load_data()

    st.dataframe(df)

if __name__=='__main__':
    main()
