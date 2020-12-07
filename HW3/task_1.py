zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

better_counter = zen.count('better')
never_counter = zen.count('never')
is_counter = zen.count('is')
upper_zen = zen.upper()
zen_replace = zen.replace('i', '&')

print (f"""The word "better" are {better_counter} times in Zen of Python. \t
The word "never" are {never_counter} times in Zen of Python. \t
The word "is" are {is_counter} times in Zen of Python.\n""")
print (upper_zen, '\n')
print (zen_replace)