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

if __name__ == "__main__":
    file_path = input("Enter CSV file path: ")
    data = read_csv(file_path)
    print_table(data)
