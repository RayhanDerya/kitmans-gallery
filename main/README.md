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

# Tugas 4 

1. AuthenticationForm adalah salah satu kelas formulir bawaan (built-in) yang disediakan oleh Django untuk menangani proses autentikasi pengguna. Secara khusus, formulir ini dirancang untuk menerima input username dan password. AuthenticationForm sangat mudah digunakan karena telah disiapkan secara default oleh Django. Formulir ini telah mengimplementasikan validasi dan keamanan st sayar Django, seperti proteksi CSRF. Namun, AuthenticationForm hanya menerima username dan password. Jika kamu ingin menambahkan kolom lain, seperti email atau nomor telepon, kamu harus membuat formulir kustom atau memperluas kelasnya.

2. Autentikasi adalah proses validasi/verifikasi identitas user.Proses ini biasanya melibatkan pemeriksaan kredensial, seperti username dan password, untuk memastikan bahwa user tersebut adalah pemilik akun yang sah.

Otorisasi adalah proses menentukan hak atau izin apa yang dimiliki pengguna yang telah terautentikasi. Otorisasi menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu, seperti halaman web, data, atau fitur.

3. Kelebihan session:
    - Data session disimpan di sisi server, sehingga tidak bisa diakses atau dimodifikasi oleh pengguna secara langsung. 
    - Tidak ada batasan ukuran data yang bisa disimpan dalam session, selain kapasitas server itu sendiri.

   Kekurangan session:
   - Setiap session aktif menggunakan sumber daya server (RAM atau database). Jika jumlah pengguna sangat banyak, ini bisa membebani server.

    Kelebihan cookie:
    - Tidak membebani server karena data disimpan di sisi klien (browser pengguna).
    - Cocok untuk aplikasi yang perlu diakses secara global atau menggunakan load balancing, karena tidak bergantung pada server tertentu untuk menyimpan data.

    kekurangan cookie:
    - Data cookies disimpan di browser pengguna dan bisa dilihat, dimodifikasi, atau dicuri oleh pihak lain jika tidak dikelola dengan benar.
    - Ukuran cookie terbatas (sekitar 4KB), sehingga tidak cocok untuk menyimpan data dalam jumlah besar.

4. Secara default, cookies tidak sepenuhnya aman. Ada beberapa risiko yang harus diwaspadai, seperti pencurian data cookies melalui XSS atau MITM jika tidak secure, perusakan atau modifikasi data cookies oleh pihak lain, dan CSRF. Django mengatasi masalah tersebut dengan menerapkan beberapa flag, seperti HttpOnly flag yang membuat cookies tidak dapat diakses oleh JavaScript mengurangi risiko pencurian, Secure flag yang mengatur cookies agar hanya dikirin melalui koneksi https mengurangi risiko serangan oleh MITM, dan CSRF Token yang memvalidasi permintaan apakah permintaan dari pihak yang terdaftar sebagai trusted origin.

5. *Registrasi, Login, dan Logout*
Untuk mengimplementasikan fitur ini,  saya membuat fungsi register(), login_user(), dan logout_user() di main/views.py yang terhubung ke URL yang sesuai di main/urls.py. Halaman register.html menggunakan UserCreationForm bawaan Django untuk membuat akun baru. Sementara itu, login.html menggunakan AuthenticationForm untuk memproses login. Fungsi logout_user() akan mengakhiri sesi dan menghapus cookie last_login, lalu mengarahkan pengguna ke halaman login.

*Menghubungkan Model Product dengan User*
Untuk membuat setiap produk terhubung dengan pemiliknya, saya menambahkan ForeignKey ke model Product di main/models.py, yang menautkannya ke model User bawaan Django. Setelah model dimodifikasi, saya menjalankan migrasi, untuk menerapkan perubahan pada database. Di main/views.py, saat membuat produk baru, saya menetapkan request.user sebagai pemilik produk tersebut.

Menampilkan Detail Pengguna dan Menggunakan Cookies
Di main/templates/main.html, saya menampilkan detail pengguna yang sedang login, seperti username, yang diteruskan dari views.py melalui context. Untuk mengimplementasikan cookie, pada fungsi login_user(), saya mengatur cookie last_login untuk menyimpan waktu login terakhir. Cookie ini kemudian bisa diakses di show_main() menggunakan request.COOKIES.get() untuk ditampilkan di halaman utama.


