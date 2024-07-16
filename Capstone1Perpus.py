from tabulate import tabulate
from datetime import datetime as datt

database = [
{'ID': 'P26K0001', 'username': 'an4',        'PIN': 3822, 'latestReadBook': 'Don Quixote', 'latestReadDate': '20/9/2023',                               'Nama Lengkap': 'Adriana Lucentia', 'Gender': 'P', 'Usia': '28', 'Kota': 'Tangerang Selatan'},
{'ID': 'P26K0002', 'username': 'beb3',       'PIN': 9258, 'latestReadBook': "Alice's Adventures in Wonderland", 'latestReadDate': '29/2/2024',          'Nama Lengkap': 'Abe Bimantyo', 'Gender': 'L', 'Usia': '21', 'Kota': 'Jakarta Pusat'},
{'ID': 'P26K0003', 'username': 'cac6sar',    'PIN': 2942, 'latestReadBook': 'The Adventures of Huckleberry Finn', 'latestReadDate': '21/2/2024',        'Nama Lengkap': 'Kartika Sari', 'Gender': 'P', 'Usia': '35', 'Kota': 'Jakarta Pusat'},
{'ID': 'P26K0004', 'username': 'dov1don',    'PIN': 1923, 'latestReadBook': 'Moby Dick', 'latestReadDate': '1/1/2024',                                  'Nama Lengkap': 'London Vicky', 'Gender': 'L', 'Usia': '20', 'Kota': 'Jakarta Utara'},
{'ID': 'P26K0005', 'username': 'ek4man',     'PIN': 5496, 'latestReadBook': '	Jane Eyre', 'latestReadDate': '18/3/2024',                                'Nama Lengkap': 'Ekky Kartika Baman', 'Gender': 'L', 'Usia': '22', 'Kota': 'Bekasi'},
{'ID': 'P26K0006', 'username': 'f4ny5',      'PIN': 4849, 'latestReadBook': "The Pilgrim's Progress", 'latestReadDate': '13/1/2024',                    'Nama Lengkap': 'Stefany Aurelia', 'Gender': 'P', 'Usia': '24', 'Kota': 'Jakarta'},
{'ID': 'P26K0007', 'username': 'g3rald0',    'PIN': 4253, 'latestReadBook': 'The Hobbit, or, There and Back Again', 'latestReadDate': '1/1/2024',       'Nama Lengkap': 'Geraldo Sutomo', 'Gender': 'L', 'Usia': '21', 'Kota': 'Tangerang'},
{'ID': 'P26K0008', 'username': 'hum4n',      'PIN': 9558, 'latestReadBook': 'The Three Musketeers', 'latestReadDate': '14/6/2024',                      'Nama Lengkap': 'Humaira Nur', 'Gender': 'P', 'Usia': '19', 'Kota': 'Bekasi'},
{'ID': 'P26K0009', 'username': '1mban9',     'PIN': 5851, 'latestReadBook': "Alice's Adventures in Wonderland", 'latestReadDate': '10/5/2024',          'Nama Lengkap': 'Imbang Firman Yasin', 'Gender': 'L', 'Usia': '25', 'Kota': 'Bekasi'},
{'ID': 'P26K0010', 'username': 'h4l1m6c',    'PIN': 8904, 'latestReadBook': "Harry Potter and the Sorcerer's Stone", 'latestReadDate': '25/1/2024',     'Nama Lengkap': 'Halim Ilyas', 'Gender': 'L', 'Usia': '22', 'Kota': 'Depok'},
{'ID': 'P26K0011', 'username': 'r4ml4hg',    'PIN': 8793, 'latestReadBook': 'Harry Potter and the Goblet of Fire', 'latestReadDate': '30/6/2024',       'Nama Lengkap': 'Ramlah Puspitasari', 'Gender': 'P', 'Usia': '37', 'Kota': 'Jakarta Timur'},
{'ID': 'P26K0012', 'username': 'p7j1x2',     'PIN': 9431, 'latestReadBook': 'Harry Potter and the Prisoner of Azkaban', 'latestReadDate': '13/1/2024',  'Nama Lengkap': 'Pu1ji Idris', 'Gender': 'L', 'Usia': '18', 'Kota': 'Jakarta Timur'},
{'ID': 'P26K0013', 'username': 'k4rt1nixld', 'PIN': 2784, 'latestReadBook': '	Eragon', 'latestReadDate': '21/4/2024',                                   'Nama Lengkap': 'Kartini Suhendri', 'Gender': 'P', 'Usia': '18', 'Kota': 'Depok'},
{'ID': 'P26K0014', 'username': 'm4r1anihy5', 'PIN': 9788, 'latestReadBook': 'The Three Musketeers', 'latestReadDate': '25/1/2024',                      'Nama Lengkap': 'Mariani Haryadi', 'Gender': 'P', 'Usia': '24', 'Kota': 'Bekasi'},
{'ID': 'P26K0015', 'username': '7sw4tundcb', 'PIN': 9831, 'latestReadBook': '	Black Beauty', 'latestReadDate': '16/1/2024',                             'Nama Lengkap': 'Uswatun Kurniati', 'Gender': 'P', 'Usia': '34', 'Kota': 'Jakarta Selatan'},
{'ID': 'P26K0016', 'username': 'w4r7wuy',    'PIN': 4925, 'latestReadBook': 'Peter Pan', 'latestReadDate': '16/7/2024',                                 'Nama Lengkap': 'Ernawati Waruwu', 'Gender': 'P', 'Usia': '35', 'Kota': 'Tangerang'},
{'ID': 'P26K0017', 'username': 'j4ns3nrqr',  'PIN': 1691, 'latestReadBook': 'Black Swan', 'latestReadDate': '15/9/2023',                                'Nama Lengkap': 'Jansen Setiadi', 'Gender': 'L', 'Usia': '19', 'Kota': 'Depok'}
]

