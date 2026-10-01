def copy_nonempty_lines(source_path: str, target_path: str) -> int:
    count: int = 0

    with open(source_path, 'r') as source_file, open(target_path, 'w') as target_file:

        for line in source_file:
            if line.strip():
                target_file.writelines(line.strip() + '\n')
                count += 1

    return count


my_source_path: str = 'text1.txt'
my_target_path: str = 'text2.txt'

copy_nonempty_lines(my_source_path, my_target_path)
