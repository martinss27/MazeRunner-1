from pyamaze import maze, COLOR, agent

def DFS(m):
    start=(m.rows,m.cols)
    seen=[start]
    frontier=[start]
    logicpath={}


    while len(frontier)>0:
        current=frontier.pop() #To move to next position on map, the values gathered in stack of frontier is used
        if current==(1,1):
            break
        for d in 'ESNW': # priority is WNSE, but put in reverse as it uses stack
            if m.maze_map[current][d]==True:
                if d == 'E':
                    next = (current[0], current[1] + 1)
                elif d== 'W':
                    next = (current[0], current[1] - 1)
                elif d == 'S':
                    next = (current[0] + 1, current[1])
                elif d == 'N':
                    next = (current[0] - 1, current[1])
                if next in seen:
                    continue
                seen.append(next)
                frontier.append(next)
                logicpath[next]=current #to map path from goal to the start
    fwd_path={}
    cell=(1,1)
    while cell != start:
        fwd_path[logicpath[cell]]=cell
        cell=logicpath[cell]
        return fwd_path

if __name__=='__main__':
    m=maze(7,25)    #Determining the size of the maze
    m.CreateMaze(loopPercent=40)   #Creating the maze
    path= DFS(m)
    a=agent(m,shape='arrow', footprints=True)
    m.tracePath({a:m.path},delay=100, showMarked=True)

    m.run()
