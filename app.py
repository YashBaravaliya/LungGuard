from cnnClassifier.pipeline.prediction import PredictionPipeline
import streamlit as st
import os

def main():
    st.title("Lung Cancer Detection")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Make prediction
        pipeline = PredictionPipeline(uploaded_file)
        prediction = pipeline.predict()
        prdict = prediction[0]
        values = prdict['image']

        if values == 'Normal':
            st.success("No Lung Cancer Detected")
        else:
            st.error(f"Lung Cancer Detected {values}")

        # Display image
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

if __name__ == '__main__':
    main()
