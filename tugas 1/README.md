## Tugas 1 Pemrograman Jaringan

Nama  : Bayu Laksana<br>
NRP   : 05111740000020<br>
Kelas : B

### Jalankan program server.py di 3 port yang berbeda (31000, 31001, 31002).

Server berjalan pada tiga port.

- Server port 31000

    ![](img/Ss1x.png)

- Server port 31001

    ![](img/Ss2x.png)

- Server port 31002

    ![](img/Ss3x.png)


### Jalankan program client.py untuk konek ke server yang jalan pada poin sebelumnya dan mengirimkan string “JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA”.

- Client mengirim ke server port 31000

    ![](img/client31000.png)

- Client mengirim ke server port 31001

    ![](img/client31001.png)

- Client mengirim ke server port 31002

    ![](img/client31002.png)

- Server merespon dari client

    ![](img/server31000.png)

    ![](img/server31001.png)

    ![](img/server31002.png)


### Jalankan program server.py di 3 port yang berbeda di 2 komputer yang berbeda.

- IP komputer 1 adalah `10.151.254.205`. Server dijalankan pada 3 port yang berbeda.

    + Server port 31000

        ![](img/Ss1x.png)

    + Server port 31001

        ![](img/Ss2x.png)

    + Server port 31002

        ![](img/Ss3x.png)

- IP komputer 2 adalah `10.151.62.227`. Server dijalankan pada 3 port yang berbeda.

    + Server port 31000

        ![](img/server31000zaldi.png)

    + Server port 31001

        ![](img/server31001zaldi.png)

    + Server port 31002

        ![](img/server31002zaldi.png)

### Jalankan program client.py untuk konek ke server pada poin sebelumnya, kirimkan string yang sama.

- Hasil client mengirim dari komputer 1 menuju komputer 2 pada port 31000, 31001, dan 31002.

    ![](img/clientzaldi31000.png)

    ![](img/clientzaldi31001.png)

    ![](img/clientzaldi31002.png)

### Jalankan program server.py di 2 komputer yang berbeda, masing-masing 2 server di port yang berbeda.

Soal ini memiliki karakteristik yang sama dengan soal [ini](#jalankan-program-serverpy-di-3-port-yang-berbeda-di-2-komputer-yang-berbeda). Hanya saja dijalankan menggunakan 2 port.

----

1. ### MODIFIKASILAH program `client.py` dan `server.py` agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a).

    [**Program `server.py` dapat dilihat disini >**](tugas1a/server.py)

    Ketika program `server.py` dijalankan, maka server akan menunggu hingga ada koneksi yang datang.

    ![](img/Ss1.png)

    [**Program `client.py` dapat dilihat disini >**](tugas1a/client.py)

    Kemudian, client mengirimkan file yang diinginkan ke server. File yang ditransfer dari client adalah file [**test_client.pdf**](tugas1a/test_client.pdf) yang kemudian server akan menyimpannya pada folder [**server**](tugas1a/server)

    ![](img/Ss2.png)

    Dan server akan merespon seperti pada gambar berikut.

    ![](img/Ss3.png)

    - File yang dikirim

        ![](img/fileto1a.png)

    - File yang diterima

        ![](img/filerecev1a.png)

2. ### MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b).

    [**Program `server.py` dapat dilihat disini >**](tugas1b/server.py)

    Program `server.py` dijalankan dan server akan menunggu koneksi yang datang.

    ![](img/S2-1.png)

    [**Program `client.py` dapat dilihat disini >**](tugas1b/client.py)

    Program `client.py` kemudian dijalankan untuk menerima input dan request file. File yang diminta misalkan adalah file [**test_request.pdf**](tugas1b/test_request.pdf).

    ![](img/S2-2.png)

    Kemudian, server akan merespon dan mengirimkan file yang dimaksud.

    ![](img/S2-3.png)

    Client merepson bahwa file telah diterima dan nantinya akan disimpan dengan nama "test_result.pdf" sebagai penanda bahwa file telah diterima.

    ![](img/S2-4.png)

    - File yang direquest oleh client

        ![](img/filerequested1b.png)

    - File yang diterima client

        ![](img/filerecev1b.png)