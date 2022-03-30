class Array_seq:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0

    def __len__(self): return self.size # O(1)
    def __iter__(self): yield from self.A # O(n)

    def build(self, X): # O(n)
        self.A = [x for x in X]
        self.size = len(self.A)

    def get_at(self, i): return self.A[i] # O(1)
    
    def set_at(self, i, x): # O(1)
        self.A[i] = x

    def __copy_forward(self, i, n, A, j): # O(1n)
        for k in range(n):
            A[j + k] = self.A[i + k]

    def __copy_backward(self, i, n, A, j): # O(n)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    # self.A = [1,2,3,4,5] i=2
    def insert_at(self,i, x): # O(n)
        n = len(self)
        A = [None] * (n + 1)
        self.__copy_forward(0, i, A, 0)
        A[i] = x
        self.__copy_forward(i, n - 1, A, i + 1)
        self.build(A)

    # self.A = [1,2,3,4,5] i=2
    def delete_at(self, i): # O(n)
        n = len(self)
        A = [None] * (n - 1)
        self.__copy_forward(0, i, A, 0)
        x = self.A[i]
        self.__copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self.A), x)
    def delete_last(self): self.delete_at(len(self.A) - 1)


newa = Array_seq()
newa.build([1,2,3,4])

for q in newa:
    print(q)