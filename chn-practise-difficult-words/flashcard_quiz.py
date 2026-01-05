import csv
from random import shuffle

def load_words_from_csv(file_path):
    """Load words from a CSV file."""
    words = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the CSV format is: Simplified, Traditional, Pinyin, English, Tags
            simplified, traditional, pinyin, english, tags = row
            words.append({
                "simplified": simplified,
                "traditional": traditional,
                "pinyin": pinyin,
                "english": english
            })
    return words

def flashcard_quiz(words):
    """Run the flashcard quiz."""
    original_words_len = len(words)
    counter = 0
    while words:
        print(f"Words left this session: {len(words)}/{original_words_len}, total cards: {counter}")

        counter += 1

        word = words[0]  # Get the first word in the list
        print(f"\nMandarin: {word['simplified']}")
        
        # Wait for the user to press Enter to reveal the answer
        input("Press Enter to reveal the pinyin and meaning...")
        print(f"Pinyin: {word['pinyin']}")
        print(f"Meaning: {word['english']}")
        
        # Ask if the user remembered the word successfully
        remembered = input("Did you remember this word? (yes/no): ").strip().lower()
        if remembered in ["yes", "y"]:
            words.pop(0)  # Remove the word from the list if remembered
        else:
            words.append(words.pop(0))  # Move the word to the end of the list

    print("\nCongratulations! You have completed the quiz.")

if __name__ == "__main__":
    #Path to the CSV file
    csv_file_path = input("Enter the path to your CSV file: ").strip()
    #csv_file_path = "words.csv"
    
    try:
        words = load_words_from_csv(csv_file_path)
        shuffle(words)
        if not words:
            print("No words found in the file. Please check the file content.")
        else:
            print("Starting the flashcard quiz!")
            flashcard_quiz(words)
    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
