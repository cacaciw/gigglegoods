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


# Tugas 4
## Apa perbedaan antara HttpResponseRedirect() dan redirect()
- HttpResponseRedirect() dan redirect() adalah dua cara untuk mengalihkan pengguna ke URL lain dalam aplikasi Django, tetapi mereka digunakan dalam konteks yang berbeda. HttpResponseRedirect() adalah kelas yang langsung membuat respon HTTP untuk pengalihan dan memerlukan kamu untuk memberikan URL secara manual. Ini memberikan kontrol yang lebih langsung, tetapi juga membutuhkan lebih banyak kode untuk menangani pengalihan.
- redirect() adalah fungsi pembantu yang lebih tinggi levelnya dan menawarkan kemudahan penggunaan yang lebih besar. Dengan redirect(), kita dapat memberikan URL, nama view, atau bahkan ID objek, membuatnya lebih fleksibel dan intuitif. Fungsi ini juga secara otomatis menangani pengalihan berdasarkan nama view, yang mengurangi kemungkinan kesalahan saat menulis URL secara manual. Oleh karena itu, dalam banyak kasus, penggunaan redirect() lebih disarankan karena meningkatkan kejelasan kode dan efisiensi pengalihan.

## Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model `Product` dengan model `User` dalam Django, kita dapat menggunakan relasi satu-ke-banyak.
- Definisi Model: Model `Product` didefinisikan dengan atribut seperti nama, deskripsi, dan harga. Hubungan dengan model `User` dibuat menggunakan `ForeignKey`, yang menunjukkan bahwa setiap produk dimiliki oleh satu pengguna.
- Pengaturan `ForeignKey`: Dengan menggunakan `ForeignKey(User, on_delete=models.CASCADE)`, kita menetapkan bahwa jika seorang pengguna dihapus, semua produk terkait juga akan dihapus. Ini menjaga integritas data.
- Atribut `related_name`: Menggunakan `related_name='products'` memungkinkan akses yang lebih mudah untuk mendapatkan semua produk milik seorang pengguna. Contohnya, kita bisa menggunakan `user.products.all()` untuk mengambil semua produk yang dimiliki oleh pengguna tersebut.
- Pembuatan Data: Saat membuat produk baru, kita dapat langsung menetapkan pengguna yang memiliki produk tersebut. Ini menjadikan pengelolaan data lebih terstruktur.
- Pengambilan Data: Dengan relasi yang sudah terhubung, kita dapat dengan mudah mengambil semua produk milik seorang pengguna, memungkinkan pengelolaan dan analisis data yang lebih efisien.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication dan authorization adalah dua konsep penting dalam keamanan aplikasi, tetapi mereka memiliki perbedaan yang jelas,
1. Authentication, proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna adalah siapa yang mereka klaim.
Contoh, saat pengguna memasukkan username dan password untuk login, sistem memeriksa apakah kredensial tersebut valid.
2. Authorization, proses menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu.
Contoh, setelah pengguna berhasil login, sistem menentukan apakah pengguna tersebut memiliki hak akses untuk melihat halaman tertentu atau mengedit data.
Saat pengguna login, langkah pertama adalah autentikasi. Pengguna memasukkan kredensial mereka (username dan password), dan sistem memverifikasi informasi tersebut. Jika kredensial valid, pengguna dianggap terautentikasi. Selanjutnya, sistem melakukan otorisasi untuk menentukan akses pengguna berdasarkan peran atau izin yang telah ditetapkan.
3. Implementasi di Django
Authentication: Django menyediakan sistem autentikasi built-in yang memungkinkan pengembang untuk menangani proses login dan logout dengan mudah. Ini termasuk penggunaan model User dan fungsi seperti authenticate() untuk memverifikasi kredensial pengguna.
Authorization: Untuk otorisasi, Django menggunakan sistem permission dan grup. Pengembang dapat menetapkan izin tertentu pada model atau tampilan (views) dan menggunakan decorator seperti @login_required dan @permission_required untuk membatasi akses pengguna.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan session cookies. Ketika pengguna berhasil login, Django membuat session yang berisi informasi terkait pengguna dan menyimpannya di database, memori, atau file tergantung pada konfigurasi. Django kemudian mengirimkan session ID kepada pengguna dalam bentuk cookie. Setiap kali pengguna membuat permintaan baru, cookie tersebut dikirim kembali ke server untuk memverifikasi identitas pengguna yang sudah login, sehingga pengguna tidak perlu login ulang selama sesi berlangsung.
- Kegunaan Lain dari Cookies
Selain mengingat pengguna yang login, cookies memiliki banyak kegunaan lain:
1. Menyimpan Preferensi Pengguna (Misalnya, bahasa atau tema yang dipilih pengguna)
2. Melacak Aktivitas Pengguna, website dapat menggunakan cookies untuk melacak halaman yang dikunjungi atau produk yang dilihat pengguna, membantu dalam personalisasi konten.
3. Membantu dalam Analiti, cookies digunakan untuk melacak perilaku pengguna secara anonim, memberikan data untuk analitik website.
4. Mengelola Keranjang Belanja ,di situs e-commerce, cookies sering digunakan untuk menyimpan informasi sementara tentang barang-barang yang ditambahkan ke keranjang belanja.
- Apakah Semua Cookies Aman Digunakan?
Tidak semua cookies aman, terutama jika tidak dikelola dengan benar. Beberapa potensi risiko:
- Cookies Tanpa Enkripsi, jika cookie yang berisi informasi sensitif dikirim tanpa enkripsi (seperti melalui HTTP, bukan HTTPS), maka bisa dicegat oleh pihak ketiga.
- Session Hijacking, penyerang bisa mencuri cookie session dan menyamar sebagai pengguna yang sah jika cookie tidak diamankan dengan baik.
- Third-Party Cookies, cookies dari pihak ketiga dapat digunakan untuk melacak aktivitas pengguna di berbagai situs, yang dapat menimbulkan masalah privasi.
Untuk meningkatkan keamanan, Django mendukung penggunaan **Secure Cookies** (cookies yang hanya dikirim melalui HTTPS) dan **HttpOnly Cookies** (cookies yang tidak dapat diakses oleh JavaScript), sehingga mengurangi risiko pencurian cookie dan eksploitasi lainnya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut adalah cara saya mengerjakan checlist Tugas Individu 4:
1. Pada directori views.py, saya menambahkan import UserCreationForm dan messages
2. Lalu saya membuat fungsi `register` yang akan diimport ke urls.py dan membuat berkas `register.html` di dalam templates pada direktori main
3. Selanjutnya saya membuat fungsi login dengan membuka views.py dan menambahkan import authenticate, login, dan AuthenticationForm. Lalu saya membuat fungsi `login_user` yang akan diimport ke urls.py dan membuat berkas `login.html` di dalam templates pada direktori main
4. Saya membuat fungsi logout dengan mengimport fungsi logout, menambahkan button logout ke `main.html`, dan mengimport fungsi logout ke urls.py pada direktori main
5. Lalu saya mengrekstriksi halaman main untuk user yang belum login, dengan mengimport `login_required`dan menambahkan `@login_required(login_url='/login')` diatas fungsi show_main
6. Setelah itu saya menabahkan penggunaan data cookies, dengan mengimpor import HttpResponseRedirect, reverse, dan datetime. Pada berkas yang sama fungsi `login_user` ditambahkan fungsionalitas cookies yang bernama `last_login`, dan pada show_main menambahkan 'last_login': request.COOKIES['last_login'] pada bagian context, dan mengedit main.html agar memperlihatkan sesi login terakhirnya
7. Lalu saya menghubungkan models product dengan user, pada berkas models.py saya mengimport user, lalu saya mengubah fungsi create_giggle_entry dengan membuat field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.
8. Lalu saya mengubah value dari giggle_entries dan context pada fungsi show_main dengan user yang suda terotorisasi agar nama pada menu utama adalah nama user yang sudah masuk
9. Saya makemigrations dan migrate
10. Setelah itu saya import os pada setting.py, dan mengubah konfigurasi debug
11. Terakhir saya save semua berkas dan melakukan add, commit, push
Proyek sekarang siap dijalankan! @_<

#TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   a. Urutan Spesifisitas (Specificity)
      CSS menentukan prioritas berdasarkan **spesifisitas** dari setiap selector. Spesifisitas dihitung berdasarkan empat kategori:
      - Inline styles (gaya yang langsung diterapkan di elemen HTML) memiliki prioritas tertinggi.
      - ID selector(`#id`) memiliki prioritas berikutnya.
      - Class selector, **attribute selector**, dan **pseudo-class** (seperti `.class`, `[type="text"]`, atau `:hover`) berada di bawah ID.
      - Tag selector(misalnya `p`, `div`) dan **pseudo-element** (seperti `::before`, `::after`) memiliki prioritas paling rendah.
    b. Perhitungan Spesifisitas
      Setiap selector dipecah ke dalam kategori-kategori berikut untuk menghitung spesifisitasnya:
      - Inline style 1 poin pada elemen inline (ini memberikan spesifisitas tertinggi).
      - ID selector 1 poin per ID (`#example`).
      - Class selector. attribute selector, pseudo-class 1 poin per item (misalnya `.class`, `[type="text"]`, `:hover`).
      - Tag selector dan pseudo-element 1 poin per item (`div`, `p`, `::before`).
      Contoh perhitungan spesifisitas:
      - Inline style: `style="color: red"` (Spesifisitas: 1000)
      - ID selector: `#id` (Spesifisitas: 0100)
      - Class selector: `.class` (Spesifisitas: 0010)
      - Tag selector: `p` (Spesifisitas: 0001)
      Jika elemen dipengaruhi oleh beberapa selector, selector dengan nilai spesifisitas tertinggi yang akan diambil.
    c. Urutan Sumber CSS
      Selain spesifisitas, urutan sumber CSS juga memengaruhi prioritas:
      - Urutan penulisan: Jika dua selector memiliki spesifisitas yang sama, yang ditulis paling akhir akan digunakan.
      - `!important`: Properti dengan deklarasi `!important` akan mengesampingkan semua aturan di atas (kecuali jika properti lain juga menggunakan `!important` dan memiliki spesifisitas lebih tinggi).
      Urutan prioritas CSS selector dipengaruhi oleh spesifisitas selector, urutan sumber CSS, dan deklarasi `!important`. Selector dengan spesifisitas lebih tinggi akan selalu diterapkan lebih dulu.

