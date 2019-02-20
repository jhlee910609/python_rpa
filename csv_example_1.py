from os import listdir

csv_file = '/Users/JunHee/Desktop/python_book/examples/05/csv_files/'
file_list = listdir(csv_file)
file_list.sort()

write_file = open(csv_file + '매출_통계.csv', 'w')
write_file.write('년월,매출\n')

for name in file_list:
    if name[-3:] != 'csv':
        continue

    sum = 0
    f = open(csv_file + name, 'r')

    while True:
        row = f.readline()
        if not row:
            break

        data = row.split(",")
        if data[1].isdigit():
            sum = sum + int(data[1])

    print("sum => %d"%(sum))
    write_file.write('%s, %d\n'%(name[:7], sum))
    f.close()

write_file.close()


