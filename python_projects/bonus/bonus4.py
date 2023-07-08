filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)  # 1 represents the first occurrence
    print(filename)