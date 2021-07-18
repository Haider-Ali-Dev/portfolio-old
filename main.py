from flask import Flask, render_template, request, redirect
import csv
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)




def write_to_csv(data):
    with open('database.csv', 'a', newline='') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        w = csv.writer(f, delimiter=',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        w.writerow([email, subject, message])

# def reply_to_res(data):
#     resp = data['email']
#     subject = data['subject']
#     message = data['message']
#     email = EmailMessage()
#     email['from'] = 'haiderdev.com'
#     email['to'] = resp
#     email['subject'] = 'Thanks'
#     email.set_content('Test ETst')
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.ehlo()
#         server.starttls()
#         server.login('pythonandhaider@gmail.com', 'Haider123')
#         server.send_message(email)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            redirect('/thankyou.html')
        except:
            return 'Database Error!'
    else:
        return f"Error"
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')




