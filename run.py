import subprocess
from flask import Flask,request, render_template



app = Flask(__name__)



@app.route('/',methods=["GET","POST"])
def playsound():
    if request.method == 'GET':
        return '''<!DOCTYPE html>                                       <html>                                                        <link rel="stylesheet" href="static/style.css">                                                     <body>                                                                                                                                                            <form action="/" method="POST" style="border:1px
solid #ccc">                                            <div class="container">                                 <h1>Play sound</h1>                                        <hr>                                                                                                        <input id="text" type="text" placeholder="Text to play" name="text" required>                                                                                     <button type="submit" class="signupbtn">Play</button>                                                       </div>                                              </div>                                              </form>                                               
</body>'''
    text = request.values.get("text")
    MyOut = subprocess.call(f'''termux-tts-speak {text}''', shell=True)
    return '''<!DOCTYPE html>                                       <html>                                                        <link rel="stylesheet" href="static/style.css">                                                     <body>                                                                                                                                                            <form action="/" method="POST" style="border:1px
solid #ccc">                                            <div class="container">                                 <h1>Play sound</h1>                                        <hr>                                                                                                        <input id="text" type="text" placeholder="Text to play" name="text" required>                                                                                     <button type="submit" class="signupbtn">Play</button>                                                       </div>                                              </div>                                              </form>                                               
</body>'''

if __name__ =='__main__':
    app.run(debug=True)
