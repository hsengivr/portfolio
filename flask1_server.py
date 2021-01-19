from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)

# http://127.0.0.1:5000/vicky
# http://127.0.0.1:5000/vic

# variable rules
# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index1.html',name=username)

@app.route('/')
def hello_():
    return render_template('index.html')

# dynamic changing of adding pages automatically according to page name
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open('database.csv','a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',')
        csv_writer.writerow([email,subject,message])


# POST  - me sending data to server once submitted 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict() 
            # print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Failed writing to database'
    else:
        return 'OOps something went wrong'