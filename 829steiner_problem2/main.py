from __future__ import print_function, division
import networkx as nx
from networkx import *
import numpy
from numpy import *
import matplotlib.pyplot as plt
import random
import steiner_tree as st
import time

    # problem1 의 설명
set_number=int(input("Enter the number of sets to create : "))
print("Enter positive integers in the x and y coordinates")
print("Enter 0 (zero) at x coordinate after completing the input\n")

xcoor=1 ## user가 입력할 x,y좌표, default=1
ycoor=1
listx=[] ## user가 입력한 x, y좌표를 list로 만들기
listy=[]
coorlist=[]
for i in range(set_number):
    coorlist+=[[]]

## user input을 받아들이는 곳
for i in range(set_number):
    while(True):
        xcoor = int(input("Enter x-coordinates : "))
        if(xcoor==0):
            break
        else : listx.append(xcoor)
        ycoor = int(input("Enter y-coordinates : "))
        if (ycoor == 0):
            listx.remove(-1)
            break
        else : listy.append(ycoor)
        coorlist[i].append((xcoor, ycoor))
    print("Complete the set %s \n\n" %(i+1))

for i in range(set_number):
    print("Here is your input of set%s : " %(i+1), coorlist[i])


## graph를 생성하는 곳
max_x=int(max(listx))
max_y=int(max(listy))
G=nx.grid_2d_graph(max_x,max_y)
pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i+1 + (j+1) * max_y ) for i, j in G.nodes() ) ## 여기서 (x, y)를 x+1+(y+1)*max_y로 설정한 것이 중요
nx.relabel_nodes(G,labels,False)
inds=labels.keys()
vals=labels.values()
pos2=dict(zip(vals,inds))
nx.draw_networkx(G, pos=pos2, with_labels=False, node_size = 0)

colorlist=['blue', 'purple', 'red', 'green', 'white', 'silver', 'black']

    # terminal_nodes 리스트 생성하기 terminal_nodes_list = [int(max_y * (listy[i]) + listx[i]) for i in range(len(listx))]
for i in range(set_number):
    print("wait", i)
    terminal_nodes_list = [int(max_y * (coorlist[i][j][1]) + coorlist[i][j][0]) for j in range(len(coorlist[i]))]
    steiner_tree=st.steiner_tree(G, terminal_nodes_list, weight="distance")
    a=terminal_nodes_list
    nx.draw_networkx(steiner_tree,pos=pos2, with_labels=False, node_size=0, edge_color=colorlist[i]) ## terminal_node는 빨간색으로 색칠하기
    nx.draw_networkx_nodes(G, pos=pos2, nodelist=a, node_color=colorlist[i], node_size=25)
plt.show() 
