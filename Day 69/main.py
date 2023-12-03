import requests
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    blog_data = response.json()
    return render_template("index.html", render_data=blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<num>")
def post(num):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    blog_data = response.json()
    post_to_show = blog_data[int(num) - 1]
    return render_template("post.html", render_data=post_to_show)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

if __name__=="__main__":
    app.run(debug=True)