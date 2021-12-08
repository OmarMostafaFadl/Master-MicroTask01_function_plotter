import sys
from sympy import var
from sympy import sympify

import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

class UsersFunction():

    def solve_function(text, u_min, u_max):

        x = var('x')  # the possible variable names must be known beforehand...
        user_input = text
        expr = sympify(user_input)

        x_iters = np.linspace(float(u_min),float(u_max),100)

        y_results = []

        for i in range(100):
            temp = expr.subs(x, x_iters[i])
            y_results.append(temp)

        return x_iters, y_results
        

    def plot_function(x_iters, y_results):

        plt.plot(x_iters, y_results, 'b')
        plt.show()



class MyWindow(QMainWindow, UsersFunction):                  #Inherites everything from QMainWindow

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 100, 1500, 900)
        self.setWindowTitle('Function Plotter')
        self.initUI()

    def initUI(self):
        
        text = self.get_function()
        u_min, u_max = self.get_boundaries()
        x_iters, y_results = UsersFunction.solve_function(text, u_min, u_max)
        UsersFunction.plot_function(x_iters, y_results)

    def get_function(self):
        users_function, result = QInputDialog.getText(self, 'input Function', 'Please Enter Your Function')

        return users_function

    def get_boundaries(self):
        users_min, result = QInputDialog.getText(self, 'Input Min and Max', 'Please Enter Your Min')
        users_max, result = QInputDialog.getText(self, 'Input Min and Max', 'Please Enter Your Max')

        return users_min, users_max
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
