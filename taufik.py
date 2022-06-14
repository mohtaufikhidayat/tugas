class _suhu():
    def __init__(self, nama, tmpt_lahir, tgl_lahir, gender, suhu_tubuh,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.suhu_tubuh = suhu_tubuh
        
    def _set (self, nama, tmpt_lahir, tgl_lahir, gender, suhu_tubuh,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.suhu_tubuh = suhu_tubuh

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tmpt_lahir + ', ' +  self.tgl_lahir)
        if self.gender in ['L', 'l']:
            gender = 'Laki-Laki'
        else:
            gender = 'Perempuan'
        print('Gender      :' + gender)

        if self.suhu_tubuh >39:
            print('Suhu tubuh tidak normal')
        else:
            if self.suhu_tubuh >36:
                print('suhu tubuh normal')
            else:
                if self.suhu_tubuh <36:
                    print('suhu tubuh dingin')

print('=====================================')
print('     PROGRAM CEK SUHU TUBUH      ')
print('=====================================')

nama      = input('Nama lengkap        :')
tmpt_lahir = input('Tempat lahir        :')
tgl_lahir  = input('Tanggal lahir       :')
gender     = input('Gender L/P          :')
suhu_tubuh = float(input('Masukkan suhu tubuh :'))

print('======================================')

proses = _suhu(nama,tmpt_lahir,tgl_lahir,gender,suhu_tubuh)
print (proses._get())