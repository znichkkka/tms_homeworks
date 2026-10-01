from collections import Counter

def find_most_common_word(source_path: str, target_path: str) -> None:
    with open(source_path, 'r') as source_file, open(target_path, 'a') as target_file:

        for line in source_file:
            words: list[str] = line.split()
            words_counter: Counter[str] = Counter(words)

            most_common_word, amount = words_counter.most_common(1)[0]

            target_file.write(most_common_word + ' - ' + str(amount) + '\n')


find_most_common_word('some_words.txt', 'count_words.txt')
