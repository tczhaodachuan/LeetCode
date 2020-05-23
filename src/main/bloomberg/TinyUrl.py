def shortUrl(id):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    url = []
    while id > 0:
        url.append(characters[id % len(characters)])
        id = id / len(characters)

    while len(url) < 6:
        url += characters[0]

    swap(url, 0, len(url) - 1)
    return ''.join(url)


def swap(url, i, j):
    if i >= j:
        return url

    temp = url[i]
    url[i] = url[j]
    url[j] = temp
    return swap(url, i + 1, j - 1)


def generateId(url):
    id = 0
    for char in url:
        id = id * 62 + convert(char)

    return id


def convert(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 10
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 36
    return -1


if __name__ == '__main__':
    tinyUrl = shortUrl(2183918321)
    id = generateId(tinyUrl)

    print tinyUrl, id
