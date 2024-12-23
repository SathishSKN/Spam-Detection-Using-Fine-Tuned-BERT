from flask import Flask, request, render_template
import tensorflow as tf
import tensorflow_text as text  # Ensures compatibility for the BERT model

app = Flask(__name__)

# Load the model once at the start
model = tf.keras.models.load_model("C://Users//sathi//Career//Internship//AFAME//Spam SMS Detection//BERT//saved_model//spam_detection_model")

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        message = request.form['message']
        prediction = model.predict([message])[0][0]  # Extract prediction value
        
        # Debugging output
        if prediction > 0.5:
            print("This has a high probability of being a spam message.")
            spam_status = 'Spam'
        else:
            print("This is not likely to be a spam message.")
            spam_status = 'Not Spam'
        
        return render_template('index.html', prediction=spam_status)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
