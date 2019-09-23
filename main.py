from flask import Flask, render_template

site = Flask(__name__)

@site.route("/")
def home():
    return render_template("pages/main.html")


@site.route("/legal")
def legal():
    return render_template("pages/legal.html")
    
@site.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    site.run(debug=True)
