# tictactoe
A simple TicTacToe game.

![](/demo/demo.gif)


## Table of contents
* [General info](#general-info)
* [File structure](#file-structure)
* [Requirements](#requirements)
* [Resources](#resources)


##  General info
* Simple Tic-Tac-Toe game. 
* Written in python3 using Flask web application framework(Model-Template-View).
* Implemented MiniMax algorithm as AI.

## File structure
* app.py : FLASK app (Template)
* tictactoe.py : Game class (Model)
* templates :
    - index.html (View)
* static :
    - style.css

## Requirements
* click==7.1.1
* Flask==1.1.2
* itsdangerous==1.1.0
* Jinja2==2.11.1
* MarkupSafe==1.1.1
* numpy==1.18.2
* python-dotenv==0.12.0
* Werkzeug==1.0.1

## Resources
* Mina Krivokuca: 
  - https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
* GeeksforGeegs
    - https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
