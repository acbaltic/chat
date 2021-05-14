
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  # 讀取中文要指定'utf-8'，再用'-sig'去掉檔案紀錄開始處的'\ufeff'
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'  # 代表現在說話的人
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue

        if person:  # 如果 person 有值的話，則...
            new.append(person + ':' + line)  # 關鍵/用法：continue
    return new


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)




if __name__ == '__main__':
    main()


