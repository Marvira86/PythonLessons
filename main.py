#import random module to use sample method
import random


#Generate 100 random numbers - k:100, between 0 and 1000 - range(0,1000)
random_list = random.sample(range(0,1000),100)
print(random_list)

#n - amount of numbers in the random list
n=100;
#iteration amount of external cycle = amount of numbers in the list - 1, since the first element is sorted
for i in range(n - 1):
    #internal cycle. Since the i last elements already sorted, list size can be decreased to n-i-1
    for j in range(n - i - 1):
        #if previous element > than the next one
        if random_list[j] > random_list[j + 1]:
            #swap both of them
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
print(random_list)

