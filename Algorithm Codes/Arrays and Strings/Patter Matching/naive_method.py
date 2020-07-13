def naive_matching(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        flag_found = False
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                flag_found = False
                break
            flag_found = True
        if flag_found:
            print(i)

# Alternative: you can use while loop and check if j has become len(pattern) and then break
# then we don't have to use flag

if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    naive_matching(text, pattern)
