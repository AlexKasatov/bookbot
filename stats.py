CONTENT = './books/frankenstein.txt'

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_book_words_numbs(content):
    num_words = len(content.split())
    return f"Found {num_words} total words"

def get_symbols():
    content = get_book_text(CONTENT).split()

    words_count = {}

    for word in content:
        for s in word:
            symbol = s.lower()
            if symbol not in words_count:
                words_count[symbol] = 0
            words_count[symbol] += 1

    return words_count

def sort_words():
    def sort_on(dict_arg):
        return dict_arg["num"]

    alpha_symbols = {k: v for k, v in get_symbols().items() if k.isalpha()}
    arr = [{'symbol': key, 'num': value } for key, value in alpha_symbols.items()]
    arr.sort(reverse=True, key=sort_on)

    return arr


def print_stats_report(content):
    sorted_words = sort_words()

    first_line = "============ BOOKBOT ============"
    first_line_title = f"Analyzing book found at {content}..."
    second_line = "----------- Word Count ----------"
    second_line_title = get_book_words_numbs(get_book_text(content))
    char_title = "--------- Character Count -------"

    print(f"{first_line}\n{first_line_title}\n{second_line}\n{second_line_title}\n{char_title}")

    for i in sorted_words:
        print(f"{i['symbol']}: {i['num']}")

sort_words()