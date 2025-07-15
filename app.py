from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3



app=Flask(__name__)
app.secret_key = 'aS3cr3t!Key#789@dev'  # Good enough for local testing


def init_db():
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user(
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              User_Name TEXT NOT NULL,
              Mail TEXT NOT NULL,
              Message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/', methods=['GET', 'POST'])

def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"Name: {name}, Email: {email}, Message: {message}")
    
    # Ensure cursor is correctly created
        conn=sqlite3.connect('user.db')
        c=conn.cursor()
        c.execute("INSERT INTO user(User_Name,Mail,Message) VALUES (?,?,?)",(name,email,message))    

        c.execute("SELECT * FROM user")
        rows=c.fetchall()
        print("User table: ")
        for row in rows:
            print(row)

        conn.commit()
        conn.close()
        
        flash("Message sent Successfully 👋")
        return redirect(url_for('form'))  # Avoid duplicate form submissions
    
    return render_template('index.html')

    
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
