from stats import get_book_text, get_word_count, character_count, sort_dict
import sys
    

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_characters = character_count(text)
    num_characters = sort_dict(num_characters)
    print(f'============ BOOKBOT =============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count-----------')
    print(f'Found {num_words} total words.')
    print(f'----------- Character Count -----------')
    for char, count in num_characters.items():
        print(f'{char}: {count}')
    print(f'============= END ===============')


main()