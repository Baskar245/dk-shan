from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based diagnosis logic
def diagnose(symptoms):
    symptoms = symptoms.lower()
    if "fever" in symptoms and "cough" in symptoms:
        return "You might have the flu or a common cold."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "This could be a migraine."
    elif "stomach pain" in symptoms or "diarrhea" in symptoms:
        return "It might be a stomach infection."
    elif "chest pain" in symptoms:
        return "Chest pain could be serious. Please consult a doctor immediately."
    else:
        return "I'm not sure. Please consult a healthcare professional for an accurate diagnosis."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['symptoms']
    response = diagnose(user_input)
    return render_template('chat.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
