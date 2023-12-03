from flask import Flask, render_template
import requests

# url = "https://api.npoint.io/c790b4d5cab58020d391"
# response = requests.get(url=url)
# data = response.json()

# title = data[0]["title"]

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    blog_data = response.json()
    return render_template("index.html", render_data=blog_data)

@app.route('/blogs/<num>')
def get_post(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    blog_data = response.json()
    post_to_show = blog_data[int(num)-1]
    return render_template("post.html", render_data=post_to_show)

if __name__ == "__main__":
    app.run(debug=True)
