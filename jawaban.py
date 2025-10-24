class PrinterQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, dokumen, waktu):
        self.queue.append((dokumen, waktu))
        print(f"{dokumen} ditambahkan ke antrian ({waktu} detik).")
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Antrian kosong!")
            return None
    def is_empty(self):
        return len(self.queue) == 0
    def proses_cetak(self):
        total = 0
        while not self.is_empty():
            dokumen, waktu = self.dequeue()
            print(f"Mencetak: {dokumen} ({waktu} detik)")
            total += waktu
        print(f"Total waktu pencetakan: {total} detik")
# Program utama
if __name__ == "__main__":
    printer = PrinterQueue()
    printer.enqueue("Tugas1.pdf", 5)
    printer.enqueue("Laporan.docx", 3)
    printer.enqueue("Foto.png", 2)
    printer.proses_cetak()