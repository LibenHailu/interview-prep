def solution(word):
    # change it to lower
    # change it to set
    # check if len == 26
    lower = word.lower()
    return "YES" if len(set(lower)) == 26 else "NO"

if __name__ == "__main__":
    q = input()
    print(solution(input()))


# solution("TheQuickBrownFoxJumpsOverTheLazyDog")
