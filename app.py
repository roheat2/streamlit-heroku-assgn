import streamlit as st

st.title('Find whether the given number is odd or even.')
a=st.number_input("Enter a number")
if a%2==0:
	st.write('Given number is even')
else:
	st.write('Given number is odd')