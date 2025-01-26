def sequential_search(arr, target):
    """
    Melakukan sequential search pada array.
    Parameters:
    arr (list): List yang berisi elemen-elemen yang akan dicari.
    target (int/float/str): Elemen yang ingin dicari.
    Returns:
    int: Indeks dari target dalam arr jika ditemukan, selain itu -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

items = [34, 7, 23, 32, 5, 62]

def add_elements():
    n = int(input("\nBerapa banyak elemen yang ingin Anda tambahkan ke dalam daftar? "))
    for _ in range(n):
        new_item = int(input("\nMasukkan elemen baru: "))
        items.append(new_item)

def search_element():
    target_item = int(input("Masukkan elemen yang ingin dicari: "))
    result = sequential_search(items, target_item)
    if result != -1:
        print(f"\nElemen ditemukan di indeks: {result}")
    else:
        print("\nElemen tidak ditemukan dalam daftar")

def main():
    while True:
        print("\nDaftar elemen saat ini:", items)
        search_element()
        add_more = input("\nApakah Anda ingin menambahkan elemen lagi? (ya/tidak): ").strip().lower()
        if add_more == 'ya':
            add_elements()
        else:
            search_more = input("\nApakah Anda ingin mencari elemen lagi? (ya/tidak): ").strip().lower()
            if search_more != 'ya':
                break
    print("\nProgram selesai.")

main()