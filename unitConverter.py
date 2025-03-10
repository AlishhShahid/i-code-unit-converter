import streamlit as st

def convert_units(value, from_unit, to_unit):

    conversion = {
        "meters_kilometers" : 0.001, # 1m = 0.001km
        "kilometers_meters" : 1000,  # 1km = 1000m
        "meters_centimeters" : 100,  # 1m = 100cm
        "centimeters_meters" : 0.01,   # 1cm = 0.01m
        "grams_kilograms" : 0.001, # 1g = 0.001kg
        "kilograms_grams" : 1000,  # 1kg = 1000g
    }

    key = f"{from_unit}_{to_unit}" 

    if key in conversion:
        converter = conversion[key]
        return value * converter
    else:
        return "Conversion not support"
    
        
st.title("Unit Converter")
value = st.number_input("Enter the value: ")
from_unit = st.selectbox("Convert from: ", ["meters", "kilometers", "grams", "kilograms", "centimeters"])
to_unit = st.selectbox("Convert to: ", ["meters", "kilometers", "grams", "kilograms", "centimeters"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"Converted Value: {result}")
   