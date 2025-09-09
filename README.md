# 🖊️ MNIST Digit Classifier  

A deep learning project that classifies handwritten digits (0–9) using the **MNIST dataset**.  
Built with **TensorFlow/Keras** and deployed using **Streamlit** for an interactive web app.  

---

## 📌 Features  
- Train a Convolutional Neural Network (CNN) on the MNIST dataset  
- Save & load trained models (`.h5`)  
- Interactive web app with **Streamlit**  
- Choose digits and test real-time predictions  
- Visualization of training accuracy & loss  

---

## 🚀 Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Mrez2/mnist-handwritten-digits.git
   cd mnist-handwritten-digits
Install dependencies:

bash
Copy code
pip install -r requirements.txt
(Optional) Train the model in Jupyter Notebook and save it as:

bash
Copy code
model.save("mnist_model.h5")
▶️ Run the App
bash
Copy code
streamlit run app.py
Then open the local URL shown in the terminal (usually http://localhost:8501/).

📊 Example
Input: Handwritten digit (0–9)

Output: Predicted digit with confidence score

🛠️ Tech Stack
Python

TensorFlow / Keras

Streamlit

NumPy, Pandas, Matplotlib, Seaborn

📌 Future Improvements
Add option to draw digits on canvas in the app

Extend to Fashion-MNIST dataset

Deploy on Streamlit Cloud / Hugging Face Spaces
