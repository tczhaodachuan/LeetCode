def compress(input_string):
    # edge case
    if len(input_string) < 2:
        return input_string
    if len(input_string) == 2:
        if input_string[0] == input_string[1]:
            return input_string[0] + '2'
        else:
            return input_string

    for i in range(len(input_string)):
        # point the compression position to the next character
        compression = i + 1
        while compression < len(input_string) and input_string[compression] == input_string[i]:
            # find all repeated characters
            compression += 1
        if compression > i + 1:
            input_string = input_string[:i + 1] + str(compression - i) + input_string[compression:]
    return input_string