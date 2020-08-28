# write a function called most_characters that accepts 
# a string, and return the character that appears the most.
# so most_characters("abcda") should return "a".


#solutions
def most_characters(a):
    result = {}

    for number in a:
      if number in result.keys():
        result[number] += 1
      else:
        result[number] = 1
    final = max(result, key=result.get).lower()

    print(final)


most_characters('abAdA')


