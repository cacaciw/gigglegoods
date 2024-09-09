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
