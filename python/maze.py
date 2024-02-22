# from operator import truediv
# from pickle import TRUE
# import node as nd
# import numpy as np
# import csv
# import pandas
# import math
# from enum import IntEnum

# class Action(IntEnum):
#     ADVANCE = 1
#     U_TURN = 2
#     TURN_RIGHT = 3
#     TURN_LEFT = 4
#     HALT = 5


# class Maze:
#     def __init__(self, filepath,start):
#         # TODO : read file and implement a data structure you like
# 		# For example, when parsing raw_data, you may create several Node objects.  
# 		# Then you can store these objects into self.nodes.  
# 		# Finally, add to nd_dict by {key(index): value(corresponding node)}
#         self.raw_data = pandas.read_csv(filepath).values
#         self.raw_data[np.isnan(self.raw_data)]=0
#         self.nodes = []
#         self.nd_dict = dict()  # key: index, value: the correspond node
#         self.deadends= []
#         for i in range(len(self.raw_data)):
#             self.nodes.append(nd.Node(i+1))
#         for i in range(len(self.raw_data)):
#             if(self.raw_data[i][1]!=0):
#                 self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][1])-1],1)
#             if(self.raw_data[i][2]!=0):
#                 self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][2])-1],2)
#             if(self.raw_data[i][3]!=0):
#                 self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][3])-1],3)
#             if(self.raw_data[i][4]!=0):
#                 self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][4])-1],4)
#             if(len(self.nodes[i].Successors)==1):
#                 self.deadends.append(self.nodes[i])
#         self.nd_dict[1]=(self.nodes[start-1])


#     def getStartPoint(self):
#         if (len(self.nd_dict) < 2):
#             print("Error: the start point is not included.")
#             return 0
#         return self.nd_dict[1]

#     def getNodeDict(self):
#         return self.nd_dict

#     def BFS(self, nd):
#         # TODO : design your data structure here for your algorithm
#         # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
#         the_maze=list()
#         visited=list()
#         pre_node=dict()
#         path=list()
#         the_maze.append(nd)
#         while len(the_maze)!=0:
#             deadend=True
#             for suc in the_maze[-1].Successors:
#                 if suc[0] not in visited:
#                     deadend=False
#                     the_maze.insert(0,suc[0])
#                     pre_node[suc[0]]=the_maze[-1]
#                     visited.append(suc[0])
#             if deadend:
#                 path.append(the_maze[-1])
#                 temp=the_maze[-1]
#                 while(temp!=nd):
#                     temp=pre_node[temp]
#                     path.append(temp)
#             the_maze.pop()
#         path.reverse()
#         return path

#     def BFS_2(self, nd_from, nd_to):
#         # TODO : similar to BFS but with fixed start point and end point
#         # Tips : return a sequence of nodes of the shortest path
#         visited=list()
#         maze_queue=list()
#         pre_node=dict()
#         path=list()
#         maze_queue.append(nd_from)
#         while(len(maze_queue)!=0):
#             for suc in maze_queue[-1].Successors:
#                 if suc[0] not in visited:
#                     maze_queue.insert(0,suc[0])
#                     pre_node[suc[0]]=maze_queue[-1]
#                     visited.append(suc[0])
#             maze_queue.pop()
#         temp=nd_to
#         path.append(temp)
#         while temp!=nd_from:
#             temp=pre_node[temp]
#             path.append(temp)
#         path.reverse()
#         return path

#     def getAction(self, car_dir, nd_from, nd_to):
#         # TODO : get the car action
#         # Tips : return an action and the next direction of the car if the nd_to is the Successor of nd_from
# 		# If not, print error message and return 0
#         directing=int(nd_from.getDirection(nd_to))
#         dict_N=[]
#         dict_N.append(0)
#         dict_S=[]
#         dict_S.append(0)
#         dict_W=[]
#         dict_W.append(0)
#         dict_E=[]
#         dict_E.append(0)
        
#         dict_N.append(1),dict_N.append(2),dict_N.append(4),dict_N.append(3)
#         dict_S.append(2),dict_S.append(1),dict_S.append(3),dict_S.append(4)
#         dict_W.append(3),dict_W.append(4),dict_W.append(1),dict_W.append(2)
#         dict_E.append(4),dict_E.append(3),dict_E.append(2),dict_E.append(1)
#         ans=[]
#         if car_dir==1:
#             ans.append(dict_N[directing])
#             ans.append(directing)
#         if car_dir==2:
#             ans.append(dict_S[directing])
#             ans.append(directing)
#         if car_dir==3:
#             ans.append(dict_W[directing])
#             ans.append(directing)
#         if car_dir==4:
#             ans.append(dict_E[directing])
#             ans.append(directing)
#         return ans

