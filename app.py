from flask import Flask, render_template, request, redirect
import pandas as pd
import pickle
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')


model = pickle.load(open('model.pkl','rb'))


df = pd.read_csv('student_mental_health_burnout.csv')
df = df.select_dtypes(include=['int64','float64'])
columns = list(df.columns[:-1])


def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS data(
        input TEXT,
        result TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
    user = cur.fetchone()

    conn.close()

    if user:
        return redirect('/home')
    else:
        return "Invalid Login"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users VALUES (?,?)", (username,password))

    conn.commit()
    conn.close()

    return "Registered Successfully"



@app.route('/home')
def home():
    return render_template('index.html', columns=columns)



@app.route('/predict', methods=['POST'])
def predict():
    values = [float(request.form[col]) for col in columns]

    result = model.predict([values])[0]

    if result == 0:
        msg = "Low Stress 😊"
    elif result == 1:
        msg = "Medium Stress 😐"
    else:
        msg = "High Stress 🚨"

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO data VALUES (?,?)", (str(values), str(result)))

    conn.commit()
    conn.close()

    return render_template('result.html', result=msg)



@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT result, COUNT(*) FROM data GROUP BY result")
    data = cur.fetchall()

    conn.close()

    labels = [str(x[0]) for x in data]
    values = [x[1] for x in data]

    return render_template('dashboard.html', labels=labels, values=values)



if __name__ == '__main__':
    app.run(debug=True, port=5002)