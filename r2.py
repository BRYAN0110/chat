#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#計算字數
def count(lines):
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_photo_count = 0
    Viki_word_count = 0
    Viki_sticker_count = 0
    Viki_photo_count = 0

    for line in lines:
        s = line.split(' ')
        if s[1] == 'Allen':
            for m in s[2:]:
                if m == '貼圖':
                    Allen_sticker_count += 1
                    continue
                elif m == '圖片':
                    Allen_photo_count += 1
                    continue
                Allen_word_count += len(m)

        elif s[1] == 'Viki':
            for m in s[2:]:
                if m == '貼圖':
                    Viki_sticker_count += 1
                    continue
                elif m == '圖片':
                    Viki_photo_count += 1
                    continue
                Viki_word_count += len(m)

    print('Allen說了多少字: ' , Allen_word_count)
    print('Allen傳了多少貼圖: ' , Allen_sticker_count)
    print('Allen傳了多少圖片: ' , Allen_photo_count)
    print('Viki說了多少字: ' , Viki_word_count)
    print('Viki傳了多少貼圖: ' , Viki_sticker_count)
    print('Viki傳了多少圖片: ' , Viki_photo_count)


#main_function
def main_function(filename):
    lines = read_file(filename)
    count(lines)

main_function('LINE-Viki.txt')
    