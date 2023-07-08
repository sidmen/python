contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents, filenames):  # zip() merges the lists and creates a list of tuples
    file = open(f"../files/{filename}", 'w')  # the files are automatically created
    file.write(content)

