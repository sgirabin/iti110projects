import streamlit as st
import tensorflow as tf
import numpy as np
import os

# Load pre-trained models
MODEL_PATHS = {
    "CNN": "models/cnn_model.keras",
    "CNN + LSTM": "models/cnn_lstm_model.keras",
    "RNN + LSTM": "models/rnn_lstm_model.keras"
}

# Constants
VOCAB_SIZE=17093
MAX_SEQUENCE_LENGTH=744

# Vectorize Layer
vectorize_layer = tf.keras.layers.TextVectorization (
        max_tokens=vocab_size,
        output_mode="int",
        output_sequence_length=max_length
    )


# Load models
models = {}
for model_name, path in MODEL_PATHS.items():
    if os.path.exists(path):
        models[model_name] = tf.keras.models.load_model(path)
    else:
        st.error(f"Error loading {model_name} model. Check file paths.")

# Streamlit UI
def main():
    st.title("ITI110 Project - Spam Detection")
    
    # Model selection
    model_option = st.selectbox("Choose a model:", list(MODEL_PATHS.keys()))

    # Text input
    email_content = st.text_area("Paste email content here:")

    # Submit button
    if st.button("Submit"):
        if not email_content.strip():
            st.warning("Please enter some text before submitting.")
        else:
            prediction = predict_spam(email_content, model_option)
            st.subheader("Prediction Result:")
            st.write(f"The email is **{prediction}**")

# Prediction function
def predict_spam(text, model_name):
    # Preprocess text
    vectorize_layer.adapt(texts)
    vectorized_text = vectorize_layer(texts)
    
    # Get model prediction
    model = models[model_name]
    probability = model.predict(vectorized_text)[0][0]
    

    return "Spam" if probability > 0.5 else "Ham"

if __name__ == "__main__":
    main()
