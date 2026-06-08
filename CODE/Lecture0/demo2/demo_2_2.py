# import packages
from flask import Flask  
  
# create the Flask class object 
app = Flask(__name__) 

# flask router default
@app.route("/home/<name>")
def home(name):
    if name is not None:
        return "My name is "+name+".";
    else:
        return "My name is Semmy.";
        
# flask router about    
@app.route("/about/<int:age>")
def about(age):
    return "My name is Semmy and I'm %d years old."%age;
    
# flask router project   
@app.route("/project")
def project():
    return "This is project :))"
    
if __name__ == "__main__":
    app.run(debug=True)