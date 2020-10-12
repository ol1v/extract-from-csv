import pandas as pd

df = pd.read_csv('query_data.csv')
ip = df.iloc[:, 12].values
port = df.iloc[:, 11].values

unfiltered_ips = open("unfiltered_ips.txt", 'w')

counter = 0

try:
    for i, p in zip(ip, port):
        unfiltered_ips.write(str(i))
        unfiltered_ips.write("\t")
        unfiltered_ips.write(str(p))
        unfiltered_ips.write("\n")

finally:
    unfiltered_ips.close()
