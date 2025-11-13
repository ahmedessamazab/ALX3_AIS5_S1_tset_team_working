import streamlit as st

# Set page title
st.set_page_config(page_title="My Projects Dashboard", layout="wide")

# Main title
st.title("🚀 My Projects Dashboard")

# Create three tabs
tab1, tab2, tab3 = st.tabs(["📊 Project 1: Data Analysis", "🤖 Project 2: Machine Learning", "🌐 Project 3: Web App"])

# ---------------- TAB 1 ----------------
with tab1:
    st.header("📊 Data Analysis Project Ahmed Azab")
    st.write("This tab contains details and visualizations for your data analysis project.")
    
    # Example content
    st.subheader("Summary Statistics")
    st.write("Here you could show summary statistics, charts, etc.")
    uploaded_file = st.file_uploader("Upload a CSV file for analysis", type="csv")

    if uploaded_file is not None:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        st.write("Basic statistics:")
        st.write(df.describe())

# ---------------- TAB 2 ----------------
with tab2:
    st.header("🤖 Machine Learning Project")
    st.write("This tab can be used for your ML model demo or results.")

    # Example content
    st.subheader("Model Performance")
    accuracy = 0.92
    st.metric(label="Model Accuracy", value=f"{accuracy*100:.1f}%")

    st.write("Visualize model performance metrics here (e.g., confusion matrix, ROC curve).")

# ---------------- TAB 3 ----------------
with tab3:
    st.header("🌐 Web App Project")
    st.write("This tab could display a small web app or UI prototype.")
    
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to the Web App Project.")

    st.button("Click Me!")

