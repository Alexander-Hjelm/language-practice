import csv
from collections import Counter

def count_mandarin_characters(file_path):
    """Count the frequency of individual Mandarin characters from the first column of a CSV file."""
    character_counts = Counter()
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure the row is not empty
                simplified = row[0]  # Extract the first column (Simplified Chinese)
                character_counts.update(simplified)  # Count each character individually

    # Sort characters by frequency (highest first)
    sorted_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print the results
    print("\nCharacter Frequency Count:")
    i = 1
    for char, count in sorted_characters:
        print(f"{i}: {char}: {count}")
        i = i + 1

if __name__ == "__main__":
    csv_file_path = input("Enter the path to your CSV file: ").strip()
    
    try:
        count_mandarin_characters(csv_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
