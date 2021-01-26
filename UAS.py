lagi='y'

while lagi=='y':
    jarak=float(input('masukkan jarak \t\t\t: '))
    v1=int(input('masukkan kecepatan Budi \t: '))
    v2=int(input('masukkan kecepatan yandi \t: '))
    p1=float(input('masukkan waktu berangkat budi \t: '))
    p2=float(input('masukkan waktu berangkat yandi \t: '))
    w1=(p1-p2)
    selisih_jarak=(v1*w1/60)
    print('')
    wp=(jarak-selisih_jarak/v1+v2)
    jam=(wp/3600)
    waktu_berpapasan=(p2+jam)
    print('mereka berpapasan pada jam',round(waktu_berpapasan,2),'dari kota jakarta')

    lagi=input("Ambil Data Lagi [y/n]? : ")
    print('')