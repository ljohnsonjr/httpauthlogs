def getHosts(filename):
    fin = open(filename, "r")
    httpnames = {}
    for line in fin:
        line = line.split()
        httpname = line[0]
        if (httpname in httpnames):
            httpnames[httpname] += 1
        else:
            httpnames[httpname] = 1
        
    for hostname in httpnames:
        print(hostname,' - ',httpnames[hostname])

getHosts("httplog.txt")
