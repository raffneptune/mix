def binary_search_books_by_title(books, target_title):
    """
    Melakukan binary search pada daftar buku yang diurutkan berdasarkan judul.
    Parameters:
    books (list): List buku yang sudah diurutkan berdasarkan judul.
    target_title (str): Judul buku yang ingin dicari.
    Returns:
    int: Indeks dari buku dalam books jika ditemukan, selain itu -1.
    """
    left, right = 0, len(books) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Membandingkan judul buku di tengah dengan target
        if books[mid]['title'].lower() == target_title.lower():
            return mid
        # Jika judul target lebih besar, abaikan setengah kiri
        elif books[mid]['title'].lower() < target_title.lower():
            left = mid + 1
        # Jika judul target lebih kecil, abaikan setengah kanan
        else:
            right = mid - 1
    # Jika judul target tidak ditemukan
    return -1

def binary_search_books_by_year(books, target_year):
    """
    Melakukan binary search pada daftar buku yang diurutkan berdasarkan tahun terbit.
    Parameters:
    books (list): List buku yang sudah diurutkan berdasarkan tahun terbit.
    target_year (int): Tahun terbit buku yang ingin dicari.
    Returns:
    int: Indeks dari buku dalam books jika ditemukan, selain itu -1.
    """
    left, right = 0, len(books) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Membandingkan tahun terbit buku di tengah dengan target
        if books[mid]['year'] == target_year:
            return mid
        # Jika tahun target lebih besar, abaikan setengah kiri
        elif books[mid]['year'] < target_year:
            left = mid + 1
        # Jika tahun target lebih kecil, abaikan setengah kanan
        else:
            right = mid - 1
    # Jika tahun target tidak ditemukan
    return -1

library_books = [
    {"title": "Buku Langit", "author": "Alterego Banana", "year": 2019},
    {"title": "Buku Bumi", "author": "Onic Buts", "year": 2020},
    {"title": "Buku Matahari", "author": "Evos Branz", "year": 2021},
    {"title": "Buku Angin", "author": "Btr Bottle", "year": 2022},
    {"title": "Buku Awan", "author": "Rrq Banana", "year": 2023}
]

def add_books():
    n = int(input("\nBerapa banyak buku yang ingin Anda tambahkan ke dalam daftar? "))
    for _ in range(n):
        title = input("\nMasukkan judul buku: ")
        author = input("\nMasukkan nama pengarang: ")
        year = int(input("\nMasukkan tahun terbit: "))
        library_books.append({"title": title, "author": author, "year": year})
    # Mengurutkan daftar buku berdasarkan judul dan tahun setelah penambahan
    library_books.sort(key=lambda x: x['title'])
    library_books.sort(key=lambda x: x['year'])

def search_book():
    search_method = input("\nPilih metode pencarian (judul/tahun): ").strip().lower()
    if search_method == 'judul':
        target_title = input("\nMasukkan judul buku yang ingin dicari: ")
        result = binary_search_books_by_title(library_books, target_title)
        if result != -1:
            print(f"\nBuku ditemukan di indeks: {result}")
            print(f"\nDetail Buku: {library_books[result]}")
        else:
            print("\nBuku tidak ditemukan dalam perpustakaan")
    elif search_method == 'tahun':
        target_year = int(input("\nMasukkan tahun terbit buku yang ingin dicari: "))
        result = binary_search_books_by_year(library_books, target_year)
        if result != -1:
            print(f"\nBuku ditemukan di indeks: {result}")
            print(f"\nDetail Buku: {library_books[result]}")
        else:
            print("\nBuku tidak ditemukan dalam perpustakaan")
    else:
        print("\nMetode pencarian tidak valid. Silakan pilih antara 'judul' atau 'tahun'.")

def main():
    while True:
        print("\nDaftar buku saat ini:")
        for book in library_books:
            print(f"Judul: {book['title']}, Pengarang: {book['author']}, Tahun: {book['year']}")
        search_book()
        add_more = input("\nApakah Anda ingin menambahkan buku lagi? (ya/tidak): ").strip().lower()
        if add_more == 'ya':
            add_books()
        else:
            search_more = input("\nApakah Anda ingin mencari buku lagi? (ya/tidak): ").strip().lower()
            if search_more != 'ya':
                break
    print("\nProgram selesai.")

main()