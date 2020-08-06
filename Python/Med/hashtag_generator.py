def generate_hashtag(string):
    split_words = []

    if string == '' or len(string) >= 140:
        return False
    for i in string.split(): # ignores all whitespace
        split_words.append(i.capitalize()) # stores every word in the correct position

    merged = ''.join(split_words)
    return f'#{merged}' # Print was causing that error that I kept having. I feel so dumb.