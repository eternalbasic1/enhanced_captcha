from flask import Flask, render_template, request, session, redirect, url_for, flash
import random
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Setup rate limiter: Limit to 5 submissions per minute per IP
limiter = Limiter(app=app, key_func=get_remote_address)

def generate_captcha(difficulty=1):
    """
    Generate a simple math CAPTCHA based on difficulty level.
    Level 1: Addition of two numbers.
    Level 2: Addition of three numbers.
    Level 3: Multiplication of two numbers.
    """
    if difficulty == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        question = f"What is {a} + {b}?"
        answer = a + b
    elif difficulty == 2:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        question = f"What is {a} + {b} + {c}?"
        answer = a + b + c
    else:  # difficulty level 3
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        question = f"What is {a} * {b}?"
        answer = a * b
    return question, answer

@app.route('/', methods=['GET'])
def index():
    # Start timer for behavioral monitoring
    session['start_time'] = time.time()
    # Set current captcha difficulty (default to 1)
    difficulty = session.get('captcha_difficulty', 1)
    question, answer = generate_captcha(difficulty)
    session['captcha_answer'] = answer
    return render_template('index.html', captcha_question=question)

@app.route('/validate', methods=['POST'])
@limiter.limit("5 per minute")
def validate():
    # Calculate time taken to complete the captcha
    start_time = session.get('start_time', time.time())
    time_taken = time.time() - start_time

    # Retrieve user input and correct answer
    user_answer = request.form.get('captcha_answer')
    correct_answer = session.get('captcha_answer')

    # Behavioral check: If form is submitted too quickly, assume suspicious activity.
    if time_taken < 3:
        flash("Suspicious activity detected. CAPTCHA difficulty increased.", "error")
        # Increase difficulty (up to level 3)
        session['captcha_difficulty'] = min(session.get('captcha_difficulty', 1) + 1, 3)
        return redirect(url_for('index'))

    try:
        if int(user_answer) == correct_answer:
            flash("CAPTCHA passed! You are human.", "success")
            # Reset difficulty after a correct response
            session['captcha_difficulty'] = 1
        else:
            flash("Incorrect CAPTCHA. Please try again.", "error")
    except ValueError:
        flash("Invalid input. Please enter a number.", "error")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
