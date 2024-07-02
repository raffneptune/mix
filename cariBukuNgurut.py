def search_books_by_title(books, target_title):
    """
    Mencari semua buku yang judulnya mengandung substring dari target_title.
    Parameters:
    books (list): List buku yang sudah diurutkan berdasarkan judul.
    target_title (str): Substring dari judul buku yang ingin dicari.
    Returns:
    list: List indeks dari buku dalam books yang mengandung target_title.
    """
    result_indices = []
    for i, book in enumerate(books):
        if target_title.lower() in book['title'].lower():
            result_indices.append(i)
    return result_indices

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

library_books = []

def add_books():
    n = int(input("Berapa banyak buku yang ingin Anda tambahkan ke dalam daftar? "))
    for _ in range(n):
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama pengarang: ")
        year = int(input("Masukkan tahun terbit: "))
        library_books.append({"title": title, "author": author, "year": year})
    # Mengurutkan daftar buku berdasarkan judul dan tahun setelah penambahan
    library_books.sort(key=lambda x: (x['title'], x['year']))

def search_book():
    search_method = input("Pilih metode pencarian (judul/tahun): ").strip().lower()
    if search_method == 'judul':
        target_title = input("Masukkan judul buku yang ingin dicari: ")
        result = search_books_by_title(library_books, target_title)
        if result:
            print(f"Buku ditemukan di indeks: {result}\n")
            for idx in result:
                print(f"Detail Buku: {library_books[idx]}")
        else:
            print("\nBuku tidak ditemukan dalam perpustakaan")
    elif search_method == 'tahun':
        target_year = int(input("Masukkan tahun terbit buku yang ingin dicari: "))
        result = binary_search_books_by_year(library_books, target_year)
        if result != -1:
            print(f"Buku ditemukan di indeks: {result}\n")
            print(f"Detail Buku: {library_books[result]}")
        else:
            print("\nBuku tidak ditemukan dalam perpustakaan")
    else:
        print("\nMetode pencarian tidak valid. Silakan pilih antara 'judul' atau 'tahun'.")

def main():
    while True:
        print("\nDaftar buku saat ini:")
        if not library_books:
            print("Belum ada buku yang ditambahkan.")
        else:
            for book in library_books:
                print(f"Judul: {book['title']}, Pengarang: {book['author']}, Tahun: {book['year']}")
        add_more = input("\nApakah Anda ingin menambahkan buku? (ya/tidak): ").strip().lower()
        if add_more == 'ya':
            add_books()
        else:
            if library_books:
                search_more = input("Apakah Anda ingin mencari buku? (ya/tidak): ").strip().lower()
                if search_more == 'ya':
                    search_book()
                else:
                    break
            else:
                print("Tidak ada buku untuk dicari.")
                break
    print("\nProgram selesai.")

main()