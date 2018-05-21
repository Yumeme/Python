# 00.py
# reverse order of character string
# Make the letters of the  string "GitHub" from the end to the beginning.

str = "yumeme"          # "str" はどんな文字で置き換えてもok
print(str[::-1])        # 同じ名前の変数を使えば良い
 

# スライスについて
'''
str = "abcdefgh"

# Get specific letter
str[0]        # 'a'の先頭からzero-based
str[-1]       # 'h'，負の数でも指定可能（文末から遡っていく）今回はstr[7]と同義

# スライス
str[1:3]      # 'bc'，終了インデックスの文字は含まないので注意．文字数とかでもない
str[0:-3]     # 'abcde'，負の数でもOK．今回ではstr[0:5]と同義
str[:4]       # 'abcd'，開始インデックスを省略した場合は最初から
str[4:]       # 'efgh'，終了インデックスを省略した場合は最後まで

# ステップ数指定
str[0:6:2]    # 'ace'，ステップ数で指定した分，飛び飛びの文字を取得（0,2,4番目）
str[::3]      # 'adg'，省略も可能
str[-3::2]    # 'fh'，負の数も可能
str[::-3]     # 'hed'，ステップ数を負の数にすると逆順に遡っていく

'''
