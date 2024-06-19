import pandas as pd


def excel_to_csv(excel_file_path, sheet_name, csv_file_path):
    # Membaca file Excel
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Menyimpan dataframe ke file CSV
    df.to_csv(csv_file_path, index=False)

    print(f"File Excel telah berhasil dikonversi menjadi file CSV di {csv_file_path}")


# Contoh penggunaan
excel_file_path = 'Jumlah Pasien Rawat Jalan Menurut Poli di RSUD.xlsx'
sheet_name = 'Sheet1'  # Nama sheet yang ingin dikonversi
csv_file_path = 'Jumlah Pasien Rawat Jalan Menurut Poli di RSUD.csv'

excel_to_csv(excel_file_path, sheet_name, csv_file_path)
