import ipdb

def line(list):
    if len(list) > 0:
        result = ['The line is currently:']
        counter = 1
        for element in list:
          result.append(f"{counter}. {element}")
          counter+=1
        result = ' '.join(result)
        print(result)
    else:
        print('The line is currently empty.')

def take_a_number(que_list, name):
    number_in_line = len(que_list) + 1
    que_list.append(name)
    print(f"Welcome, {name}. You are number {number_in_line} in line.")
    return que_list
    

def now_serving(que_list):
    if len(que_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {que_list[0]}.")
        que_list.pop(0)
        return que_list