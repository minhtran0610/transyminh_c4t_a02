sx = int(input("Enter start x_coordinate: "))
sy = int(input("Enter start y_coordinate: "))
dx = int(input("Enter destination x_coordinate: "))
dy = int(input("Enter destination y_coordinate: "))

def move(dx, dy):
    global sx
    global sy

    if (dx > sx and dy <= sy) or (dy > sy and dx <= sx):
        return
    if (dx > sx and dy > sy) or (dx > sx and dy > sy):
        return False
    elif (dx == sx) and (dy == sy):
        return True
    
    print(dx, dy)
    move(dx+dy, dy)
    move(dx, dy+dx)

    

print(move(dx,dy))

    
     
