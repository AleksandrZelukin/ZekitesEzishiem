from flask import Flask, render_template, request, url_for, redirect
import dbMethods
app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/login',methods=["GET","POST"])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    userExists = dbMethods.checkIfUserExists(username, password)
    if userExists:
      return redirect(url_for('mainpage'))
    else:
      return render_template('login.html')
      
@app.route('/mainpage')
def mainpage():
  
  userid = request.args.get('id')
  if userid != None:
    dbMethods.deleteUser(userid)
    
  productid = request.args.get('productid')
  if productid != None:
    dbMethods.deleteProduct(productid)
    
  visiLietotaji = dbMethods.selectAllUsers()
  visiProdukti = dbMethods.selectAllProducts()
  return render_template('mainpage.html',p1=visiLietotaji,p2=visiProdukti)
  
@app.route('/edituser', methods=["GET","POST"])
def edituser():
  if request.method == "GET":
    userid = request.args.get('id')
    if userid is None:
      return redirect(('mainpage'))
    else:
      lietotajs = dbMethods.selectUserById(userid)
      return render_template('edituser.html',p1=lietotajs,id=userid)
  else:
    userid = request.form['userid']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    dbMethods.updateUser(userid,username,password,email)
    return redirect('mainpage')

@app.route('/editproduct', methods=["GET","POST"])
def editproduct():
  if request.method == "GET":
    productid = request.args.get('id')
    if productid is None:
      return redirect('mainpage')
    else:
      produkts = dbMethods.selectProductById(productid)
      return render_template('editproduct.html',p1=produkts,id=productid)
  else:
    productid = request.form['productid']
    productname = request.form['productname']
    price = request.form['price']
    description = request.form['description']
    dbMethods.updateProduct(productid,productname,price,description)
    return redirect('mainpage')

@app.route('/adduser', methods=["GET","POST"])
def adduser():
  if request.method == "GET":
      return render_template('adduser.html')
  else:
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    dbMethods.addUser(username,password,email)
    return redirect('mainpage')

@app.route('/addproduct', methods=["GET","POST"])
def addproduct():
  if request.method == "GET":
      return render_template('addproduct.html')
  else:
    productname = request.form['productname']
    price = request.form['price']
    description = request.form['description']
    dbMethods.addProduct(productname,price,description)
    return redirect('mainpage')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

