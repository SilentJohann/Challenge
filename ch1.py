if __name__ == "__main__":
    alphabet    =   "abcdefghijklmnopqrstuvwxyzab"
    txt         =   "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "\
                    +"bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "\
                    +"sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    txt         = "map"
    new_txt     =   ""

    for k in range(len(txt)):
        if not txt[k].isalpha():
            new_txt += txt[k]
            next
        else:
            new_txt += alphabet[alphabet.find(txt[k])+2]
    
    print(new_txt)