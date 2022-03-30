#Main Data 
calls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

staff = ["anna", "ben", "cherry"]
staff_count = len(staff)
early_staff = 2
early_calls = calls[:5]


#This will be for which calls are allocated to the early staff which are only two people
early_allocation = {}
for employee in staff[:early_staff]:
    position = staff.index(employee)
    early_allocation[employee] = early_calls[position::early_staff]

early_names_list = list(early_allocation)   #this is to print the keys in our dict

call_values = early_allocation.values()     #this is to print values in our dict
call_values_list = list(call_values)

print(f"""Allocation will be, 
    first: {early_names_list[0]}, who is assigned calls: {call_values_list[0]}. 
    Second: {early_names_list[1]} assigned calls: {call_values_list[1]}""")


#This will be for the calls for the late shift people. The whole staff will be here 
late_calls = calls[5:]
late_staff = staff[::-1]    #reverses the list

late_allocation = {}
for employee in staff:
    position = late_staff.index(employee)
    late_allocation[employee] = late_calls[position::staff_count]
#print(late_allocation)

late_names_list = list(late_allocation)


late_values = late_allocation.values()
late_values_list = list(late_values)


print(f"""Allocation will be, 
    first: {late_names_list[0]}, who is assigned calls: {late_values_list[0]}. 
    Second: {late_names_list[1]} assigned calls: {late_values_list[1]}
    Third: {late_names_list[2]} assigned calls: {late_values_list[2]}""") 

#test