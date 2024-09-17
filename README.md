## Link proyek
http://tarissa-mutia-gigglegoods.pbp.cs.ui.ac.id

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat proyek django yang baru
- Pertama saya membuat direktori baru dengan nama giggle goods
- Lalu saya mengaktifkan virtual enviroment, dan membuat file bernama requirements.txt dan menambahkan dependencies
- Lalu saya menginstalasi dependencies itu dengan me-run pip install -r requirements.txt ke terminal vscode saya
- Setelah itu saya me-run " django-admin startproject gigglegoods . " untuk memulai proyek django saya
- Saya mengkonfigurasi Host dan menambahkan file .gitignore untuk mengkonfigurasi git sata lalu saya add, commit, push ke repository yang sudah saya buat sebelumnya
- Setelah itu saya membuka web PWS dan membuat proyek baru dengan nama gigglegoods
- lalu saya mengkonfigurasi local host sesuai dengan link proyek yang baru saya buat di PWS
- Setelah itu saya cek bila proyek saya sudah running atau belum
- Ketika sudah terlihat running saya melakukan git add, commit, push
2. Membuat aplikasi dengan nama main pada proyek tersebut.
- Pada direktori saya me-run " python3 manage.py startapp main " untuk membuat aplikasi main, dan pada setting.py saya tambahkan 'main' pada 'ALLOWED APPS'
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Setelah saya sudah memberikan template dan attribute yang diingikan saya membuat file urls.py dalam direktori main
- Saya meng-import path django.urls untuk mendefinisikan pola URL
- Saya juga meng-import main.views dengan fungsi show.main untuk menampil URL
- Lalu pada direktori utama saya mengakses urls.py, disana saya meng-import fungsi include, dari django,urls
- Pada urls.py didalamnya ada variable urlpatterns dan saya menambahkan path(' ', include('main.urls')). Dibiarkan string kosong agar halaman aplikasi dapat diakses secara langsung
4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: name, price, description
- Pada aplikasi main saya mengakses file models.py
- Lalu saya membuat class GiggleCatalogue dan menambahkan attribut name, price, description, dan, giggle level
- Lalu saya membuat migrasi model dengan me-run " python3 manage.py makemigrations "
- Lalu saya mengaplukasi migrasi model dengan me-run " python3 manage.py migrate "
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Pada file views.py saya membuat fungai show_main yang memberikan context ke main.html yang berisikan nama app, nama saya, dan kelas saya
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Seperti yang saya sudah lalukan tadi saya membuat file urls.py dalam aplikasi main
- Saya meng-import path django.urls untuk mendefinisikan pola URL
- Saya juga meng-import main.views dengan fungsi show.main untuk menampil URL
7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Saya mendeploy ke PWS yang sebelumnua sudah saya buat sebelumnya

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Uploading Screenshot 2024-09-09 at 20.17.55 2.jpeg…]()

