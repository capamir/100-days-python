print('wellcome to love calculator')
name1 = input('what is your name? ')
name2 = input('what is his/her name? ')
combined_string = name1.lower() + ' ' + name2.lower()

TRUE_LOVE = {'t': 0, 'r': 0, 'u': 0, 'e': 0, 'l': 0, 'o': 0, 'v': 0}

for ch in TRUE_LOVE:
    TRUE_LOVE[ch] += combined_string.count(ch)

true = 0
love = 0
true_string = 'true'
love_string = 'love'

for ch in true_string:
    true += TRUE_LOVE[ch]

for ch in love_string:
    love += TRUE_LOVE[ch]

love_score = true*10 + love

# print(love_score)
if love_score < 10 or love_score > 90:
    print(f'your love score is {love_score}. you go together like coke and mentos')
elif 40 <= love_score < 50:
    print(f'your love score is {love_score}. you are alright together')
else:
    print(f'your love score is {love_score}.')
