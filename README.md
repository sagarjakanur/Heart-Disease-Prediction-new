## Heart Disease Prediction System

### Overview

This project is a web-based application that predicts whether a person is at risk of heart disease using machine learning techniques. The system takes user inputs such as age, gender, blood pressure, cholesterol level, and other medical parameters, and provides a prediction result.

The machine learning model is built using Scikit-learn and integrated into a Flask web application, allowing users to interact with the model through a simple and user-friendly interface.

---

### Motivation

During my learning in Machine Learning and Data Science, I understood that building a model is only one part of the process. Making the model accessible to users is equally important.

This project focuses on building a complete end-to-end system, including:

* Data processing
* Model training
* Web application development
* User interaction

This helps in understanding how machine learning solutions are deployed in real-world applications.

---

### Technical Aspects

This project is divided into two main parts:

1. **Model Development**

   * Data preprocessing and cleaning
   * Feature selection
   * Training the model using Scikit-learn
   * Evaluating model performance

2. **Web Application**

   * Built using Flask
   * Takes user input through a web form
   * Sends input data to the trained model
   * Displays prediction results

---

### Project Structure

* `app.py` → Main Flask application that runs the web server
* `model.pkl` / `.sav` → Trained machine learning model
* `templates/` → HTML files for user interface
* `static/` → CSS files for styling
* `requirements.txt` → List of required Python libraries

---

### Installation

Make sure Python is installed (Python 3.8 or above recommended).

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

### How to Run

Clone the repository:

```bash
git clone https://github.com/sagarjakanur/Heart-Disease-Prediction-new.git
cd Heart-Disease-Prediction-new
```

Run the application:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

### Technologies Used

* Python
* Flask
* Scikit-learn
* HTML
* CSS

---

### Future Improvements

* Improve model accuracy using advanced algorithms
* Add better user interface design
* Include graphical representation of results
* Deploy the application on cloud platforms

---

### Credits

This project is developed for learning and academic purposes.
Some design and structural ideas are inspired by open-source machine learning deployment projects, and have been modified and customized.
