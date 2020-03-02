## Tugas 1 Pemrograman Jaringan

Nama  : Bayu Laksana<br>
NRP   : 05111740000020<br>
Kelas : B



----

1. MODIFIKASILAH program `client.py` dan `server.py` agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a).

    [**Program `server.py` dapat dilihat disini >**](tugas1a/server.py)

    Ketika program `server.py` dijalankan, maka server akan menunggu hingga ada koneksi yang datang.

    ![](img/Ss1.png)

    [**Program `client.py` dapat dilihat disini >**](tugas1a/client.py)

    Kemudian, client mengirimkan file yang diinginkan ke server. File yang ditransfer dari client adalah file [**test_client.pdf**](tugas1a/test_client.pdf) yang kemudian server akan menyimpannya pada folder [**server**](tugas1a/server)

    ![](img/Ss2.png)

    Dan server akan merespon seperti pada gambar berikut.

    ![](img/Ss3.png)

2. MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b).

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
