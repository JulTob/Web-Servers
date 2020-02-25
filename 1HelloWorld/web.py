from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to <h1>home</h1> page."

# passing variables
@app.route("/<MyName>")
def userpage(MyName):
    return f"Hello {MyName}!"


if __name__ =="__main__":
    app.run()
