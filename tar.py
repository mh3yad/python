import tarfile
i=1000
while 1 > 0:
        tf=tarfile.open(str(i) + ".tar")
        tf.extractall()
        print("file" + str(i) + ".tar is extracted")
        i -=1


