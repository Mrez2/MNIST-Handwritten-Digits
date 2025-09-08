import streamlit as st
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model

# Streamlit UI
st.title("🖊️ MNIST Digit Classifier")

# Dropdown to select digit
digit = st.selectbox("Choose a digit (0-9) to test:", list(range(10)))

# Button to run prediction
if st.button("Predict on sample"):
    # Load MNIST test data
    (_, _), (X_test, y_test) = mnist.load_data()
    X_test = X_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

    # Pick first sample of the selected digit
    idx = np.where(y_test == digit)[0][0]
    sample = X_test[idx].reshape(1, 28, 28, 1)

    # Load your trained model
    model = load_model("mnist_model.h5")

    # Predict
    pred = model.predict(sample)
    pred_digit = np.argmax(pred)

    st.write(f"✅ Model Prediction: {pred_digit}")
    st.image(sample.reshape(28,28), caption="Test Image", width=150)
