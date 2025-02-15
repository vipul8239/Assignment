import csv

def read_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

def get_column_widths(data):
    return [max(len(str(item)) for item in col) for col in zip(*data)]

def print_table(data):
    column_widths = get_column_widths(data)
    border = '+'.join('-' * (w + 2) for w in column_widths)
    
    for i, row in enumerate(data):
        print(f"+{border}+")
        print('| ' + ' | '.join(str(item).ljust(width) for item, width in zip(row, column_widths)) + ' |')
    print(f"+{border}+")

def get_recommendation(instance_type, cpu_utilization):
    sizes = ["nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]
    
    family, size = instance_type.split('.')
    if size not in sizes:
        return "Invalid instance type"
    
    index = sizes.index(size)
    
    if cpu_utilization < 20 and index > 0:
        recommended_size = sizes[index - 1]
        status = "Underutilized"
    elif cpu_utilization > 80 and index < len(sizes) - 1:
        recommended_size = sizes[index + 1]
        status = "Overutilized"
    else:
        recommended_size = size
        status = "Optimized"
    
    recommended_instance = f"t3.{recommended_size}" if family.startswith("t2") else f"{family}.{recommended_size}"
    return [["1", instance_type, f"{cpu_utilization}%", status, recommended_instance]]

if __name__ == "__main__":
    instance_type = input("Enter Current EC2 instance type (e.g., t2.large): ")
    cpu_utilization = int(input("Enter CPU utilization percentage: "))
    
    table_data = [["Serial No.", "Current EC2", "Current CPU", "Status", "Recommended EC2"]]
    table_data += get_recommendation(instance_type, cpu_utilization)
    print_table(table_data)
