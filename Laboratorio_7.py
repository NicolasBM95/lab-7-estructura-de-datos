#Problema 1 Implementación clase HEAP
class heap:
    def __init__(self, capacity):
        self.A = [0] * capacity
        self.size = 0

    def Parent(self, i):
        return (i-1) // 2
    
    def Left(self,i):
        return 2*(i)+1
    
    def Right(self,i):
        return 2*(i)+2
    
    def MAX_HEAPIFY(self,i):
        l = self.Left(i)
        r = self.Right(i)
        largest = i
        if l < self.size and self.A[l]>self.A[i]:
            largest = l
        else:
            largest = i     
        if r < self.size and self.A[r]>self.A[largest]:
            largest = r
        if largest!=i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.MAX_HEAPIFY(largest)
    
    def BUILD_MAX_HEAP(self,B):
        self.size = len(B)
        self.A = B
        for i in range(self.size // 2 - 1, -1, -1):
            self.MAX_HEAPIFY(i)
    
    def HEAPSORT(self):
        self.BUILD_MAX_HEAP(self.A)
        for i in range(self.size -1, 0, -1):
            temp = self.A[i]
            self.A[0], self.A[i] = self.A[i], self.A[0]     
            self.size -=1
            self.MAX_HEAPIFY(0) 

#Problema 2 Implementación clase Priority Queue
class Priority_Queue:
    def __init__(self, capacity):
        self.heap = heap(capacity)
    
    def MAX_HEAP_INSERT(self,k):
        if self.heap.size == len(self.heap.A):
            raise Exception("Heap overflow")
        self.heap.size += 1
        i = self.heap.size - 1
        self.heap.A[i] = k
        while i > 0 and self.heap.A[self.heap.Parent(i)] < self.heap.A[i]:
            self.heap.A[i], self.heap.A[self.heap.Parent(i)] = self.heap.A[self.heap.Parent(i)], self.heap.A[i]
            i = self.heap.Parent(i)

    def HEAP_EXTRACT_MAX(self):
        if self.heap.size < 1:
            raise Exception("Heap underflow")
        max1 = self.heap.A[0]
        self.heap.A[0] = self.heap.A[self.heap.size - 1]
        self.heap.size -= 1
        self.heap.MAX_HEAPIFY(0)
        return max1
    
    def HEAP_MAXIMUM(self):
        if self.heap.size > 0:
            return self.heap.A[0]
        return None

#Problema 3 Uso de las clases HEAP y PrioriryQueue
import random
random_array = [random.randint(1, 100) for _ in range(20)]

#Prueba del HEAP
print("Probando HEAP")
#Aqui probamos el build y el heapify
heap1 = heap(len(random_array))
heap1.BUILD_MAX_HEAP(random_array)
print("Heap construido:", heap1.A)
#Aqui probamos el sort
heap1.HEAPSORT()
print("Arreglo ordenado:", heap1.A)

#Prueba de PriorityQueue
print("\nProbando PriorityQueue")
#Se construye la cola usando max heap insert en todo el random array, asi probando el insert
pq = Priority_Queue(len(random_array))
for num in random_array:
    pq.MAX_HEAP_INSERT(num)
#Se prueba el heap maximum
print("Valor máximo:", pq.HEAP_MAXIMUM())
#Finalmente se imprime una lista con los elementos extraidos con heap extract max que en un principio fueron agregados con max heap insert, asi comprobando el funcionamiento del extract y del insert
sorted_priority_queue = []
while pq.heap.size > 0:
    sorted_priority_queue.append(pq.HEAP_EXTRACT_MAX())
print("Elementos extraídos en orden descendente:", sorted_priority_queue)