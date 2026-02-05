def total_savings(months):
    total = 0       
    month = 1       
    savings = 100   

    while month <= months:
        total =total+ savings     
        savings =savings+ 50       
        month =month+ 1            

    print( total)


total_savings(1)   
total_savings(3)   
total_savings(6) 
