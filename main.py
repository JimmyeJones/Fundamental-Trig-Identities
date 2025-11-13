#Mattox J
#Jenkins - AM2
#A simple Streamlit app to calculate trigonometric functions based on user input.
#This site is accessible at: https://fundamental-trig-identities.streamlit.app/
#If prompted, click "Yes" to wake the site.
import math
import streamlit as st

def calc_trig_values(sin_value):
    sin = sin_value
    try:
        cos=math.sqrt(1-sin**2)
    except:
        cos=False
    try:
        tan=sin/cos
    except ZeroDivisionError:
        tan=False
    try:
        csc=1/sin
    except ZeroDivisionError:
        csc=False
    try:
        sec=1/cos
    except ZeroDivisionError:
        sec=False
    try:
        cot=cos/sin
    except ZeroDivisionError:
        cot=False
    values = [["sin(t)", sin], ["cos(t)", cos], ["tan(t)", tan], ["csc(t)", csc], ["sec(t)", sec], ["cot(t)", cot]]
    return values

st.title("Trigonometric Function Calculator")
st.text("Made by Mattox J")
page = st.selectbox("Select your input value", ["sin(t)=?", "cos(t)=?", "tan(t)=?"])
if page == "sin(t)=?":
    sin = st.text_input("Enter value")
    if sin:
        try:
            sin = float(sin)
        except:
            st.warning("Invalid input")
        else:
            if st.button("Calculate"):
                values = calc_trig_values(sin)
                for value in values:
                    if value[1] is not False:
                        st.info(f"{value[0]} = {round(value[1], 3)}")
                    else:
                        st.error(f"{value[0]} is undefined")
elif page == "cos(t)=?":
    cos = st.text_input("Enter value")
    if cos:
        try:
            cos = float(cos)
        except:
            st.warning("Invalid input")
        else:
            sin = math.sqrt(1-cos**2)
            if st.button("Calculate"):
                values = calc_trig_values(sin)
                for value in values:
                    if value[1] is not False:
                        st.info(f"{value[0]} = {round(value[1], 3)}")
                    else:
                        st.error(f"{value[0]} is undefined")
elif page == "tan(t)=?":
    tan = st.text_input("Enter value")
    if tan:
        try:
            tan = float(tan)
        except:
            st.warning("Invalid input")
        else:
            cos=math.sqrt((tan**2)+1)
            sin=tan/cos
            if st.button("Calculate"):
                values = calc_trig_values(sin)
                for value in values:
                    if value[1] is not False:
                        st.info(f"{value[0]} = {round(value[1], 3)}")
                    else:
                        st.error(f"{value[0]} is undefined")