#     def getActions(self, nodes):
#         # TODO : given a sequence of nodes, return the corresponding action sequence
#         # Tips : iterate through the nodes and use getAction() in each iteration
#         actions=[]
#         cur_dir=1
#         for suc in nodes[0].Successors:
#             cur_dir=suc[1]
#         for i in range(len(nodes)-1):
#             for suc in nodes[i].Successors:
#                 if suc[0]==nodes[i+1]:
#                     temp=self.getAction(cur_dir,nodes[i],nodes[i+1])
#                     cur_dir=temp[1]
                    
#                     actions.append(temp[0])
#         return actions

#     def actions_to_str(self, actions):
#         # cmds should be a string sequence like "flbrs....", use it as the input of BFS checklist #1
#         cmd = "fbrls"
#         cmds = ""
#         for action in actions: cmds += cmd[action-1]
#         return cmds

#     def strategy(self, nd):
#         return self.BFS(nd)

#     def strategy_2(self, nd_from, nd_to):
#         return self.BFS_2(nd_from, nd_to)


from operator import truediv
from pickle import TRUE
import node as nd
import numpy as np
import csv
import pandas
import math
from enum import IntEnum

class Action(IntEnum):
    ADVANCE = 1
    U_TURN = 2
    TURN_RIGHT = 3
    TURN_LEFT = 4
    HALT = 5


