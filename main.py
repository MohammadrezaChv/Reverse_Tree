import stddraw , math
def Tree(n,x,y,a,bra):
    bend = math.radians(15)
    branch = math.radians(37)
    branchRate = 0.65
    cx = x + math.cos(a) * bra
    cy = y + math.sin(a) * bra
    stddraw.setPenRadius(0.001 * math.pow(n , 1.2))
    stddraw.line(x,y,cx,cy)
    if n == 0:
        return
    Tree(n-1,cx,cy,a+bend-branch,bra * branchRate)
    Tree(n-1,cx,cy,a+bend+branch,bra * branchRate)
    Tree(n-1,cx,cy,a+bend,bra * (1- branchRate))


n = int(input('Please Enter n : '))
Tree(n,0.5,0,math.pi/2,0.3)
stddraw.show()

