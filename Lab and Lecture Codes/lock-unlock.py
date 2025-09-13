def job_scheduling(lock,unlock):
    total_rotation = 0
    while lock > 0 or unlock>0:
        l=lock%10
        u=unlock%10
        total_rotation+=min(abs(l - u), 10 - abs(l - u))
        lock//=10
        unlock//=10
    return total_rotation
        
lock=9287
unlock=0000
print(job_scheduling(lock,unlock))