# import packages
from flask import Flask  
  
# create the Flask class object 
app = Flask(__name__)   
 
# decorator define   
@app.route('/') 
def home():  
    return "Hello class, this is my first flask webpage.";  
  
if __name__ =='__main__':  
    app.run(host='127.0.0.1', port=5000, debug=True)
    #app.run(debug = True)  
    #app.run(host='0.0.0.0', port=6000)