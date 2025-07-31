# SpamDetection_Using_MachineLearning

Spam Detection API
This project provides a simple REST API to detect spam messages using a machine learning model (Naive Bayes) trained on email data. The backend is built with Flask and uses scikit-learn for natural language processing and classification.

Features
REST API endpoint for spam message prediction
Trained on labeled email messages
Uses CountVectorizer and Multinomial Naive Bayes
Simple and easy to extend

Requirements
Python 3.7+
Flask
pandas
scikit-learn.
<p align ="centre">
<img src  ="data/WhatsApp Image 2025-07-31 at 12.00.33_577cb507.jpg" width = "200" height = "200" alt="logo">
</p>

 To Send API Reqest Follow These Steps - 
 -
1.U need To download following things in you python in order to run this code - 
```shell
pip install flask pandas scikit-learn

```
2.Set the PATH of csv File of Spam/NotSpam Emails - 
-
```shell
emails.csv

```
    
3.After Running the Code U might see this Interface -
-

<p align ="centre">
<img src  ="data/Screenshot 2025-07-31 104111.png" width = "700" height = "400" alt="logo">
</p>

4.Now You can create a POST method to Send Your Request -
-
```
http://192.168.1.6:8080/predict

```
5.Send a POST request to /predict with a JSON body:
-
```
{
  "message": "Congratulations! You've won a lottery. Claim now."
}
```
6.On Testing On POSTMAN you can see the result - 
<p align ="centre">
<img src  ="data/Screenshot 2025-07-31 115018.png" width = "700" height = "400" alt="logo">
</p>

