from app import app

@app.route("/")
def helloworld():
    return "Hello world!"





if __name__ == "__main__":
    app.run(debug=True)