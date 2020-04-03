a=['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

def count_list (a_list):
    result = {}
    for fruit in a_list:

        if fruit in result.keys():
            result[fruit] +=1
        else:
            result[fruit] = 1
    return result

print(count_list(a))