def spiralOrder( matrix):
        llx, lly = 0, 0
        array = []
        ydim = len(matrix)
        xdim = len(matrix[0])
        print(xdim)
        print(ydim)
        length=xdim*ydim
        print(length)
        while len(array)<=length:
            for i in range(llx, xdim):
                array.append(matrix[lly][i])
            lly += 1
            if lly==ydim:
                break
            for j in range(lly, ydim):
                # print(j, "in y")
                array.append(matrix[j][xdim - 1])
            xdim -= 1
            if llx==xdim:
                break
            print(ydim, "yyy")
            for k in range(xdim - 1, llx - 1, -1):  # Corrected range
                print(k, "in x")
                array.append(matrix[ydim - 1][k])
            ydim -= 1
            if lly==ydim:
                break
            for l in range(ydim - 1, lly - 1, -1):
                # print(j, "in y")
                array.append(matrix[l][llx])
            llx += 1
            if llx == xdim:
                break
            print (llx ,lly)

        print(array)

spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])