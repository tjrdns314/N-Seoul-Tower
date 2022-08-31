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
print("\nEnter positive integers in the x and y coordinates")
print("Enter 0 (zero) at x coordinate after completing the input\n")

xcoor=1 ## user가 입력할 x,y좌표, default=1
ycoor=1
listx=[] ## user가 입력한 x, y좌표를 list로 만들기
listy=[]
coorlist=[]

## user input을 받아들이는 곳
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
    coorlist.append((xcoor, ycoor))

print("Here is your input : ", coorlist)

## graph를 생성하는 곳
max_x=int(max(listx))
max_y=int(max(listy))
print(max_x, ' ', max_y)
G=nx.grid_2d_graph(max_x,max_y)
pos = dict( (n, n) for n in G.nodes() )
print(G.nodes())
labels = dict( ((i, j), i + j * (max_x) ) for i, j in G.nodes() ) ## 여기서 (x, y)를 x+1+(y+1)*max_y로 설정한 것이 중요
print(labels)
nx.relabel_nodes(G,labels,False)
inds=labels.keys()
vals=labels.values()
pos2=dict(zip(vals,inds))
nx.draw_networkx(G, pos=pos2, with_labels=False, node_size = 0, edge_color='white')

    # terminal_nodes 리스트 생성하기
terminal_nodes_list=[int((max_x)*(listy[i]-1)+listx[i]-1) for i in range(len(listx))]
steiner_tree=st.steiner_tree(G, terminal_nodes_list, weight="distance")
a=terminal_nodes_list
nx.draw_networkx(steiner_tree,pos=pos2, with_labels=False, node_size=0, edge_color='r') ## terminal_node는 빨간색으로 색칠하기
nx.draw_networkx_nodes(G, pos=pos2, nodelist=a, node_color='r', node_size=25)
plt.show()