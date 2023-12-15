#import random module to use sample method
import random
import string


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

#define the number of dictionaries
num_dicts = random.randint(2,10)
print(num_dicts)

#variable for our list of generated dictionaries, firstly it's empty
task_dict=[]

#cycle for filling the dictionary
for r in range(num_dicts):
    #dict's values should be a number (0-100)
    size = random.randint(1, 100)
    #populate a list (keys = letter from a to z, values = integer from 0 to 100
    new_dict = {random.choice(string.ascii_lowercase): random.randint(0, 100) for s in range(size)}
    #add key,value to dictionary
    task_dict.append(new_dict)

#recheck the dictionaries
print(task_dict)

#variable for combined dictionary
combined_dict = {}

for i, curr_dict in enumerate(task_dict, start=1):
        for key, value in curr_dict.items():
            # If key is already in the combined_dict, update it with the max value
            if key in combined_dict:
                if value > combined_dict[key]:
                    combined_dict[key] = value
                    # Rename the key with dict number having max value, f'{key}_{i}' creates a new string by combining the value of key, an underscore (_), and the value of i
                    combined_dict[f'{key}_{i}'] = combined_dict.pop(key)
            else: combined_dict[key] = value

print("\n")
print(combined_dict)