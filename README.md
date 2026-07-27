🏠 House Price Prediction


A Machine Learning web application that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, furnishing status, parking availability, and other amenities.

This project is developed using Python, Scikit-Learn, and Streamlit. A Linear Regression model was trained and deployed to estimate house prices through an interactive web interface.

📌 Features


Predicts house prices in real time
Interactive Streamlit web application
Built using Linear Regression
Supports 13 input features
One-Hot Encoding for categorical variables
Responsive and user-friendly interface

🚀 Technologies Used

Python
NumPy
Pandas
Scikit-Learn
Streamlit
Pickle
📊 Dataset Features
The model uses the following input features:

Feature	Description
Area	House area (sq ft)
Bedrooms	Number of bedrooms
Bathrooms	Number of bathrooms
Stories	Number of floors
Main Road	Connected to the main road
Guest Room	Guest room availability
Basement	Basement availability
Hot Water Heating	Hot water heating system
Air Conditioning	Air conditioning availability
Parking	Number of parking spaces
Preferred Area	Located in a preferred area
Furnishing Status	Furnished / Semi-Furnished / Unfurnished
🤖 Machine Learning Model
Data Preprocessing
The following preprocessing steps were performed before training the model:

Removed duplicate records
Converted binary categorical features (Yes/No) into numerical values (1/0)
Applied One-Hot Encoding to the Furnishing Status feature
Split the dataset into training and testing sets
Trained multiple regression models for comparison
Models Evaluated
The following regression algorithms were trained and evaluated:

Linear Regression ✅
Ridge Regression
Decision Tree Regressor
Random Forest Regressor
XGBoost Regressor
Model Performance
Model	R² Score	MAE
Linear Regression	0.6529	970,043.40
Ridge Regression	0.6524	970,589.50
Random Forest Regressor	0.6092	1,028,272.98
XGBoost Regressor	0.6004	1,030,458.00
Decision Tree Regressor	0.5837	1,100,985.25
Final Model
Selected Algorithm: Linear Regression

Performance Metrics
R² Score: 0.6529
Mean Absolute Error (MAE): 970,043.40
Linear Regression achieved the highest R² Score and the lowest Mean Absolute Error (MAE) among all the evaluated models. Therefore, it was selected as the final model for deployment.

The trained model was saved using Pickle as:

house_price_model.pkl
and integrated into the Streamlit web application for real-time house price prediction.

📸 Application Preview
https://1drv.ms/i/c/0E06ABA45ED6FE7D/IQCcsfY8HfNqRbROTyoRojElAd6LhtUXkwJQ8l89qp669vU?e=8Ra3HX
👨‍💻 Author
Fasna Swafvan

⭐ Support
If you found this project useful, please consider giving it a ⭐ on GitHub.

About
A Machine Learning web application that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, furnishing status, parking availability, and other amenities.

housepriceprediction-paw2ucahykgs84zmaz2t4e.streamlit.app/
Resources
Readme
Activity
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Report repository
Releases
No releases published
Contributors
1
 (1)
@fasnasafwan28-cloud
fasnasafwan28-cloud
Languages
Jupyter Notebook
96.4%
Python
3.6%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Com
# House_loan_prediction
