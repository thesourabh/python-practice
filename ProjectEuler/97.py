import time
start_time = time.clock()

print (28433*(2**7830457)+1) % 10000000000

print time.clock() - start_time, "seconds"