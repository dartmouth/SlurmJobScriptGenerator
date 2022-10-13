#!/usr/bin/python3.6
import subprocess, array, json
#sinfo -h --format="[%n--%c CPUs,%Y Cores|Memory=%m,State=%a,Load=%O,partition:%P\")" #human-readable
#====================================================
def node(self,name,cpus,cores,mem,state,load,partition):
    node = []
node_list = []

with open("sinfo.csv") as file: #csv format
           node_arr = [line.rstrip() for line in file.readlines()]
           # print (node_arr[7]+":")
           node_arr.remove(node_arr[0])  #header line
           # print ("----------------------")
           for index in range(len(node_arr)):
              my_names = []
              attrib_list = node_arr[index].split (",")
              # print (attrib_list[0:3])
              node.name = attrib_list[0]
              node.group = attrib_list[0][0]
              node.cpus = attrib_list[1]
              node.cores = attrib_list[2]
              node.mem = attrib_list[3]
              node.state= str(attrib_list[4])
              if attrib_list[5] == "N/A":
                    node.load = 0
              else:
                    node.load = (float( attrib_list[5]) / float(node.cores))
                    node.load = round (node.load,3)
              node.partition = attrib_list[6]

              # if node.state == "down":
              if node.state in("down","down*"):
                 # node.color="black"
              # elif node.load<=.5:
                 # node.color='blue'
              # elif 1 < node.load:
                 # node.color='purple'
              # elif 1 < node.load < 2.5:
                 # node.color='magenta'
              # elif 2.5 <= node.load < 4:
                 # node.color='orange'
              # else:
                 # node.color='red'
              # print(node.name," is in group", node.group, "and is ",node.state," and load is ",node.load," and  color is ", node.color)
                node_list.append(node.__dict__)
              encoded_data = json.dumps( node_list )
              print(encoded_data)
 
