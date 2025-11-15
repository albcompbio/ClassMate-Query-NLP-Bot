import sqlite3
import spacy
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load the SpaCy language model
nlp = spacy.load('en_core_web_md')

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to find the most similar question from the database
def get_most_similar_question(input_question, stored_questions):
    input_doc = nlp(input_question.lower())
    max_similarity = 0
    most_similar_answer = None

    for question_row in stored_questions:
        stored_question = question_row['question'].lower()
        stored_answer = question_row['answer']
        stored_doc = nlp(stored_question)
        
        similarity = input_doc.similarity(stored_doc)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_answer = stored_answer

    return most_similar_answer

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the training page
@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO questions_answers (question, answer) VALUES (?, ?)", 
                    (question, answer))
        conn.commit()
        conn.close()
        
        flash('Bot trained successfully!', 'success')
        return redirect(url_for('train'))

    return render_template('train.html')

# Route for clearing all questions and answers
@app.route('/clear', methods=['POST'])
def clear():
    conn = get_db_connection()
    conn.execute('DELETE FROM questions_answers')
    conn.commit()
    conn.close()
    flash('All questions and answers have been cleared!', 'success')
    return redirect(url_for('train'))

# Route for the chatbot interface
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    messages = []
    if request.method == 'POST':
        input_question = request.form['question']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT question, answer FROM questions_answers")
        stored_questions = cur.fetchall()
        
        most_similar_answer = get_most_similar_question(input_question, stored_questions)

        # Append user message
        messages.append({'type': 'user', 'text': input_question, 'avatar': 'user.png'})

        # Append bot response based on similarity
        if most_similar_answer:
            messages.append({'type': 'bot', 'text': most_similar_answer, 'avatar': 'avatar.gif'})
        else:
            messages.append({'type': 'bot', 'text': "I'm sorry, I didn't understand that.", 'avatar': 'avatar.gif'})
        
        return render_template('chatbot.html', messages=messages)

    return render_template('chatbot.html', messages=messages)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
