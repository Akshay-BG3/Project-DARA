# dara_app.py — Streamlit UI (No FastAPI)

import streamlit as st
import main

st.title("📊 Project DARA – Data Analysis & Reporting Assistant")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "xls", "json"])

if uploaded_file:
    try:
        df = main.read_dataset(uploaded_file)
        st.success("✅ File successfully loaded!")

        # Show data preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head())

        # Generate Summary
        st.subheader("📄 Data Summary")
        summary = main.summarize_data(df)
        st.text(summary)

        # Histogram Plot
        st.subheader("📊 Generate Histogram")
        selected_col = st.selectbox("Choose a column", df.columns)
        if st.button("Generate Histogram"):
            hist_base64 = main.get_histogram(df, selected_col)
            st.image(f"data:image/png;base64,{hist_base64}")

        # Scatter Plot
        st.subheader("🔁 Generate Scatter Plot")
        x_col = st.selectbox("X-axis", df.columns, key="x")
        y_col = st.selectbox("Y-axis", df.columns, key="y")
        if st.button("Generate Scatter"):
            scatter_base64 = main.get_scatter(df, x_col, y_col)
            st.image(f"data:image/png;base64,{scatter_base64}")

        # Train ML Model
        st.subheader("🤖 Train a Machine Learning Model")
        target_col = st.selectbox("Choose Target Column", df.columns, key="target")
        if st.button("Train Model"):
            result = main.train_and_serialize(df, target_col)
            st.success(f"✅ Model trained! Accuracy: {result['accuracy']:.2f}")
            st.text(result["report"])
            st.session_state.model_data = result

        # Prediction
        if "model_data" in st.session_state:
            st.subheader("🔮 Make Prediction")
            model_data = st.session_state.model_data
            input_data = {}
            for col in model_data["feature_columns"]:
                input_data[col] = st.text_input(f"{col}", key=f"input_{col}")

            if st.button("Predict"):
                try:
                    pred = main.make_prediction(
                        model_data["model_bytes"],
                        model_data["scaler_bytes"],
                        model_data["encoder_bytes"],
                        input_data
                    )
                    st.success(f"🎯 Prediction: {pred}")
                except Exception as e:
                    st.error(f"Prediction failed: {e}")

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
