from flask import Flask, render_template
from app import app

@app.route("/")
def helloworld():
    return render_template('index.html')





if __name__ == "__main__":
    app.run()