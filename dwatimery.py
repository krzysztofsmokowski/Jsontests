


def update_list1800(list1):

def update_list20(list1):
    pass





timer = 0
while True:
    if timer%1800 == 0:
        update_list1800()
    if timer%20 == 0:
        update_list20()
    time.sleep(1)
    timer=timer+1

