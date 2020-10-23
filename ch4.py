import pip._vendor.requests as rq
if __name__ == "__main__":
    num = '12345'
    for k in range(400):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
        r = rq.get(url)
        num = r.text[24:29]
        print(r.text)
