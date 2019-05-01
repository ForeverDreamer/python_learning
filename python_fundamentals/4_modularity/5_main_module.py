from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words


def print_words(words):
    print(words)


def main():
    words = fetch_words()
    print_words(words)


if __name__ == '__main__':
    main()
