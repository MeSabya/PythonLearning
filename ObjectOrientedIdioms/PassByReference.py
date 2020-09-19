'''A function can change any mutable object passed as a parameter, but it can never replace it with another object.
To understand it, let’s should jump straight to an example. Consider the following function'''

#Example1 :
def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']

print("**************** Working on example 1 *************************")
print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)
print("**************** example 1 completed *************************")

#Example2:
def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print("*************** Example2 Trying to change the object in another function ********************************")
print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)
print("*************** Example2 Done **************")