class Maze:
    def __init__(self, filepath,start):
        # TODO : read file and implement a data structure you like
		# For example, when parsing raw_data, you may create several Node objects.  
		# Then you can store these objects into self.nodes.  
		# Finally, add to nd_dict by {key(index): value(corresponding node)}
        self.raw_data = pandas.read_csv(filepath).values
        self.raw_data[np.isnan(self.raw_data)]=0
        self.nodes = []
        self.nd_dict = dict()  # key: index, value: the correspond node
        self.deadends= []
        self.deadends_dis=[] 
        self.start_index=start-1
        self.dp=np.array
        self.computed=np.array
        self.times=0
        self.trace_path=np.array
        self.hamming_dis=[]
        self.start_direction=-1
        self.selection_score=np.array
        #the score is the score of each deadend in increasing index order
        for i in range(len(self.raw_data)):
            self.nodes.append(nd.Node(i+1))
        for i in range(len(self.raw_data)):
            if(self.raw_data[i][1]!=0):
                self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][1])-1],1)
            if(self.raw_data[i][2]!=0):
                self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][2])-1],2)
            if(self.raw_data[i][3]!=0):
                self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][3])-1],3)
            if(self.raw_data[i][4]!=0):
                self.nodes[i].setSuccessor(self.nodes[int(self.raw_data[i][4])-1],4)
            if(len(self.nodes[i].Successors)==1):
                if(i!=start-1):
                    self.deadends.append(self.nodes[i])
        self.start_direction=self.nodes[start-1].Successors[0][1]
        self.nd_dict[1]=(self.nodes[start-1])
        for i in range(len(self.deadends)):
            self.deadends_dis.append([])
        self.startpoint=self.nodes[start-1]
        
        return None

    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def BFS(self, nd):
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        the_maze=list()
        visited=list()
        pre_node=dict()
        path=list()
        the_maze.append(nd)
        while len(the_maze)!=0:
            deadend=True
            for suc in the_maze[-1].Successors:
                if suc[0] not in visited:
                    deadend=False
                    the_maze.insert(0,suc[0])
                    pre_node[suc[0]]=the_maze[-1]
                    visited.append(suc[0])
            if deadend:
                path.append(the_maze[-1])
                temp=the_maze[-1]
                while(temp!=nd):
                    temp=pre_node[temp]
                    path.append(temp)
            the_maze.pop()
        path.reverse()
        return path

    def BFS_2(self, nd_from, nd_to):
        # TODO : similar to BFS but with fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path
        visited=list()
        maze_queue=list()
        pre_node=dict()
        path=list()
        maze_queue.append(nd_from)
        while(len(maze_queue)!=0):
            for suc in maze_queue[-1].Successors:
                if suc[0] not in visited:
                    maze_queue.insert(0,suc[0])
                    pre_node[suc[0]]=maze_queue[-1]
                    visited.append(suc[0])
            maze_queue.pop()
        temp=nd_to
        path.append(temp)
        while temp!=nd_from:
            temp=pre_node[temp]
            path.append(temp)
        path.reverse()
        return path

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car if the nd_to is the Successor of nd_from
		# If not, print error message and return 0
        directing=nd_from.getDirection(nd_to)
        dict_N=[]
        dict_N.append(0)
        dict_S=[]
        dict_S.append(0)
        dict_W=[]
        dict_W.append(0)
        dict_E=[]
        dict_E.append(0)
        
        dict_N.append(1),dict_N.append(2),dict_N.append(4),dict_N.append(3)
        dict_S.append(2),dict_S.append(1),dict_S.append(3),dict_S.append(4)
        dict_W.append(3),dict_W.append(4),dict_W.append(1),dict_W.append(2)
        dict_E.append(4),dict_E.append(3),dict_E.append(2),dict_E.append(1)
        ans=[]
        if car_dir==1:
            ans.append(dict_N[directing])
            ans.append(directing)
        if car_dir==2:
            ans.append(dict_S[directing])
            ans.append(directing)
        if car_dir==3:
            ans.append(dict_W[directing])
            ans.append(directing)
        if car_dir==4:
            ans.append(dict_E[directing])
            ans.append(directing)
        return ans

    def getActions(self, nodes):
        # TODO : given a sequence of nodes, return the corresponding action sequence
        # Tips : iterate through the nodes and use getAction() in each iteration
        actions=[]
        cur_dir=int(self.start_direction)
        for i in range(len(nodes)-1):
            for suc in nodes[i].Successors:
                if suc[0]==nodes[i+1]:
                    temp=self.getAction(cur_dir,nodes[i],nodes[i+1])
                    cur_dir=temp[1]
                    actions.append(temp[0])
        return actions

    def actions_to_str(self, actions):
        # cmds should be a string sequence like "flbrs....", use it as the input of BFS checklist #1
        cmd = "fbrls"
        cmds = ""
        for action in actions: cmds += cmd[action-1]
        return cmds
    def score_initial(self):
        self.selection_score=np.full((2**len(self.deadends),2),0)
        for i in range(2**len(self.deadends)):
            temp='{0:b}'.format(i)
            temp=temp[::-1]
            for j in range(len(temp)):
                if(temp[j]=='1'):
                    self.selection_score[i][0]+=self.hamming_dis[j]
            self.selection_score[i][1]=i
        self.selection_score=self.selection_score[self.selection_score[:, 0].argsort()]
        return None
    def deadenddis_ini(self):
        L=len(self.deadends)
        for i in range(L):
            for j in range(L):
                if i != j:
                    self.deadends_dis[i].append(len(self.BFS_2(self.deadends[i],self.deadends[j]))-1)
                else:
                    self.deadends_dis[i].append(0)
        return None 
    def strategy(self, nd):
        return self.BFS(nd)
    
    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)
    def distance_dp_initial(self):
        self.dp=np.full((2**(len(self.deadends)),len(self.deadends)),999)
        self.computed=np.full((2**(len(self.deadends)),len(self.deadends)),False)
        self.trace_path=np.full((2**(len(self.deadends)),len(self.deadends),len(self.deadends)),999)
        for i in range(len(self.deadends)):
            temp=2**i
            self.dp[temp][i]=len(self.BFS_2(self.startpoint,self.deadends[i]))-1
            self.computed[temp][i]=True
            self.trace_path[temp][i][0]=(self.deadends[i].getIndex())
        return None
    def hamming_initial(self):
        weight=dict()
        weight[1]=[1,0]
        weight[2]=[-1,0]
        weight[3]=[0,1]
        weight[4]=[0,-1]
        for i in range(len(self.deadends)): 
            temp=self.BFS_2(self.nodes[self.start_index],self.deadends[i])
            print(len(temp))
            dis=[0,0]
            for j in range(len(temp)-1):
                dis[0]+=weight[int(temp[j].getDirection(temp[j+1]))][0]
                dis[1]+=weight[int(temp[j].getDirection(temp[j+1]))][1]
                #print(int(temp[j].getDirection(temp[j+1])),end=" ")
            self.hamming_dis.append(abs(dis[0])+abs(dis[1]))
        return None
    def dis_dp(self,index,terminal):
        self.times+=1
        if(self.computed[index][terminal]):
            return self.dp[index][terminal]
        else:
            flag=False
            temp='{0:b}'.format(index)
            temp=temp[::-1]
            for i in range(len(temp)):
                if(temp[i]=='1' and terminal==i):
                    flag=True
            if(flag==False):
                return 999
            else:
                index=index-2**terminal
                temp='{0:b}'.format(index)
                temp=temp[::-1]
                ans=999
                amount=0
                for i in range(len(temp)):
                    if(temp[i]=='1'):
                        amount+=1
                        if(ans>self.dis_dp(index,i)+self.deadends_dis[i][terminal]):
                            ans=self.dis_dp(index,i)+self.deadends_dis[i][terminal]
                            self.trace_path[index+2**terminal][terminal]=self.trace_path[index][i]
                self.computed[index+2**terminal][terminal]=True
                self.dp[index+2**terminal][terminal]=ans
                self.trace_path[index+2**terminal][terminal][amount]=self.deadends[terminal].getIndex()
                return self.dp[index+2**terminal][terminal]
            