(Link drive bagan: https://drive.google.com/drive/folders/1pelIxNo9OPmyCBBEmUvfjsOvh0BlyKe8?usp=sharing)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi yang digunakan secara luas dalam pengembangan perangkat lunak. Fungsinya mencakup berbagai aspek penting yang membantu tim pengembang mengelola perubahan kode dengan efisien dan kolaboratif. Berikut adalah fungsi utama Git dalam pengembangan perangkat lunak:
1. Version Control
- Git memungkinkan pengembang melacak setiap perubahan yang dilakukan pada kode sumber. Setiap perubahan disimpan sebagai commit, yang memungkinkan pengembang untuk melihat riwayat perubahan, memulihkan kode ke versi sebelumnya, dan mencegah hilangnya pekerjaan akibat kesalahan.
2. Branching dan Merging
- Git mendukung pembuatan branch yang memungkinkan pengembang bekerja pada fitur baru, eksperimen, atau perbaikan bug tanpa mengganggu kode utama (branch main atau master). Setelah fitur diuji, branch dapat digabungkan (merge) ke dalam branch utama.
3. Kolaborasi Tim
- Git mendukung kolaborasi tim dengan memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan. Dengan sistem distributed version control, setiap pengembang memiliki salinan penuh dari repositori di mesin lokal mereka.

Fungsi git dalam pengembangan perakat lunak itu masih banyak seperti tracking dan reverting perubahan,continuous integration (CI) dan deployment, dan lain lain

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan framework permulaan dalam pembelajaran pengembangan perangkat lunak karena menyediakan banyak fitur bawaan (batteries included) seperti autentikasi, manajemen database, dan sistem admin, yang memudahkan pemula memulai. 
Dengan dokumentasi yang lengkap dan komunitas yang kuat, Django mendukung pembelajaran secara efektif. Struktur Model-View-Template (MVT) membantu pemula memahami pemisahan antara logika bisnis, data, dan tampilan. Selain itu, Django memiliki keamanan bawaan, mendukung pengembangan cepat, cocok untuk proyek skala kecil hingga besar, dan menggunakan Python, bahasa yang mudah dipahami. 
Kombinasi fitur ini menjadikan Django pilihan ideal untuk memulai belajar pengembangan web.

## Mengapa model pada Django disebut sebagai ORM?
Django menggunakan ORM (Object-Relational Mapping) untuk memetakan objek dalam kode Python ke tabel-tabel di database relasional tanpa perlu menulis kueri SQL secara manual. 
Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan sintaks Python, sehingga operasi seperti menyimpan, mengambil, memperbarui, dan menghapus data menjadi lebih sederhana. 
ORM juga menangani relasi antar tabel secara otomatis dan memungkinkan aplikasi untuk lebih mudah dipindahkan ke berbagai jenis database, seperti SQLite atau PostgreSQL.


# Tugas 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian platform karena:

1. Konsistensi Data, Menjamin data yang dikirim akurat dan seragam.
2. Kecepatan, Memastikan data sampai dengan cepat, penting untuk aplikasi real-time.
3. Skalabilitas, Mendukung pertumbuhan volume data dan jumlah pengguna.
4. Pengalaman Pengguna, Meningkatkan kepuasan dengan data yang relevan dan terkini.
5. Keamanan, Melindungi data dari akses tidak sah.
Secara keseluruhan, data delivery memastikan performa, integritas, dan keamanan platform.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dibandingkan XML karena kemudahan penggunaannya, ukuran yang lebih kecil, dan performa yang lebih baik dalam kebanyakan kasus. JSON lebih efisien untuk komunikasi data modern, terutama dalam aplikasi web dan API, tetapi XML masih memiliki tempat dalam konteks tertentu yang memerlukan fungsionalitas atau struktur khusus.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Metode `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirimkan melalui formulir memenuhi semua validasi yang telah ditentukan. Ketika memanggil `is_valid()` pada sebuah instance form, metode ini akan:
- Validasi Data, Memeriksa setiap field dalam form untuk memastikan data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan (seperti tipe data yang benar, format, panjang, dan lain-lain).
- Mengumpulkan Error, Jika data tidak valid, metode ini akan mengumpulkan dan menyimpan pesan error yang terkait dengan field yang bermasalah. Pesan error ini kemudian bisa digunakan untuk memberi umpan balik kepada pengguna.
- Mengembalikan Hasil Validasi, Metode ini mengembalikan `True` jika semua data valid, dan `False` jika ada kesalahan. 

Kenapa Kita Membutuhkan `is_valid()`?
- Keamanan Data, Memastikan bahwa hanya data yang valid dan aman yang diproses, menghindari masalah keamanan seperti injeksi data yang tidak valid.
- Pengalaman Pengguna, Memberi umpan balik yang jelas kepada pengguna jika ada kesalahan dalam pengisian form, sehingga mereka bisa memperbaiki data yang salah sebelum data diproses lebih lanjut.
- Konsistensi Data, Menghindari penyimpanan data yang tidak konsisten atau tidak sesuai format yang diinginkan, yang bisa mengakibatkan masalah dalam pengolahan data atau integritas database.
Secara keseluruhan, `is_valid()` membantu menjaga kualitas dan keamanan data yang dikumpulkan melalui formulir di aplikasi Django.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` di Django melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF) dengan memastikan bahwa permintaan POST berasal dari pengguna yang sah. Tanpa `csrf_token`, aplikasi rentan terhadap serangan di mana penyerang dapat memanipulasi permintaan atas nama pengguna yang telah masuk, berpotensi menyebabkan kerusakan atau pencurian data. Dengan menambahkan `csrf_token` di formulir, Django memastikan bahwa setiap permintaan yang diterima valid dan tidak dibuat oleh pihak yang tidak berwenang.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut adalah cara saya mengerjakan Tugas Individu 3:
1. Buat `forms.py` di direktori `main`, dan sesuaikan dengan model yang telah dibuat.
2. Edit `views.py` untuk mengimpor `forms`, `HttpResponse`, `redirect`, dan `serializers`.
3. Tambahkan fungsi untuk membuat objek baru dengan metode POST.
4. Buat halaman baru dengan menambahkan file HTML baru di direktori `templates`, misalnya `create_giggle_entry.html`.
5. Sertakan `{% csrf_token %}` dan tombol submit di formulir HTML.
6. Tambahkan empat fungsi di `views.py` untuk menampilkan data dalam format JSON dan XML: `show_json`, `show_xml`, `show_xml_by_id`, dan `show_json_by_id`.
7. Update `urls.py` dengan rute baru untuk halaman formulir dan halaman yang menampilkan data dalam format JSON dan XML.
Proyek sekarang siap dijalankan! @_<

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

show_xml
<img width="1512" alt="Screenshot 2024-09-17 at 19 35 52" src="https://github.com/user-attachments/assets/62090021-c522-40db-ad38-53158455fddc">

show_json
<img width="1512" alt="Screenshot 2024-09-17 at 19 36 05" src="https://github.com/user-attachments/assets/37dde4be-14f4-4262-bfdb-38818276c889">

show_json_by_id
<img width="1512" alt="Screenshot 2024-09-17 at 19 36 19" src="https://github.com/user-attachments/assets/117b6c16-373c-4cb5-b6a7-082e079966f3">

show_xml_by_id
<img width="1512" alt="Screenshot 2024-09-17 at 19 36 25" src="https://github.com/user-attachments/assets/463152f9-ac97-4d20-b1c2-66ed0085bd39">


