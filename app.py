from flask import Flask,request, render_template


app = Flask(__name__)


HOBBIES = [
    {
    'id':1,
    'title':'Reading and learning about new libraries',
    'location':'Github',
   },
   {
    'id':2,
    'title':'Playing Chess',
    'location':'Chess App',
   },
   {
    'id':3,
    'title':'Watching and Playing Cricket',
    'location':'Online',
   }
]

@app.route("/")
def hello_world():
    return render_template('home.html', hobbies=HOBBIES)

print(__name__)
if __name__== "__main__":
    print("I an inside if now")
    app.run(host='0.0.0.0', debug= True)
