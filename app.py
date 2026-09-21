import streamlit as st

st.set_page_config(page_title="EnvelopeCalcs", layout="wide")

st.title("Building Envelope Structural Calculations")
st.write("Welcome to EnvelopeCalcs facade engineering portal.")

# Sidebar Navigation
module = st.sidebar.selectbox(
    "Choose Calculation Module", 
    ["Glass Thickness & Deflection", "Structural Silicone Glazing (SSG) Bite", "Mullion Inertia (Ix)"]
)

if module == "Glass Thickness & Deflection":
    st.header("1. Glass Thickness & Deflection")
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("Glass Width (a) [mm]", value=1200.0)
        b = st.number_input("Glass Length (b) [mm]", value=2000.0)
        t = st.number_input("Glass Nominal Thickness (t) [mm]", value=10.0)
        q = st.number_input("Design Wind Load (q) [kPa]", value=1.5)
    
    with col2:
        E = 70000  # Modulus of Elasticity in MPa
        max_stress = (0.75 * q * (a**2)) / (t**2)
        
        st.subheader("Results")
        st.metric("Estimated Max Bending Stress", f"{max_stress:.2f} MPa")
        if max_stress < 80:
            st.success("Passes for Fully Tempered Glass (< 80 MPa)")
        else:
            st.error("Exceeds allowable stress for tempered glass")

elif module == "Structural Silicone Glazing (SSG) Bite":
    st.header("2. Structural Silicone Glazing (SSG) Bite")
    W = st.number_input("Short Side of Glass [mm]", value=1200.0)
    Pw = st.number_input("Wind Load [kPa]", value=2.0)
    sigma = st.number_input("Allowable Design Stress [MPa]", value=0.14)
    
    bite = (Pw * W) / (2 * sigma)
    st.subheader("Required Silicone Bite")
    st.metric("Minimum Bite Width (b)", f"{bite:.2f} mm")

elif module == "Mullion Inertia (Ix)":
    st.header("3. Aluminum Mullion Inertia Requirements")
    H = st.number_input("Mullion Span Height (H) [m]", value=3.5)
    W_trib = st.number_input("Tributary Width [m]", value=1.2)
    q = st.number_input("Wind Pressure [kPa]", value=1.5)
    
    w_line = q * W_trib  # kN/m
    st.metric("Line Load on Mullion", f"{w_line:.2f} kN/m")
