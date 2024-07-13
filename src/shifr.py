alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТ\ЬОГ>ШЩДЛБЮЖЗХЭЪjklm/nopqr stuvwxy'z1234567)89_йф0ячыц<увсмипакен|ртогшлб,юдщьзжэхъ*-+=&:;?!@"


def sh(text, alf=alf, key=2):
    cezar_shifr = []
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                # if text[j]==" ":
                # text[j]=='|he|re_|prob|el'
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_shifr.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_shifr.append(alf[i + key])

    return ''.join(cezar_shifr)


def unsh(text, alf=alf, key=2):
    cezar_un = []
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if alf[i] == text[j]:
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_un.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])

    return ''.join(cezar_un)


"""
def dcc(alf):
    dc={}
    for i in range(len(alf)):
        dc[alf[i]]="1"*i
    dc["Q"]="LEN"
    return dc
"""

def unshifr_brutforce(text,key=10,alf=alf):
    rs=[]
    res=""
    for p in range(key):
        for j in range(len(text)):
            for i in range(len(alf)):
                # print(i,j)
                if alf[i] == text[j]:
                    if i + p > len(alf)-1:
                        # print("          ",i,j)
                        res+=text[j]
                    else:
                        # print("                          ",i,j)
                        res+=alf[i - p]
        rs.append(res)
        rs.append(str(p))
        res=""
    return rs

    
# a=sh("Words")
# b=unshifr_brutforce(a,key=12)
# print(b)