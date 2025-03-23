import sys
from stats import print_stats_report


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    content = sys.argv[1]
    print_stats_report(content)

main()