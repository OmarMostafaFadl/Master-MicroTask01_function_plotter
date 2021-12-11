import sys
from sympy import var
from sympy import sympify

import matplotlib.pyplot as plt
import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QInputDialog, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot

class UsersFunction():
    
    """This class contains all the functions used to solve and plot the user entered funciton
    """

    def solve_function(text, u_min, u_max):

        """
        This function takse a Mathematical function, Minimum boundary and Maximum Boundary and solves them
        to return all the X and Y points of the function within the boundary

        Inputs : 
            String: text
            Int: u_min
            Int: u_max

        Returns:
            List: x_iters
            List: y_iters
        """
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

        """
        This function takes all the X and Y points and plots the graph
        
        Inputs : 
            List: x_iters
            List: y_iters

        Returns:
            None
        """

        plt.plot(x_iters, y_results, 'b')
        plt.title("Graph Plot")
        plt.show()



class MyWindow(QMainWindow, UsersFunction):                  #Inherites everything from QMainWindow

    """This class is for the GUI
    """

    def __init__(self):

        """This Function is called whenever an object of MyWindow is made.
        """

        super(MyWindow, self).__init__()
        self.setGeometry(200, 100, 400, 400)
        self.setWindowTitle('Function Plotter')
        self.initUI()

    def initUI(self):

        """This Function initilizes the UI
        """   
        

        self.start_button()
        
    def start_button(self):

        """This function add a Start button to the GUI and calls another function whenever
        this button is clicked
        """

        button = QPushButton('Start', self)
        button.setToolTip('Press this button to add a function to plot')
        button.move(100,70)
        button.resize(200, 200)
        button.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):

        """When the button is clicked this function is called to get all inputs from the user
        """

        try:

            text = self.get_function()
            u_min, u_max = self.get_boundaries()
            x_iters, y_results = UsersFunction.solve_function(text, u_min, u_max)
            UsersFunction.plot_function(x_iters, y_results)

        except:
            QMessageBox.question(self, "Error Message", "Please Enter the Data Correctly", QMessageBox.Ok, QMessageBox.Ok)

    def get_function(self):

        """This function gets a string from the user which is the math function.

        Returns:
            String: users_function
        """

        users_function, result = QInputDialog.getText(self, 'input Function', 'Please Enter Your Function')

        return users_function

    def get_boundaries(self):

        """This function takes from the user the function boundaries

        Returns:
            Int: users_min
            Int_ users_max
        """

        users_min, result = QInputDialog.getText(self, 'Input Min and Max', 'Please Enter Your Min')
        users_max, result = QInputDialog.getText(self, 'Input Min and Max', 'Please Enter Your Max')

        return users_min, users_max
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
