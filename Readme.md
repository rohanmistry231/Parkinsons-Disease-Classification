# Parkinson's Disease Classification

## 📌 Project Overview
This project focuses on classifying Parkinson's Disease using machine learning techniques. The dataset used contains various biomedical voice measurements, which help in distinguishing between healthy individuals and those with Parkinson's disease. The classification model is trained to predict the presence of the disease based on these features.

## 📂 Directory Structure
```
📦 Parkinsons Disease Classification
├── 📂 Pages
│   ├── Prediction.py  # Script for making predictions
├── venv/              # Virtual environment (if used)
├── .gitignore         # Git ignore file to exclude unnecessary files
├── Parkinsons Disease Knowledge.py  # Script containing domain knowledge
├── Parkinson disease.csv  # Dataset file
├── predictive system.py  # Main script for training and testing the model
├── Readme.md           # Documentation
├── trained_model.sav   # Saved trained model
```

## 📊 Dataset
The dataset used for this project includes various biomedical voice measurements such as:
- MDVP:Fo(Hz) - Fundamental frequency
- MDVP:Jitter(%) - Variation in frequency
- MDVP:Shimmer - Variation in amplitude
- HNR - Harmonics-to-noise ratio
- Various other frequency and amplitude-related parameters

**Target Variable:** `status` (1 = Parkinson's Disease, 0 = Healthy)

## 🚀 Installation and Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/rohanmistry231/Parkinsons-Disease-Classification.git
   cd Parkinsons-Disease-Classification
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🛠 How to Use
### Training the Model
Run the following command to train the model:
```sh
streamlit run Parkinsons Disease Knowledge.py
```
This script loads the dataset, trains the classification model, and saves the trained model as `trained_model.sav`.

### Making Predictions
Open the Streamlit web interface in your browser. Navigate to the prediction page where you can input the biomedical voice measurements to get the prediction results.

## 📈 Results and Performance
The model achieves high accuracy in distinguishing between healthy individuals and those with Parkinson’s disease. Performance metrics and results are analyzed in the `predictive system.py` script.

## 📚 References
- UCI Parkinson’s Disease Dataset: [Link to dataset]
- Research papers and domain knowledge related to Parkinson’s Disease

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, improve the model, and submit pull requests.