### VALIDATION FUNCTION START FROM HERE ###
def ADC(foo = 'Masukkan Angka/Huruf: '):
  while True:
    wew = input(foo)
    if wew.replace(' ', '').replace("'",'').isalnum():
      return str(wew)
    else:
      print(f'Input Invalid.')

def DigC(foo = 'Masukkan Angka: '):
  while True:
    wew = input(foo)
    if wew.isdigit():
      return int(wew)
    else:
      print(f'Input Invalid.')

def AlpC(foo = 'Masukkan Kata: '):
    while True:
      wew = input(foo)
      if wew.replace(' ', '').isalpha():
        return str(wew)
      else:
        print(f'Input Invalid.')

def checklenid(id):
    while True:
        formatted_id = ''
        if len(str(id)) == 1:
            formatted_id = 'P26K000' + str(id)
        elif len(str(id)) == 2:
            formatted_id = 'P26K00' + str(id)
        elif len(str(id)) == 3:
            formatted_id = 'P26K0' + str(id)
        elif len(str(id)) == 4:
            formatted_id = 'P26K' + str(id)
        else:
            print('ID harus terdiri dari 1-4 digit.')
            id = DigC('Masukkan ID: ')
            continue
        if any(entry['ID'] == formatted_id for entry in database):
            print('ID sudah ada!')
            id = DigC('Masukkan ID: ')
        else:
            return formatted_id

def checkusername(uname):
  while True:
    if any(entry['username'] == uname for entry in database):
      print('Username sudah ada!')
      uname = ADC('Masukkan username: ')
    else:
      return uname

