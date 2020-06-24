from flask import Flask, request, redirect, url_for, render_template
import tictactoe as ttt
import time

app = Flask(__name__)

game = ttt.Game()

@app.route('/')
@app.route('/index')
def index():
     return render_template("index.html", board_state=game.get_board(), result=game.get_result(), level=game.get_level())     


@app.route('/index/<int:id>')
def input(id):
     print(id)
     p = game.set_move(id)
     r = game.get_result()
     print(r)
     print(game.level)
     game.get_move()
     if not r:
          
          game.get_move()
          
     r = game.get_result()
     return render_template("index.html", board_state=game.get_board(), result=game.get_result(), level=game.level)     

@app.route('/index/easy')
def easy():
     game.set_level('Easy') 
     return redirect('/')

@app.route('/index/medium')
def medium():
     game.set_level('Medium')
     return redirect('/')


@app.route('/index/reset')
def reset():
     game.initialize_game()
     return render_template("index.html", board_state=game.get_board(), level=game.get_level())     


if __name__ == "__main__":
    
    app.run()
    
     
    
