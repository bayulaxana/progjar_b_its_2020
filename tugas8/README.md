## Tugas 8 Pemrograman Jaringan

Nama  : Bayu Laksana<br>
NRP   : 05111740000020<br>
Kelas : B

----

## Menjalankan Program Sebelum Modifikasi

Bukalah browser arahkan ke http://127.0.0.1:10002/sending.html , isilah dengan sesuatu dan kirim.

- Membuka http://127.0.0.1:10002/sending.html

    ![](img/img-1.jpg)

- Hasil setelah menekan 'kirim'

    ![](img/img-2.jpg)

    > Akan keluar hasil berupa string `kosong`

## Modifikasi Program

### Instruksi

**Modifikasilah agar server dapat membalas dengan isi:**

- Semua header yang dikirim dari browser,
- Yang anda isikan di form pada saat mengisi pada poin nomor 5, misalkan mengisi “ISILAH” maka server akan mereply dengan “ISILAH” juga , dan bukan ‘kosong’.

### Hasil

*Program modifikasi dapat dilihat pada file [http.py](http.py) dan [server_thread_http.py](server_thread_http.py)*

- Membuka http://127.0.0.1:10002/sending.html dan mengisikan form dengan sebuah string, contohnya disini adalah **`BayuLaksana`**.

    ![](img/img-3.jpg)

- Hasil setelah menekan 'kirim'

    ![](img/img-4.jpg)

    > Konten kotak oranye bagian atas adalah isi **header request dari browser**. Sedangkan bagian bawah merupakan **isi dari form** yang dikirim.

    
    ![](img/img-5.jpg)
