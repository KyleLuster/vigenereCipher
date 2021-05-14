def encode(key, text):
    encode = []
    for i in range(0, len(text)):
        if text[i] == ' ':
          encode.append(' ')
          i+=1
        elif text[i] != ' ':
            s = (ord(text[i]) + ord(key[i])) % 26
            s += ord('A')
            encode.append(chr(s))
    return("".join(encode))

def decode(key, encoded):
    decode = []
    for i in range(0, len(encoded)):
        if encoded[i] == ' ':
          decode.append(' ')
          i+=1
        elif encoded[i] != ' ':
            s = (ord(encoded[i]) - ord(key[i]) +26) % 26
            s += ord('A')
            decode.append(chr(s))
    return("".join(decode))

text = "HYPOSTATIC UNION IS COOL"
key = "FILIOQUEFILIOQUEFILIOQUEFILIOQUE"
print("Original Text: " + text)
print("Encoded Text: " + encode(key, text))
encode = encode(key, text)
print("Decoded Text: " + decode(key, encode))
