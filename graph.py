import csv
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, file_name):
    
        self.file_name = file_name             
        self.input_data = []
        self.intensity = [[]]
        
    def parse_data(self):
        with open(self.file_name) as csvfile:
            data = csv.reader(csvfile, delimiter='\n')
            for row in data:
                self.input_data.append(eval(row[0]))
        return self.input_data
                
    def generate_intensity(self, coordinates, width, height):
        self.intensity = [[0 for x in range(width)] for y in range(height)]
        for x in range(width):
            for y in range(height):
                self.intensity[x][y] = coordinates.count([x,y])/10
        return self.intensity

    def generate_graph(self, intensity):
        plt.imshow(intensity, cmap='hot', interpolation = 'nearest')
        plt.savefig('foo.png', bbox_inches='tight')
        plt.savefig('foo.pdf')
        plt.show()
        
