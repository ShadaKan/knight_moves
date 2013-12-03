Simulation of knight moves on a chessboard
============

Simulation of knight moves on a chess board to visualize the stationary probability distribution using markov chains.

This is a simulation for random moves of a knight on a chess board. It was a class project for my Applied Probability class.

Introduction
============
You have a 4x4 chessboard with a knight on a board. A knight can move in two ways. It moves from one square to another square in any direction, turn 90 degrees from first movement, and go two more squares. A knight can also first move two squares forward in any direction, and finish up with one more square in 90 degrees angle to the movement. You start from a certain point, and after a large number of movements, the position of the horse will be random, yet not uniform on the chessboard. This project will discuss the Markov Chain and the limit theorem of Markov Chain to find the probability mass function of the position of the Knight. Computer simulation will also be given to verify our results.

I have taken a 4 x 4 chessboard for simplicity. The probability distribution is calcualted by
<br /> P (Cell_i) = Number of times the knight appeared at Cell_i / Total number of moves played

About the Code
============
There is a javascript version and a python version. Work is in progress to get a chart that shows the convergence of the distribution.
