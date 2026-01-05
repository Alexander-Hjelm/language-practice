import csv

def print_duplicate_lines(file_path):
    """Reads a CSV file, outputs duplicate lines once."""
    unique_lines = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        print("\Duplicate Lines:")
        for row in reader:
            # Output unique lines
            if row in unique_lines:
                print(row)

            unique_lines.append(row)

if __name__ == "__main__":
    csv_file_path = input("Enter the path to your CSV file: ").strip()
    
    try:
        print_duplicate_lines(csv_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
