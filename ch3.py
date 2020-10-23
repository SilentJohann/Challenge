import pip._vendor.requests as rq
if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    r = rq.get(url)
    raw = r.text
    start = raw.find('!')
    msg = raw[start:-5].rstrip("\n")

    res = ''
    
    for i in range(len(msg)):
        if msg[i].islower() and msg[i-3:i+4].isalpha():
            if msg[i-4].islower() and msg[i-3:i].isupper() and msg[i+1:i+4].isupper() and msg[i+4].islower():
                res += msg[i-4:i+5]+"\n"
    print(res)

