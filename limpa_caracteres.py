import csv

with open('Ger_semanal.csv', errors='ignore') as csv_file_object:
    reader_obj = csv.reader(csv_file_object)
    csv_rows = [row for row in reader_obj]
    print(len(csv_rows))
    print(csv_rows[:10])
    with open('arquivo_tratado.csv', 'w') as writer_obj:
        out_writer = csv.writer(writer_obj, delimiter=';',quoting=csv.QUOTE_ALL, lineterminator='\n')
        for row in csv_rows:
            out_writer.writerow(row)