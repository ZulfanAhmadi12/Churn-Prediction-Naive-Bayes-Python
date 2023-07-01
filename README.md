## About This Project

Project Description: Predicting Customer Churn using Naive Bayes Algorithm with Class Imbalance Handling

In this project, we aim to develop a predictive model to determine whether a customer is likely to churn or not in a given bank. Churn refers to the phenomenon where customers stop using the services of a company. Identifying potential churners can help businesses take proactive measures to retain customers and reduce customer attrition.

One challenge we need to address is the class imbalance problem. Class imbalance occurs when the distribution of the target variable is significantly skewed, with one class being dominant compared to the other. In our case, the churned customers may be a minority class compared to the non-churned customers.

To handle the class imbalance problem, we will utilize undersampling or oversampling methods. Undersampling involves randomly removing samples from the majority class to achieve a balanced class distribution. Oversampling, on the other hand, involves creating synthetic samples for the minority class to balance the class distribution.

We will apply these techniques using libraries such as imbalanced-learn in Python. By balancing the class distribution, we ensure that the Naive Bayes algorithm receives sufficient training data for both classes, leading to better predictive performance.

In addition to class imbalance handling, we will employ the Naive Bayes algorithm, a popular machine learning algorithm known for its simplicity and effectiveness in classification tasks. Naive Bayes assumes independence among features and calculates the probability of each class given the feature values.

The dataset includes various features such as CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, and Exited. These features provide valuable insights into customer behavior and characteristics, which will be used to train the Naive Bayes classifier.

To build the user interface, we will utilize the Flask framework in Python. Flask is a lightweight web framework that allows us to create web applications easily. We will design a form where users can input the necessary information for making predictions. This information will be passed to the Naive Bayes model, which will predict whether the customer is likely to churn or not.

The Flask application will handle the request, process the form data, and make predictions using the trained model. The prediction result will be displayed on the user interface, indicating whether the customer is likely to churn or not.

By combining the power of the Naive Bayes algorithm, class imbalance handling techniques, and the user-friendly interface provided by Flask, we aim to develop a practical solution for predicting customer churn. This project has the potential to assist businesses in proactively managing customer retention strategies and improving overall customer satisfaction.

Note: It is important to preprocess and analyze the dataset, split it into training and testing sets, and perform feature engineering before handling class imbalance and training the Naive Bayes model. Additionally, model evaluation and performance metrics should be considered to assess the accuracy and reliability of the predictions.

<img src="https://github.com/ZulfanAhmadi12/MyPortfolio/blob/main/public/backend/assets/images/logoportofolio.png" width="200" height="100">

## Churn Prediction User Interfaces

<figure>
    <img src="https://github.com/ZulfanAhmadi12/MyPortfolio/blob/main/homefirst.png"
         alt="Home Top Page" width="600" height="300">
    <figcaption>Screenshot Home Page, at the top of the page.</figcaption>
</figure>



