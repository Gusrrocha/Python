data1 = str(input("Insira a 1º data (dd/mm/yyyy): "))
data2 = str(input("Insira a 2º data (dd/mm/yyyy): "))
fdata1 = data1.split('/')
fdata2 = data2.split('/')
d1, m1, y1 = int(fdata1[0]), int(fdata1[1]), int(fdata1[2])
d2, m2, y2 = int(fdata2[0]), int(fdata2[1]), int(fdata2[2])
dif = y2-y1
dy = 365.23*dif
if d2 > d1:
    dif3 = d2-d1
    if m2 > m1:
        dif2 = m2-m1
        dy3 = dy+(365/12)*dif2
        dy3 += dif3
        print(int(dy3), "dias de diferença!")
    elif m2 == m1:
        print(int(dy+dif3),"dias de diferença!")
    elif m2 < m1:
        dif2 = m1-m2
        dy2 = dy-(365/12)*dif2
        dy2 += dif3
        print(int(dy2),"dias de diferença!")

elif d1 > d2:
    dif3 = d1-d2
    if m2 > m1:
        dif2 = m2-m1
        dy3 = dy+(365/12)*dif2
        dy3 -= dif3
        print(int(dy3), "dias de diferença!")
    elif m2 == m1:
        print(int(dy-dif3),"dias de diferença!")
    elif m2 < m1:
        dif2 = m1-m2
        dy2 = dy-(365/12)*dif2
        dy2 -= dif3
        print(int(dy2),"dias de diferença!")

elif d1 == d2:
    if m2 > m1:
        dif2 = m2-m1
        dy3 = dy+(365/12)*dif2
        print(int(dy3), "dias de diferença!")
    elif m2 == m1:
        print(int(dy),"dias de diferença!")
    elif m2 < m1:
        dif2 = m1-m2
        dy2 = dy-(365/12)*dif2
        print(int(dy2),"dias de diferença!")


