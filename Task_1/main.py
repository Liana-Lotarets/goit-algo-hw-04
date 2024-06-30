# The begin
def total_salary(path: str) -> tuple[float]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Create a list of information about every employees.
            lines = [line.strip() for line in file.readlines()]
            # Create a list of salaries
            list_of_salaries = [float(line.split(',')[1]) for line in lines]
            # Calculate the total and the average salaries.
            total_amount_of_salary = sum(list_of_salaries)
            average_amount_of_salary = total_amount_of_salary/len(list_of_salaries)
            # Return a tuple of the total and the average salaries.
        return (total_amount_of_salary, average_amount_of_salary)
    except Exception as excpt:
        print(f'Sorry, but {excpt}.')
        return (0,0)
# The end

total, average = total_salary('Task_1/monthly_salaries.txt')
print(f"Total salary: {total}, Average salary: {average:.2f}")