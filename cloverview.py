#!/usr/bin/python3.6
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
# array = []
#i = 0
#for line in sinfo_data:
#   print(i)
#   print(line)
#   array = array.append(line)
#   i += 1
   # print(arg[1])
# print ("rc = "+ str(sinfo_data.returncode))
# print (sinfo_data)
#print (array[3])
#====================================================
def node(self,name,cpus,cores,mem,state,load,partition):
    node = []

with open("sinfo.csv") as file: #csv format
           node_arr = [line.rstrip() for line in file.readlines()]
           # print (node_arr[7]+":")
           node_arr.remove(node_arr[0])  #header line
           print ("----------------------")
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
                    node.load = float(attrib_list[5])
              node.partition = attrib_list[6]

              # if node.state == "down":
              if node.state in("down","down*"):
                 node.color="black"
              elif node.load<=.5:
                 node.color='blue'
              elif 1 < node.load:
                 node.color='purple'
              elif 1 < node.load1 < 2.5:
                 node.color='magenta'
              elif 2.5 <= node.load < 4:
                 node.color='orange'
              else:
                 node.color='red'
              print(node.name," is in group", node.group, "and is ",node.state," and load is ",node.load," and  color is ", node.color)

