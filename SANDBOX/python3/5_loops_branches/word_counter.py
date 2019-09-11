# book list
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby',
              'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

title_counter = {}

for title in book_title:
    if title not in title_counter:
        title_counter[title] = 1
    else:
        title_counter[title] += 1

print(title_counter)


