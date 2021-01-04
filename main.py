
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask, I am using virtual environment"


app.run()
