'''
@author: Solrac
'''
def largest_consecutive_sum(lista):
    big_nums = []
    counter = 0
    
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        sum = lista[0] + lista[1]
        if sum > lista[0] and sum > lista[1]:
            return sum
        elif lista[0] > sum and lista[0] > lista[1]:
            return lista[0]
        else:
            return lista[1]
    else:
        for i in range(len(lista)-2):
            sum1 = lista[i] + lista[i+1]
            sum2 = sum1 + lista[i+2]
            counter = i+2
            while sum2 > sum1 and counter < len(lista)-2:
                sum1 = sum2
                sum2 = sum1 + lista[counter + 1]
                counter += 1
                big_nums.append(sum1)
        print(big_nums)
        return max(big_nums)

lista = [1]
print(largest_consecutive_sum(lista))
lista = [-2, 1]
print(largest_consecutive_sum(lista))
lista = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_consecutive_sum(lista))

