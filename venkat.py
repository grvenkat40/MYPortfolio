from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail (Replace with your credentials)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'venkat2040gr@gmail.com'  # Your Gmail
app.config['MAIL_PASSWORD'] = 'oipo nbgc hejs oiuq'    # Use App Password (not your Gmail password)
app.config['MAIL_DEFAULT_SENDER'] = 'venkat2040gr@gmail.com'

mail = Mail(app)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return "Error : ALl fields are required"
    # Send email to yourself
    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        sender=email,
        recipients=['venkat2040gr@gmail.com'],  # Your email to receive messages
        body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
    )
    mail.send(msg)

    return jsonify({"success": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

