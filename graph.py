import csv
import numpy as np
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, file_name):
    
        self.file_name = file_name             
        self.input_data = []
        self.intensity = [[]]
        
    def parse_data(self):
        self.input_data = np.genfromtxt(self.file_name + '.csv',delimiter=',')
        self.x = self.input_data[:,0]
        self.y = self.input_data[:,1]
        return self.x,self.y

    def generate_graph(self):
        heatmap, xedges, yedges = np.histogram2d(self.x,self.y,bins=100)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        plt.clf()
        plt.imshow(heatmap.T, extent=extent, origin='lower')
        plt.savefig(self.file_name + '.png', bbox_inches='tight')
        plt.savefig(self.file_name + '.pdf')
        #plt.show()
        
