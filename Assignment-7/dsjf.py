# employee_count = {}
# given = ["HR", "Programmer", "Intern"]
# hr_count = 10
# intern_count = 6
# programmer_count = 5
# count_list = []
# count_list.extend(hr_count, intern_count, programmer_count)

# for i in range(len(given)):
#     pass

employee_count = {}
given = ["HR", "Programmer", "Intern"]
hr_count = 10
intern_count = 6
programmer_count = 5
total_count = 0

count_list = [hr_count, programmer_count, intern_count]

for i in range(len(given)):
    employee_count[given[i]] = count_list[i]
    total_count += count_list[i]

print(employee_count)

for k, v in employee_count.items():
    print(f"Category: {k}, Count: {v}")
    
print(total_count)