2. Responsive design penting karena memastikan aplikasi web menyesuaikan tampilannya sesuai perangkat yang digunakan, baik smartphone, tablet, atau desktop. Ini memberikan pengalaman       pengguna yang konsisten, meningkatkan SEO, serta mempermudah pengembangan dan pemeliharaan.
Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- Instagram: Tampilan web dan mobile yang mudah digunakan.
- Medium: Artikel menyesuaikan ukuran layar.
Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- Website yang tidak ramah mobile.
- Situs web pendidikan tertentu: Hanya mendukung tampilan desktop.
Responsive design memastikan akses yang nyaman di berbagai perangkat.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  a. Margin: Ruang di luar elemen, memberikan jarak antara elemen dengan elemen lain di sekitarnya.
   - Contoh implementasi: 
     ```
     div {
       margin: 20px;
     }
     ```
   Ini akan memberikan jarak 20px di luar elemen `div`.
  b. Border: Garis yang mengelilingi elemen, berada di antara margin dan padding.
   - Contoh implementasi: 
     ```
     div {
       border: 2px solid black;
     }
     ```
   Ini akan memberikan garis border hitam dengan ketebalan 2px di sekitar elemen `div`.

  c. Padding: Ruang di dalam elemen, memberikan jarak antara konten elemen dengan border elemen tersebut.
   - Contoh implementasi: 
     ```
     div {
       padding: 15px;
     }
     ```
   Ini akan memberikan jarak 15px di dalam elemen `div` antara konten dan border.
   Perbedaan mendasar: Margin mengontrol jarak luar, border adalah garis di sekitar elemen, dan padding mengatur jarak dalam elemen.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   Flexbox dan Grid Layout adalah dua teknik tata letak di CSS yang digunakan untuk menyusun elemen secara responsif.

  a. Flexbox (Flexible Box Layout):
   - Konsep: Flexbox digunakan untuk menyusun elemen dalam satu dimensi, baik secara baris (horizontal) maupun kolom (vertikal). Elemen di dalam flex container dapat diatur agar menyesuaikan ukuran atau ruang yang tersedia.
   - Kegunaan: Ideal untuk menyusun elemen secara horizontal atau vertikal, seperti menata navigasi, kartu produk, atau galeri gambar.
   - Contoh implementasi:
     ```
     .container {
       display: flex;
       justify-content: space-around;
     }
     ```
   Ini akan membuat elemen dalam container berbaris dengan ruang di antara mereka.
  b. Grid Layout:
   - Konsep: Grid layout digunakan untuk membuat tata letak dua dimensi, yaitu baris dan kolom. Grid memungkinkan kita untuk menentukan area tertentu bagi elemen dengan lebih presisi.
   - Kegunaan: Cocok untuk tata letak kompleks seperti halaman web dengan beberapa kolom dan baris, dashboard, atau layout halaman utama.
   - Contoh implementasi:
     ```
     .container {
       display: grid;
       grid-template-columns: repeat(3, 1fr);
     }
     ```
   Ini akan membagi container menjadi tiga kolom dengan lebar yang sama.
   Perbedaan: Flexbox digunakan untuk tata letak satu dimensi (baris atau kolom), sedangkan Grid untuk tata letak dua dimensi (baris dan kolom).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  a. Saya membuat fungsi `edit_product` dan `delete_product` pada `views.py`, yang menerima request dan ID produk, lalu menambahkan URL-nya.
  b. Saya membuat template untuk `edit_product`, sekaligus memperbarui template lain agar terlihat lebih menarik.
  c. Di `main.html`, saya mengedit templatenya sehingga ketika tidak ada produk, muncul tampilan kosong dengan pesan yang menjelaskan bahwa produk tidak tersedia.
  d. Saya membuat `card_product.html` yang dihubungkan ke `main.html` untuk menampilkan informasi produk yang meliputi nama, harga, deskripsi, serta tombol edit dan delete.
  e. Saya mengatur layout `card_product` menggunakan grid untuk menampilkan informasi produk dengan rapi.
  f. Saya membuat template navbar yang responsive di direktori luar, dengan mengaitkan link pada elemen-elemen di navbar.
  g. Terakhir, saya menambahkan script agar situs dapat digunakan dengan nyaman di perangkat mobile, lalu melakukan `git add`, `commit`, dan `push`.


