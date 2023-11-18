# our first flask server
# following url contains information about the several routes that
# flask allows
# url: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)   # Creating an instance of a Flask application
print(__name__)     # Outputs: '__main__'

@app.route('/')
def my_home():
    return render_template("index.html")

# the funtion below helps to parameterize the name of the page
# so, instead of having an entry-function for each one, only one function is needed
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/index.html')
# def index():
#     return render_template("index.html")
#
# @app.route('/about.html')
# def about():
#     return render_template("about.html")
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
# @app.route('/works.html')
# def works():
#     return render_template("works.html")

def write_to_file(data):

    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            # write_to_file(data)
            write_to_csv(data)
            # return "Form submitted successfully"
            return redirect("thankyou.html")
        except:
            return "Did not save to database"
    else:
        return "Something went wrong. Try again!"