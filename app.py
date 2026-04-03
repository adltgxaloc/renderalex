from flask import Flask
app=Flask(__name__)
@app.route("/")
def mi_incio():
  return ("esto es una prueba con reder  otra prueba")
