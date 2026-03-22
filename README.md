#  End-to-End Machine Learning Project

This project is a complete machine learning pipeline that starts with raw data and ends with a trained model.


## 📥 Data Ingestion
The process begins by reading the dataset from a CSV file and splitting it into training and testing data.  
These files are then saved so they can be used in the next steps.


## 🔄 Data Transformation
Before training the model, the data is cleaned and prepared:
- Missing values are handled  
- Categorical features are converted into numbers  
- Numerical features are scaled  

All of this is done using pipelines so the same steps can be applied again later without repeating work.



## 🤖 Model Training
Multiple machine learning models are trained, including:
- Random Forest  
- Decision Tree  
- Gradient Boosting  
- Linear Regression  
- XGBoost  
- CatBoost  
- AdaBoost  

For each model, different parameters are tested using GridSearchCV to improve performance.


## 📊 Model Evaluation
After training, all models are evaluated using the R² score.  
The model with the best score is selected as the final model.



## 💾 Saving the Model
The final model and the preprocessing steps are saved so they can be used later to make predictions on new data.


## 📁 Project Structure
The project is divided into different parts like:
- Data Ingestion  
- Data Transformation  
- Model Training  

This makes the code easier to understand, reuse, and manage.