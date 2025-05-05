from flask import Flask,render_template,request
import mysql.connector


# Configure Flask-Mail (Replace with your credentials)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'venkat2040gr@gmail.com'  # Your Gmail
# app.config['MAIL_PASSWORD'] = 'oipo nbgc hejs oiuq'    # Use App Password (not your Gmail password)
# app.config['MAIL_DEFAULT_SENDER'] = 'venkat2040gr@gmail.com'

# mail = Mail(app)

# @app.route('/send-message', methods=['POST'])
# def send_message():
#     data = request.form
#     name = data.get("name")
#     email = data.get("email")
#     message = data.get("message")

#     if not name or not email or not message:
#         return "Error : ALl fields are required"
#     # Send email to yourself
#     msg = Message(
#         subject=f"New Contact Form Submission from {name}",
#         sender=email,
#         recipients=['venkat2040gr@gmail.com'],  # Your email to receive messages
#         body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
#     )
#     mail.send(msg)

#     return jsonify({"success": "Message sent successfully!"})

# if __name__ == '__main__':
#     app.run(debug=True)



app=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2040",
    database="venkat"
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f"Name: {name}, Email: {email}, Message: {message}")
    
    # Ensure cursor is correctly created
    cursor = db.cursor()
    
    # Corrected SQL insert query
    query = "INSERT INTO venkat.portfolio_db(Name, Email, Message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))  # Pass correct data (name, email, message)
    
    db.commit()
    
    return render_template('index.html', response_msg="Message sent Successfully 👋")

    
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
