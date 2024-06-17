
import seedhelper.structures as sth
import math
import numpy
import keyboard
import time
seed = -1190917522
offset = 320.5

x = int(input("Enter x coordinate: "))
z = int(input("Enter Z coordinate: "))


blacklist = []

x1 = x/offset
z1 = z/offset

ships = sth.get_elytras_positions(seed,x=round(x1),z=round(z1), r=10000, mc_version="1.20")
while True:
    
    if keyboard.is_pressed("]"):
        distance = []
        xpos = []
        zpos = []
        count = 0
        
    
        for ship in ships:
            dist = math.hypot(x - ship.pos.x, z - ship.pos.z)    
            xpos.append(ship.pos.x)
            zpos.append(ship.pos.z)
            distance.append(dist)
        
        combined = list(zip(xpos, zpos, distance))
        sorted_combined = sorted(combined, key=lambda x: x[2])
        xpos_sorted, zpos_sorted, distance_sorted = zip(*sorted_combined)
        xpos_sorted = list(xpos_sorted)
        zpos_sorted = list(zpos_sorted)
        distance_sorted = list(distance_sorted)
        coordniate = list(zip(xpos_sorted,zpos_sorted))
            
        while coordniate[count] in blacklist:
            count = count+1
        print("End city found: "+str(xpos_sorted[count]) +" "+str(zpos_sorted[count]))
        blacklist.append(coordniate[count])
    
        keyboard.press_and_release("t")
        time.sleep(0.1)
        keyboard.write(".waypoint del 0")
        keyboard.press_and_release("enter")
        time.sleep(0.1)
        keyboard.press_and_release("t")
        time.sleep(0.1)
        keyboard.write(".waypoint add 0 "+" "+str(xpos_sorted[count]) + " 120 "+str(zpos_sorted[count]))
        keyboard.press_and_release("enter")
        x = xpos_sorted[count]
        z = zpos_sorted[count]
        x1 = x/offset
        z1 = z/offset
        ships = sth.get_elytras_positions(seed,x=round(x1),z=round(z1), r=10000, mc_version="1.20")
        
        
    
        
   
    
    
    
    
