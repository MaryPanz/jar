class Jar:
    
    def __init__(self, capacity = 12, size = 0):
        if capacity < 0:
           raise ValueError
        self._capacity = capacity
        self._size = size

    def __str__(self):
        if self._size == 0:
            return("")
        else:
            return(self._size * "🍪")

    def deposit(self, n):
        self._size = self._size + n
        if self._size > self._capacity:
            raise ValueError
        else:
            return self._size

    def withdraw(self, n):
        if n > self._capacity:
            raise ValueError
        if n > self._size:
            raise ValueError
        else:
            self._size = self._size - n
            return self._size

    # capacity cannot be changed
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size




#c = Jar()
#c.deposit(8)
#c.withdraw(15)
#print(c.__str__())
