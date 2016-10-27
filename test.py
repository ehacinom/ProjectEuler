# a copy of dlx

class DLX:
    """DLX data structure"""
    
    PRIMARY = 0 # must be covered
    SECONDARY = 1 # covered at most once
    
    def __init__(self, columns, rows=None, rowNames=None):
        """Init with columns, and row data if provided.
        columns = [(coumnname, 0/1)]
        """
        
        self.nodect = len(columns)+1
        self.U = [i for i in range(self.nodect)]
        self.D = [i for i in range(self.nodect)]
        self.L = [0] * self.nodect
        self.R = list(range(self.nodect))
        self.C = list(range(self.nodect))
        self.S = [0] * self.nodect
        self.N = [colname for (colname,_) in columns] + [None]
        
        print self.U
        print self.D
        print self.L
        print self.R
        print self.C
        print self.S
        print self.N
        
        # ignoring PRIMARY -- that's for crossing tetrasticks
        # L-R link columns
        # process to ensure only PRIMARY columns are linked together
        # link L pointers
        prev = self.nodect-1
        cur = 0
        for cur in range(len(columns)):
            self.L[cur] = prev
            prev = cur
        self.L[self.nodect-1] = prev
        
        # link R nodes
        prev = self.nodect-1
        cur = self.L[prev]
        while cur != self.nodect-1:
            self.R[cur] = prev
            prev = cur
            cur = self.L[cur]
        self.R[self.nodect-1] = prev
        
        print self.U, 'up'
        print self.D, 'down'
        print self.L, 'left'
        print self.R, 'right'
        print self.C, 'c'
        print self.S, 'size'
        print self.N, 'name'
        
        # header index
        self.header = len(columns)
        
        # solution variable
        self.partialsolution = []
        
        # if rows
        if rows: self.appendRows(rows, rowNames)
    
    def appendRows(self, rows, rowNames=None):
        """rows is a matrix, one list for each row
        list contains indicies where 1s appear
        returns list containing row identifiers, the index of first node
        """
        
        rowIdentifiers = []
        if rowNames == None: rowNames = [None] * len(rows)
        for i in range(len(rows)):
            print 'row', rows[i], rowNames[i]
            rowIdentifiers.append(self.appendRow(rows[i], rowNames[i]))
        return rowIdentifiers
    
    def appendRow(self,row, rowName=None):
        first = self.nodect
        prev = self.nodect
        for index in row:
            print 'index', index
            # append data to all lists for the node representing this row
            
            print 'U', self.U
            self.U.append(self.U[index])
            print 'U', self.U
            
            print 'D', self.D
            self.D.append(index)
            self.D[self.U[index]] = self.nodect
            print 'D', self.D
            
            self.U[index] = self.nodect
            print 'U', self.U
            
            self.S[index] += 1
            
            print 'C', self.C
            self.C.append(index)
            print 'C', self.Cc
            
            
        return first





        
if __name__ == '__main__':
    columns = [('a',DLX.PRIMARY), ('b',DLX.PRIMARY), ('c',DLX.PRIMARY), 
               ('d',DLX.SECONDARY), ('e',DLX.PRIMARY)]
    d = DLX(columns)
    rows = [[1,2,4],
            [0,1,3],
            [0],
            [0,1,2,3,4]]
    rowNames = ['row%i' % i for i in range(len(rows))]
    d.appendRows(rows, rowNames)
    for sol in d.solve():
        d.printSolution(sol)