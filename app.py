from flask import Flask
<<<<<<< HEAD
import windows
=======
import linux
>>>>>>> 52448b123e795643b0336caacfd93581d8f99d54

app = Flask(__name__)

@app.route("/")
def hello():
    return "updated Flask sample application on azure hghapp service updated verrsion-4"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
