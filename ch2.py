import pip._vendor.requests as rq
if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    r = rq.get(url)
    raw = r.text
    start = raw.find('%')
    msg = raw[start:-5]

    res = ''

    for i in range(len(msg)):
        if msg[i].isalpha():
            res += msg[i]
    print(res)
