import flask


app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.secret_key="bharath"

@app.route('/display',methods=["GET"])
def index_fun():
    flask.flash("whats your name ?")
    return flask.render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flask.flash("Hi "+str(flask.request.form['name_input'])+", Great to see you!")
    return  flask.render_template("index.html")

app.run(host="0.0.0.0")
