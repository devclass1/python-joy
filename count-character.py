def count_characters(filename):
    """
    Counts the number of characters in a file.
    
    Args:
        filename (str): Path to the file to be analyzed
    
    Returns:
        dict: A dictionary with character counts
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Initialize an empty dictionary to store character counts
            char_count = {}
            
            # Count each character
            for char in content:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            
            return char_count
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def display_results(char_count):
    """
    Displays the character count results in a readable format.
    
    Args:
        char_count (dict): Dictionary containing character counts
    """
    if not char_count:
        print("No character counts to display.")
        return
    
    print("\nCharacter Count Results:")
    print("-----------------------")
    print(f"{'Character':<10} {'Count':<10}")
    print("-" * 20)
    
    # Sort characters for better readability
    for char, count in sorted(char_count.items()):
        # Display special characters with their escaped representation
        display_char = repr(char)[1:-1] if char in '\n\t\r' else char
        print(f"{display_char:<10} {count:<10}")
    
    print("\nTotal unique characters:", len(char_count))
    print("Total characters:", sum(char_count.values()))

def main():
    print("File Character Counter")
    print("=====================")
    
    filename = input("Enter the path to the file: ")
    
    # Count characters
    counts = count_characters(filename)
    
    if counts:
        # Display results
        display_results(counts)
        
        # Optional: Save results to a file
        save_option = input("\nWould you like to save the results to a file? (y/n): ").lower()
        if save_option == 'y':
            output_file = input("Enter output filename: ")
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write("Character Count Results:\n")
                    f.write("-----------------------\n")
                    f.write(f"{'Character':<10} {'Count':<10}\n")
                    f.write("-" * 20 + "\n")
                    for char, count in sorted(counts.items()):
                        display_char = repr(char)[1:-1] if char in '\n\t\r' else char
                        f.write(f"{display_char:<10} {count:<10}\n")
                    f.write(f"\nTotal unique characters: {len(counts)}\n")
                    f.write(f"Total characters: {sum(counts.values())}\n")
                print(f"Results saved to {output_file}")
            except Exception as e:
                print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
