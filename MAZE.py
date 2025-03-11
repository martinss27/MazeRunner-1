from pyamaze import maze, COLOR, agent

def DFS(m):
    start=(m.rows,m.cols)
    seen=[start]
    frontier=[start]
    logicpath={}

    print("Maze structure:", m.maze_map)

    while frontier:
        current = frontier.pop()
        print(f"Exploring: {current}")

        if current == (1,1):
            break

        for d in 'ESNW': # priority is WNSE, but put in reverse as it uses stack
            if m.maze_map[current][d]:
                if d == 'E':
                    next_cell = (current[0], current[1] + 1)
                elif d == 'W':
                    next_cell = (current[0], current[1] - 1)
                elif d == 'S':
                    next_cell = (current[0] + 1, current[1])
                elif d == 'N':
                    next_cell = (current[0] - 1, current[1])

                if next in seen:
                    continue

                seen.append(next_cell)
                frontier.append(next_cell)
                logicpath[next_cell] = current #to map path from goal to the start
    
    if (1,1) not in logicpath:
        print('Error: DFS did not find a valid path.')
        return {}
    
    fwd_path={}
    cell=(1,1)
    while cell != start:
        fwd_path[logicpath[cell]] = cell
        cell=logicpath[cell]
        
        return fwd_path

if __name__=='__main__':
    m=maze(7,25)    #Determining the size of the maze
    m.CreateMaze(loopPercent=40)   #Creating the maze
    
    path= DFS(m)
    if path:
        a=agent(m,shape='arrow', footprints=True)
        m.tracePath({a: path}, delay=100, showMarked=True)
        m.run()
    else:
        print('No path found. Finishing execution')