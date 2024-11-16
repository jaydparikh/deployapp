from flask import Flask
from markupsafe import escape
from flask import request, render_template

from models import Products
from database import session

app = Flask(__name__) 
#use the name of the current module as the argument to the Flask class

@app.route("/")
def homepage(): #called when root URL is accessed
#    return "<p> Hello, World! </p>"
    #add_Product()
    get_Product()
    return render_template("homepage.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def greet(name=None): 
    return render_template("greet.html", name=name)

# @app.route("/products/", methods=["GET", "POST"]) #methods is optional
# def products(): 
#     if request.method == "POST": 
#         return "You are using POST"
#     else:
#         return "<h> Product </h>"

@app.get("/products/") #separate routing for GET and POST
def products_get():
    products = get_Product()
    page = "<h1> Products Get</h1>"
    page += '<ul>'
    for product in products:
        page += f'<li>{product.name} </li>'
    page += '</ul>'
    return page

@app.post("/products/")
def products_post():
    return "<h> Product Post </h>"


@app.route("/products/<int:id>")
def product(id): 
#    return f"<h1> Product: #{escape(id)} </h1>" #escape is used to prevent attacks
    return render_template("products.html", productid=id)

@app.route("/users/<username>")
def user(username): 
    return f"<h1> Product: #{escape(username)} </h1>"

@app.get("/users/") # if you do not say .get assumed by default
def users_get(): 
    fname = request.args.get('fname')
    lname = request.args.get('lname', default="Doe")
    print(f"First Name: {fname}, Last Name: {lname}")
    print(request.args)
    return f"<h1> User: {fname} {lname} </h1>"

@app.post("/users/")
def users_post(): 
    firstname = request.form.get('fname')
    lastname = request.form.get('lname', default="Doe")
    return f"<h1> User: {firstname} {lastname} </h1>"

@app.route("/aboutus")
def aboutus(): 
    return "<h> About us </h>"

#app route to handle URL
@app.route("/aboutus/<path:subpath>")
def about(subpath): 
    return f"<h1> About: {escape(subpath)} </h1>"    


## <add text>
def add_Product():
    product = Products(name = "Products1", price = 20, quantity = 10)
    session.add(product)
    session.commit()

def get_Product():
    return session.query(Products).all()

##if __name__ == "__main__":
##    app.run(debug=True)