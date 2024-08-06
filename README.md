# Spam-Detection-Using-Fine-Tuned-BERT
Spam detection is a crucial task in natural language processing (NLP) aimed at identifying and filtering out unwanted or harmful messages, such as spam emails or SMS. Leveraging the power of BERT, a pre-trained transformer model developed by Google, we can significantly enhance the accuracy and efficiency of spam detection systems.
In this project, we fine-tune a BERT model specifically for the task of spam detection. The process involves the following steps:

Data Collection and Preprocessing: We gather a diverse dataset of emails and SMS messages, labeled as spam or ham (non-spam). The data is then cleaned and preprocessed to remove noise and irrelevant information.
Text Preprocessing with TensorFlow Hub: Instead of traditional tokenization, we utilize TensorFlow Hub’s BERT preprocessor and encoder. This approach simplifies the preprocessing pipeline by directly converting raw text into embeddings that the BERT model can understand.
Handling Imbalanced Data:
Original Data: We start by building the model with the original dataset.
Down Sampling: We reduce the number of ham messages to balance the dataset.
Up Sampling: We increase the number of spam messages to balance the dataset.
Class Weights: We assign different weights to classes to handle the imbalance.
Custom Loss Method: We implement a custom loss function to further address the imbalance between ham and spam.
Model Fine-Tuning: The pre-trained BERT model is fine-tuned on our spam detection dataset. This involves training the model on labeled data to adjust its weights and improve its ability to classify messages as spam or ham.
Evaluation and Optimization: We evaluate the performance of the fine-tuned BERT model using metrics such as accuracy, precision, recall, and F1 score. Hyperparameter tuning and optimization techniques are applied to enhance the model’s performance.
Model Comparison: We compare the results of models built with different data handling techniques and select the best-performing model based on the F1 score.
Deployment: The optimized model is deployed in a real-world environment, where it can process incoming messages and classify them as spam or ham in real-time.
By fine-tuning BERT for spam detection and leveraging TensorFlow Hub’s preprocessor and encoder, along with various techniques to handle imbalanced data, we achieve a high level of accuracy and robustness. This makes it an effective solution for filtering out unwanted messages and protecting users from potential threats.
