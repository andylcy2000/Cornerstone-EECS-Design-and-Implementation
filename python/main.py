import maze as mz
from score import ScoreboardFake, Scoreboard
from BTinterface import BTinterface

import numpy as np
import threading
import pandas
import time
import sys
import os



a = []
def main():
    interf = BTinterface()
    # maze = mz.Maze("data/big_maze_111.csv",6)
    # maze.deadenddis_ini()
    # maze.distance_dp_initial()
    # maze.hamming_initial()
    # maze.score_initial()
    # index=0
    # ans=9999
    # # s=[]
    # for i in range(len(maze.deadends)):
    #     if(ans>maze.dis_dp(2**len(maze.deadends)-1,i)):
    #         index=i
    #         ans=maze.dis_dp(2**len(maze.deadends)-1,i)
    # first=maze.BFS_2(maze.nodes[5],maze.nodes[maze.trace_path[2**len(maze.deadends)-1][index][0]-1])
    # for i in range(len(first)-1):
    #     s.append(first[i])
    # for i in range(len(maze.deadends)-1):
    #     n_a=maze.nodes[maze.trace_path[2**len(maze.deadends)-1][index][i]-1]
    #     n_b=maze.nodes[maze.trace_path[2**len(maze.deadends)-1][index][i+1]-1]
    #     s.append(n_a)
    #     temp=maze.BFS_2(n_a,n_b)
    #     for j in range(1,len(temp)-1):
    #         s.append(temp[j])
    # s.append(maze.nodes[maze.trace_path[2**len(maze.deadends)-1][index][len(maze.deadends)-1]-1])
    # s=maze.getActions(s)
    # nodes_set=maze.getNodeDict()
    
    # s=[]
    # for i in range(len(maze.deadends)-1):
    #     s+=maze.BFS_2(maze.deadends[i],maze.deadends[i+1])
    # s=maze.getActions(s)
    # print(maze.actions_to_str(s))
    # dir = maze.actions_to_str(s)
    dir = "fffffffff"
    # dir = "flrlfbrflbfrbrfffblbllflflbrfrflffffllrlfbrflbfrbrfffblbllflflbrfrflffffl"
    print(dir)
    # dir = "frrrrrrrrrrrrrrrrrrrrr"
    dir += "bf"
    interf.send_action(dir[0])
    msgWrite = input()
    interf.send_action(msgWrite)
    # point = Scoreboard("linlinlin-1", "http://140.112.175.18:3000")
    point = ScoreboardFake("your team name", "data/fakeUID.csv")
    # TODO : Initialize necessary variables

    def read():
        i = 1
        while True:
            # if interf.waiting():
            uid = interf.get_UID()
            if uid:
                # print(uid)
                if len(uid) > 12:
                    interf.send_action(dir[i])
                    print(dir[i])
                    i += 1
                else:
                    point.add_UID(uid[2:])

    if (sys.argv[1] == '0'):#sys.argv[1] == '0'
        print("Mode 0: for treasure-hunting")
        # TODO : for treasure-hunting, which encourages you to hunt as many scorees as possible
        
    elif (sys.argv[1] == '1'):#sys.argv[1] == '1'
        # TODO: You can write your code to test specific function.
        print("Mode 1: Self-testing mode.")
        readThread = threading.Thread(target=read)
        readThread.daemon = True
        readThread.start()

        while True:
            msgWrite = input()
            interf.send_action(msgWrite)
            # interf.send_action(dirc)
            # print(interf.ser.SerialReadByte())

if __name__ == '__main__':
    main()
