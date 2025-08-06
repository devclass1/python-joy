def compare_files():
    # Get filenames from user
    filename1 = input("Enter first filename: ")
    filename2 = input("Enter second filename: ")

    try:
        # Read both files
        with open(filename1, 'r') as f1, open(filename2, 'r') as f2:
            file1_content = f1.read()
            file2_content = f2.read()

        print(f"\nComparing '{filename1}' and '{filename2}':")

        # Character-level comparison
        print("\nCharacter differences:")
        found_char_diff = False
        min_length = min(len(file1_content), len(file2_content))
        
        for i in range(min_length):
            if file1_content[i] != file2_content[i]:
                print(f"Position {i}: '{file1_content[i]}' → '{file2_content[i]}'")
                found_char_diff = True
        
        if not found_char_diff and len(file1_content) == len(file2_content):
            print("No character differences found!")
        elif not found_char_diff:
            print("No character differences in overlapping portion!")

        # Word-level comparison
        print("\nWord differences:")
        words1 = file1_content.split()
        words2 = file2_content.split()
        found_word_diff = False
        min_word_count = min(len(words1), len(words2))
        
        for i in range(min_word_count):
            if words1[i] != words2[i]:
                print(f"Word {i+1}: '{words1[i]}' → '{words2[i]}'")
                found_word_diff = True
        
        if not found_word_diff and len(words1) == len(words2):
            print("No word differences found!")
        elif not found_word_diff:
            print("No word differences in overlapping portion!")

        # Length differences
        if len(file1_content) != len(file2_content):
            print(f"\nFile length difference: {filename1} has {len(file1_content)} characters, {filename2} has {len(file2_content)} characters")
        
        if len(words1) != len(words2):
            print(f"Word count difference: {filename1} has {len(words1)} words, {filename2} has {len(words2)} words")

    except FileNotFoundError as e:
        print(f"\nError: {e}")

# Run the comparison
compare_files()
