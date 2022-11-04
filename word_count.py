#return count of words for input text
def words_counter(text):
    words = text.split()
    words_count = len(words)
    return words_count

if __name__ == "__main__":
    result = words_counter(input())
    print(result)