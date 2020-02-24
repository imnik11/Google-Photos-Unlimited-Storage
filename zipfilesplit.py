outfile = "Google CTF 2017 Quals Write-up Winners-20200126T092515Z-001.mp4"
packet_size = int(15 * 1024**2)   # bytes

with open(outfile, "rb") as output:
    filecount = 0
    while True:
        data = output.read(packet_size)
        print(len(data))
        if not data:
            break   # we're done
        with open("{:03}{}".format(filecount , outfile ), "wb") as packet:
            packet.write(data)
        filecount += 1
