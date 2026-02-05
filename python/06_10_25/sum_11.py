def taxi_fare(distance):
    # write your code here
    if 10>=distance:
        print(15*distance)
    elif distance<=30:
        print((10*15)+(distance-10)*12)
    else:
        print((10*15)+(20*12)+(distance-30)*10)        
taxi_fare(10)
taxi_fare(15)
taxi_fare(35)