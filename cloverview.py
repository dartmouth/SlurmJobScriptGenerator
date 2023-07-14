#!/usr/bin/python-3.8.5
import subprocess, array
##sinfo -h --format="[%n--%c CPUs,%Y Cores|Memory=%m,State=%a,Load=%O,partition:%P\")" #human-readable
#====================================================
#sinfo_data is formatted as a python array: no easy way to use preformatted array, might as well just CSV it?
# sinfo -h --format="[%n,%c,%Y,%m,%a,%O,%P]" | sort -r
#====================================================
# stuff that didn't work:
# command = "'sinfo','--format=\"%n,%c, %Y,%m'"
      # sinfo = subprocess.run([command])
#####sinfo_data = subprocess.check_output(['sinfo','--format=[%n,%c,%Y,%m,%a,%O,%P]'])
# print ("rc = "+ str(sinfo_data.returncode))
#====================================================
#====================================================
def node(self,name,cpus,cores,mem,state,load,partition):                                                                                   node = []  
with open("sinfo.csv") as file: #csv format
           node_arr = [line.rstrip() for line in file.readlines()]
           print (node_arr[7]+":")
           print ("----------------------")
           for index in range(len(node_arr)):
              attrib_list = node_arr[index].split (",")
              # print (attrib_list[0:3])
              node.name = attrib_list[0]
              node.group = attrib_list[0][0]
              node.cpus = int(attrib_list[1])
              node.cores = int(attrib_list[2])
              node.mem = int(attrib_list[3])
              node.state= str(attrib_list[4])
              if attrib_list[5]=="N/A":
                attrib_list[5]=0
              node.load = float(attrib_list[5])
              node.partition = attrib_list[6]
              if node.state != "up":
                 node.color="black"
              elif node.load<=.5:
                 node.color='blue'
              elif 1 < node.load <=2.5:
                 node.color='purple'


              elif 2.5 < node.load <= 4:
                 node.color='magenta'
              elif 4 <= node.load < 5:
                 node.color='orange'
              else:
                 node.color='red'
              print(node.name," is in group", node.group, "and is ",node.state," and load is ",node.load," and  color is ", node.color)
              print ("----------------------")
######################################################################################################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
node_list=[]
node_list.append(node.__dict__)
print (node_list)
#node_list.insert((node.__dict__))
#print((node.__dict__))
#node_list.append(node.__dict__)
# encoded_data = json.dumps( node_list )
# print(encoded_data)

# sns.set()
#uniform_data = node.group,node.load
# #ax = sns.heatmap(uniform_data, vmin=0, square=True, cmap='Greens')

# #plt.title("Discovery Heatmap")
# #plt.show()
               
