class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, nama, prioritas):
        self.queue.append((nama, prioritas))
        print(f"{nama} (prioritas {prioritas}) masuk ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong!")
            return None
        
        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < self.queue[min_index][1]:
                min_index = i
        return self.queue.pop(min_index)

    def is_empty(self):
        return len(self.queue) == 0
    
    def proses_pelayanan(self):
        while not self.is_empty():
            nama, prioritas = self.dequeue()
            print(f"Melayani pasien: {nama} (prioritas {prioritas})")

# Program utama
if __name__ == "__main__":
    antrian = PriorityQueue()
    antrian.enqueue("Budi", 2)
    antrian.enqueue("Siti", 1)
    antrian.enqueue("Andi", 3)
    antrian.proses_pelayanan()