def checkdate(date):
  while True:
    if len(date) != 10 or not date[0:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit() or date[2] != '/' or date[5] != '/':
      print('Tanggal harus dalam format DD/MM/YYYY.')
      date = input('Masukkan Tanggal (DD/MM/YYYY): ')
      continue
    try:
      parsed_date = datt.strptime(date, '%d/%m/%Y')
      formatted_date = parsed_date.strftime('%d/%m/%Y')
      return formatted_date
    except ValueError:
      print('Tanggal tidak valid.')
      date = input('Masukkan Tanggal (DD/MM/YYYY): ')

def checkpin(pin):
  while True:
    if len(str(pin)) == 4:
      return pin
    else:
      print('PIN harus terdiri dari 4 digit.')
      pin = ADC('Masukkan 4 Digit PIN: ')

def checkgender(gender):
    while True:
        if gender.lower() in ['p', 'l']:
            return gender.title()
        else:
            print('Jenis Kelamin harus P/L.')
            gender = input('Masukkan Jenis Kelamin (P/L): ')

### FUNCTIONS OF PROGRAM START HERE ###
def check(w):
    print(tabulate(w, headers = 'keys', tablefmt = 'pretty'))
  
def new():
  id = DigC('Masukkan ID: ')
  id = checklenid(id)
  uname = ADC('Masukkan username: ')
  uname = checkusername(uname)
  pin = ADC('Masukkan 4 Digit PIN: ')
  pin = checkpin(pin)
  book = input('Masukkan Judul Buku: ').title().replace("'S","'s")
  date = input('Masukkan Tanggal Baca (DD/MM/YYYY): ')
  date = checkdate(date)
  nama = AlpC('Masukkan Nama: ')
  gender = input('Masukkan Jenis Kelamin (P/L): ').title()
  gender = checkgender(gender)
  usia = DigC('Masukkan Usia: ')
  kota = AlpC('Masukkan Kota: ').title()
  new_data = {'ID': id, 'username': uname, 'PIN': pin, 'latestReadBook': book, 'latestReadDate': date, 'Nama Lengkap': nama, 'Gender': gender, 'Usia': usia, 'Kota': kota}
  database.append(new_data)
  check(database)

### THIS IS REINPUT FUNCTION ###
def more_no(foo: str = 'Tambah Data'):
  more = input(f"Apakah Anda ingin melakukan {foo} lagi? (Y/n): ").title()
  if more.lower() in ['ya', 'y', 'yes']:
    return True
  else:
    return False

def edit():
    while True:
        id_suffix = input('Masukkan 4 Digit ID terakhir yang ingin diganti: ')
        found = False
        for index, data in enumerate(database):
            if data['ID'].endswith(id_suffix):
                found = True
                key = AlpC('Masukkan Jenis Keys yang ingin diganti (username/PIN/Nama Lengkap/Gender/Usia/Kota/Book/Date): ').lower()
                if key in ['username', 'pin', 'nama lengkap', 'gender', 'usia', 'kota', 'book', 'date']:
                    if key == 'username':
                        uname = ADC('Masukkan username: ')
                        database[index]['username'] = uname
                    elif key == 'pin':
                        pin = ADC('Masukkan 4 Digit PIN: ')
                        if len(str(pin)) == 4:
                            database[index]['PIN'] = pin
                        else:
                            print('PIN harus terdiri dari 4 digit.')
                            continue
                    elif key == 'book':
                        book = input('Masukkan Judul Buku: ').title().replace("'S", "'s")
                        database[index]['latestReadBook'] = book
                    elif key == 'date':
                        date = input('Masukkan Tanggal (DD/MM/YYYY): ')
                        date = checkdate(date)
                        database[index]['latestReadDate'] = date
                    elif key == 'nama lengkap':
                        nama = input('Masukkan Nama: ')
                        database[index]['Nama Lengkap'] = nama
                    elif key == 'gender':
                        gender = AlpC('Masukkan Jenis Kelamin (P/L): ').title()
                        if gender.lower() in ['p', 'l']:
                            database[index]['Gender'] = gender
                        else:
                            print('Jenis Kelamin harus P/L.')
                    elif key == 'usia':
                        usia = DigC('Masukkan Usia: ')
                        database[index]['Usia'] = usia
                    elif key == 'kota':
                        kota = input('Masukkan Kota: ').title()
                        database[index]['Kota'] = kota
                    check(database)
                    if not more_no('edit'):
                        return 
                else:
                    print('Input Invalid!')
        if not found:
            print('ID tidak ditemukan!')
        
def remove_data():
    id_suffix = input('Masukkan 4 Digit ID terakhir yang ingin dihapus: ')
    found = False
    for data in database:
        if data['ID'].endswith(id_suffix):
            database.remove(data)
            found = True
            break
    if found:
        print('Data berhasil dihapus.')
    else:
        print('ID tidak ditemukan!')
    check(database)

def filter_data():
  while True:
    filter_choice = input("Filter berdasarkan (ID/Nama/Gender/Usia/Kota/Book/Date): ").lower()
    if filter_choice not in ['id', 'nama', 'gender', 'usia', 'kota', 'book', 'date']:
      print("Pilihan filter tidak valid. Silakan pilih dari: ID, Nama, Gender, Usia, Kota, Book, Date")
      continue
    if filter_choice == 'usia':
      try:
        age_range = input("Masukkan rentang usia (misal: 20-30): ")
        age_min, age_max = map(int, age_range.split('-'))
      except ValueError:
        print("Format rentang usia tidak valid. Silakan masukkan dalam format 'min-max'.")
        continue
      filtered_data = [entry for entry in database if age_min <= int(entry['Usia']) <= age_max]
    elif filter_choice == 'nama':
      filter_value = input(f"Masukkan nilai filter untuk {filter_choice}: ").title()
      filtered_data = [entry for entry in database if filter_value in entry['Nama Lengkap']]
    elif filter_choice == 'Book':
      filter_value = input(f"Masukkan nilai filter untuk {filter_choice}: ").title()
      filtered_data = [entry for entry in database if filter_value in entry['latestReadBook']]
    elif filter_choice == 'Date':
      try:
        date_range = input("Masukkan rentang tanggal (misal: 15/01/2024-12/31/2024): ")
        date_min, date_max = date_range.split('-')
        date_min = datt.strptime(date_min, '%d/%m/%Y').date()
        date_max = datt.strptime(date_max, '%d/%m/%Y').date()
      except ValueError:
        print("Format rentang tanggal tidak valid. Silakan masukkan dalam format 'dd/mm/yyyy-dd/mm/yyyy'.")
        continue
      filtered_data = [entry for entry in database if date_min <= datt.strptime(entry['latestReadDate'], '%d/%m/%Y').date() <= date_max]
    else:
      filter_value = input(f"Masukkan nilai filter untuk {filter_choice}: ").title()
      filtered_data = [entry for entry in database if entry[filter_choice.capitalize()] == filter_value]
    if filtered_data:
      check(filtered_data)
    else:
      print("Tidak ada data yang sesuai dengan filter.")
    if not more_no('filter'):
      break

def main():
   while True:
    print('''
    \tEntry Perpustakaan +26 Skopus
    
    Masukkan Program:
    1. Lihat Data
    2. Tambah Data
    3. Edit Data
    4. Hapus Data
    5. Filter Data
    6. Exit
          
    ''')

    inputan = DigC('Masukkan Pilihan: ')
    if str(inputan) == '1': #udah oke
      check(database)
    elif str(inputan) == '2': #udah oke
      new()
    elif str(inputan) == '3': #sudah oke
      edit()
    elif str(inputan) == '4': #udah oke
      remove_data()
    elif str(inputan) == '5': #sudah oke
      filter_data()
    elif str(inputan) == '6': #udah oke
      break
    else:
      print('Pilihan tidak ada!')

main()
