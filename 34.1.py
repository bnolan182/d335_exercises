"""Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site"""

# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles

employee_A = 15.62
employee_B = 41.85
employee_C = 32.67

input_A = int(input())
input_B = int(input())
input_C = int(input())

total_A = input_A * employee_A
total_B = input_B * employee_B
total_C = input_C * employee_C

print(f"Distance: {total_A + total_C + total_B:.2f} miles")
