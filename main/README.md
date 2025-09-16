# Link Web : https://rayhan-derya-kitmansgallery.pbp.cs.ui.ac.id/

# Penjelasan checkpoint
    1. Membuat proyek django baru dengan menjalankan perintah django-admin startproject setelah mengaktifkan virtual environment di command prompt pada direktori utama

    2. di direktori utama, membuat aplikasi main dengan menjalankan django-admin startapp di command prompt

    3. melakukan routing pada proyek dengan memodifikasi file urls.py pada proyek sehingga ketika URL diterima oleh proyek, akan dipetakan ke level aplikasi apakah ada pola yang cocok atau tidak.

    4. membuat model dengan mendifinisikan class bernama Product yang memiliki atrbut-atribut wajib seperti name, price, description, thumbnail, category, is_featured

    5. fungsi pada views.py yang mengembalikan laman HTML dengan membuat fungsi show_main pada views.py yang mereturn fungsi render yang menampilkan main.html pada direktori templates

    6. routing pada level aplikasi adalah dengan memetakan url dari urls.py pada tingkat aplikasi ke views.py yang akan menampilkan laman HTML sesuai dengan pola yang diterima

    7. mendeploy web menggunakan PWS

# Bagan Routing : https://drive.google.com/file/d/1scn4GZLybcGpxzLjCG8BtGMCxwWoNaoI/view?usp=sharing

# Peran settings.py pada proyek django adalah sebagai pusat kontrol dan konfigurasi dari proyek django. settings.py mengatur koneksi databes hingga daftar aplikasi yang terpasang.

# Migrasi model pada django adalah untuk melacak perubahan pada database model dari proyek. Migrasi adalah instruksi untuk membuat perubahan tabel database menyesuaikan dengan perubahan yang diterapkan dalam kode. Dengan perintah python manage.py makemigrations pada terminal, django akan memindai perubahan pada model dan akan membuat berkas migrasi yang akan menjadi "blueprint" dari perubahan yang akan diterapkan. Lalu, dengan perintah python manage.py migrate, django akan membaca berkas migrasi yang sebelumnya dibuat lalu menerapkan perubahan dengan menjalankan instruksi yang ada pada berkas. Terakhir, django akan membuat log riwayat perubahan untuk melacak perubahan.

#  Django tepat untuk dijadikan permulaan pembelajaran perangkat lunak karena fitur fitur nya yang siap pakai. strukturnya yang jelas dengan arsitektur MVT (Model-View-Template) mengajarkan pemisahan tanggung jawab antara data (models.py), logika (views.py), dan tampilan (HTML). Ditambah penggunaan bahasa python yang relatif mudah dipahami pemula, django menjadi pilihan tepat untuk menjadi framework permulaan.

# Asisten dosen membantuk cukup baik untuk tutorial dan pengerjaan tugas ini


# Tugas 3

1. Data delivery penting karena dapat mendukung terbuatnya pengalaman pengguna yang baik. data delivery yang terstruktur dengan baik juga dapat mengoptimalkan performa platform. 

2. menurut saya anatar XML dan JSON lebih baik JSON. karena JSON adalah format yg umum dan universal yang dapat diterima banyak program dan bahasa sehingga memudahkan untuk mengirim dan memindahkan data tanpa adanya atribut yang hilang.

3. fungsi method is_valid() adalah untuk memastikan data yang dikirim melalui form valid sehingga tidak ada kesalahan dalam pengiriman data.
method is_valid() penting agar data yang diterima memenuhi ketentuan yang sudah didefinisikan sehingga penyajian data lebiih akurat

4. csrf-token itu penting karena tanpa token itu, form kita rentan diserang CSRF (Cross-Site Request Forgery). Kalau tidak pakai, penyerang bisa membuat form palsu di situs mereka, lalu mengarahkan korban untuk submit form itu secara diam-diam. Karena tokennya nggak ada dan permintaan itu dianggap valid, Django akan memprosesnya, dan korban bisa mengalami kerugian. csrf_token berfungsi sebagai kunci unik yang hanya diketahui oleh server dan form yang sah, sehingga Django bisa menolak permintaan yang datang dari luar.

5. Langkah-langkah Implementasi

 - membuat 4 fungsi baru pada views.py dengan membuat list semua model dan mereturn httpresponse yang kemudian dilakukan routing pada level aplikasi untuk mengarahkan request sesuai pola yang cocok dan mengembalikan halaman html(XML, JSON, XML_BY_ID, JSON_BY_ID).

 - fitur baru ditambahkan yaitu add product. tombol add product pada main.html dibuat dengan tag <button></button> yang akan meredirect user
    ke halaman tambah produk yang berisi form sesuai yang sudah didefinisikan pada forms.py. setelah proses input selesai, maka akan kembali
    ke halaman main dan akan menampilkan preview produk yang baru serta tombol detail yang akan meredirect user ke halaman detail produk.

6. asdos cukup membantu dalam pengerjaan tugas 3

7. ristek.link/ScreenshotPostmanRayhan