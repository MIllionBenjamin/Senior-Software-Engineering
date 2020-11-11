import random

BEGIN_WEEK = 12
GROUP_AMOUNT = 29
NUM_PER_WEEK = 4

id_list = list(range(1, GROUP_AMOUNT + 1))

random.shuffle(id_list)

for i in range(0, GROUP_AMOUNT, NUM_PER_WEEK):
    if i + NUM_PER_WEEK < GROUP_AMOUNT:
        print("week " + str(BEGIN_WEEK + i // 4) + ":", id_list[i: i + 4])
    else:
        print("week " + str(BEGIN_WEEK + i // 4) + ":", id_list[i: ])
    
