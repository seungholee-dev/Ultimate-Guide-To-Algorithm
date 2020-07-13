def preprocessLPS(pattern):
    M = len(pattern)
    lps = [0] * M

    i = 1 # faster pointer
    j = 0 # slower pointer

    # We want to end the loop when we fill all the lps (when i == m)
    while i < M:
        if pattern[j] == pattern[i]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
    return lps

# Function for the actual algorithm of searching matches.
def kmp_searching(text, pattern):   
    i, j = 0, 0

    lps = preprocessLPS(pattern)
    
    while i < len(text):
        if text[i] == pattern[j]:
            j += 1
            i += 1

            # Match found!
            if j == len(pattern):
                print(i - j) # i - j to return start of the index
                j = lps[j - 1] # prepare for the next match look up but we are still gonna utilize the suffix, prefix hack.
                                # So to speak, we are setting j to the point where we are gonna start comparing again with i (that moved on).
        else:
            if j == 0: # you can't subtract from j anymore so move i to compare with new text[i]
                i += 1
            else:
                j = lps[j - 1] # j will be moved to the +1 index of the former suffix. Because that's where you start comparing with text[i] again.

if __name__ == "__main__":
    print("###### Preprocessing Test ######")
    print("AABAACAABAA", ":", preprocessLPS("AABAACAABAA") )
    print("AAAAA", ":", preprocessLPS("AAAAA") )
    print("AAABAAA", ":", preprocessLPS("AAABAAA") )
    print("ABAABAB", ":", preprocessLPS("ABAABAB") )

    
    print("###### KMP Searching Test ######")
    kmp_searching("AABAACAABAA", "AAB")
    print()
    kmp_searching("AABAACAABAA", "AC")
    