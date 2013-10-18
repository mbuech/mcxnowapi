x = open("hello.txt", "r").read()
print x.split("BTC</tla><balavail>")[1].split("</baltotal><btctotal>")[0].split("<")[0]
y = open("hello.txt", "r").read()
print y.split("PPC</tla><balavail>")[1].split("</baltotal><btctotal>")[0].split("<")[0]	