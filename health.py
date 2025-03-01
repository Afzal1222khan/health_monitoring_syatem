import streamlit as st
import pandas as pd
import random

# Function to generate patient data (same as in the notebook)
def generate_patient_data(n=10000):
    data = []
    for i in range(n):
        patient = {
            "patient_id": i+1,
            "age": random.randint(18, 90),
            "gender": random.choice(["Male", "Female"]),
            "bp": f"{random.randint(90, 160)}/{random.randint(60, 100)}",
            "sugar": random.randint(70, 180),
            "cholesterol": random.randint(125, 250),
            "haemoglobin": round(random.uniform(12, 18), 1),
            "bmi": round(random.uniform(18, 35), 1)
        }
        data.append(patient)
    
    return pd.DataFrame(data)

# Load data
df = generate_patient_data(10000)

# Streamlit components to display the data
st.title("Health Analysis Dashboard")
st.write("This dashboard shows various health statistics for a sample of 10,000 patients.")

# Show some data
st.subheader("Patient Data (First 10 Records)")
st.write(df.head(10))

# Show statistics
st.subheader("Health Statistics")
average_stats = {
    'Average Blood Pressure': df['bp'].mean(),
    'Average Sugar Level': df['sugar'].mean(),
    'Average Cholesterol Level': df['cholesterol'].mean(),
    'Average Hemoglobin Level': df['haemoglobin'].mean(),
}

for stat, value in average_stats.items():
    st.write(f"{stat}: {value:.2f}")

# You can add more features here such as filters, charts, etc.
