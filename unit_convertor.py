import streamlit as st

def main():
    st.title("Unit Converter")
    st.write("A simple application to convert between different units")

    # Select conversion category
    category = st.selectbox(
        "Select Category",
        ["Length", "Weight/Mass", "Temperature", "Area", "Volume", "Speed", "Time"]
    )

    # Define conversion units and factors based on category
    if category == "Length":
        units = {
            "Meter": 1.0,
            "Kilometer": 0.001,
            "Centimeter": 100.0,
            "Millimeter": 1000.0,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        }
        base_unit = "Meter"
    
    elif category == "Weight/Mass":
        units = {
            "Kilogram": 1.0,
            "Gram": 1000.0,
            "Milligram": 1000000.0,
            "Metric Ton": 0.001,
            "Pound": 2.20462,
            "Ounce": 35.274,
            "Stone": 0.157473
        }
        base_unit = "Kilogram"
    
    elif category == "Temperature":
        units = {
            "Celsius": "°C",
            "Fahrenheit": "°F",
            "Kelvin": "K"
        }
        base_unit = "Celsius"
    
    elif category == "Area":
        units = {
            "Square Meter": 1.0,
            "Square Kilometer": 0.000001,
            "Square Centimeter": 10000.0,
            "Square Millimeter": 1000000.0,
            "Square Mile": 3.861e-7,
            "Square Yard": 1.19599,
            "Square Foot": 10.7639,
            "Square Inch": 1550.0,
            "Acre": 0.000247105,
            "Hectare": 0.0001
        }
        base_unit = "Square Meter"
    
    elif category == "Volume":
        units = {
            "Cubic Meter": 1.0,
            "Cubic Centimeter": 1000000.0,
            "Liter": 1000.0,
            "Milliliter": 1000000.0,
            "Gallon (US)": 264.172,
            "Quart (US)": 1056.69,
            "Pint (US)": 2113.38,
            "Cup (US)": 4226.75,
            "Fluid Ounce (US)": 33814.0,
            "Cubic Inch": 61023.7,
            "Cubic Foot": 35.3147
        }
        base_unit = "Cubic Meter"
    
    elif category == "Speed":
        units = {
            "Meter per second": 1.0,
            "Kilometer per hour": 3.6,
            "Mile per hour": 2.23694,
            "Foot per second": 3.28084,
            "Knot": 1.94384
        }
        base_unit = "Meter per second"
    
    elif category == "Time":
        units = {
            "Second": 1.0,
            "Millisecond": 1000.0,
            "Microsecond": 1000000.0,
            "Minute": 1/60,
            "Hour": 1/3600,
            "Day": 1/86400,
            "Week": 1/604800,
            "Month (30 days)": 1/2592000,
            "Year (365 days)": 1/31536000
        }
        base_unit = "Second"

    # Create two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("From")
        from_unit = st.selectbox("Convert from", list(units.keys()), key="from")
        input_value = st.number_input("Enter value", value=1.0, step=0.1, format="%.3f")
    
    with col2:
        st.subheader("To")
        to_unit = st.selectbox("Convert to", list(units.keys()), key="to")
    
    # Conversion logic
    if st.button("Convert"):
        if category == "Temperature":
            result = convert_temperature(input_value, from_unit, to_unit)
            st.success(f"{input_value:.3f} {from_unit} = {result:.3f} {to_unit}")
        else:
            # For other categories using conversion factors
            if from_unit == to_unit:
                result = input_value
            else:
                # Convert to base unit first, then to target unit
                to_base = input_value / units[from_unit] if from_unit != base_unit else input_value
                result = to_base * units[to_unit] if to_unit != base_unit else to_base
            
            st.success(f"{input_value:.3f} {from_unit} = {result:.3f} {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    """Special handling for temperature conversions"""
    # Convert to Celsius first (as base)
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    
    # Convert from Celsius to target
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15

if __name__ == "__main__":
    main()
