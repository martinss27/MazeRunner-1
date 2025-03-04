from pyamaze import maze, COLOR, agent

m=maze(7,20)    #Determining the size of the maze
m.CreateMaze(loopPercent=40)   #Creating the maze

a=agent(m,shape='square',footprints=True,filled=True)

m.tracePath({a:m.path},delay=100, showMarked=True)

m.run() #Running the application
