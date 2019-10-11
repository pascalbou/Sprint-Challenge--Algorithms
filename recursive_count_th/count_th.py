'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    
    l = len(word)

    if l <= 1:
        return 0

    # print(f'word[l-1] {word[l-1]}')
    # print(f'word[l-2] {word[l-2]}')

    if word[l-1] == 'h' and word[l-2] == 't':
        count += 1
    
    word = word[:-1]
    count += count_th(word)

    # print(count)
    return count