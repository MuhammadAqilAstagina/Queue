import os
import queue

class myQueue:
    def __init__(self):
        self.items = queue.Queue()
   
    # Memeriksa apakah queue dalam keadaan kosong
    def isEmpty(self):
        return self.items.empty()
    # Menambah data ke queue
    def enqueue(self, item):
        self.items.put(item)
    # Mengeluarkan data dari queue
    def dequeue(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "empty" 
    # Menghitung panjang queue
    def size(self):
        return self.items.qsize()
   
# Main menu aplikasi

    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("=========================")
            print("|  Menu aplikasi queue  |")
            print("=========================")
            print("1. Put objek")
            print("2. Get objek")
            print("3. Cek Empty")
            print("4. Panjang dari queue")
            print("=========================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("cls")
                obj = str(input("Masukan objek yang ingin anda tambahkan: "))
                self.enqueue(obj)
                print("Object "+obj+" telah ditambahkan")
                x = input("")
            elif(pilihan=="2"):
                os.system("cls")
                temp = self.dequeue()
                if temp != "empty":
                    print("Objek "+temp+" dihapus")
                else:
                    print("Queue kosong")
                x = input("")
            elif(pilihan=="3"):
                os.system("cls")
                print(self.isEmpty())
                x = input("")
            elif(pilihan=="4"):
                os.system("cls")
                print("Panjang dari queue adalah: "+str(self.size()))
                x = input("")
            else:
                pilih="n"  
 
if __name__ == "__main__":
    q=myQueue()
    q.mainmenu()