import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("errortable_m.csv", header=0)
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
plt.plot(df['m'], df['relmse'], color='red',
         marker='.', label="RelMSE vs m with d=100")
plt.title("RelMSE vs m with d=100 [dataset=GNUTELLA]")
plt.xlabel("m : Number of measurements")
plt.ylabel("RelMSE: Percentage Difference in l2-norm")
plt.legend(loc='upper right')
plt.savefig("RelMSEvsM_gnu.jpg",dpi=600)


df = pd.read_csv("errortable_d.csv", header=0)

fig = plt.figure()
plt.plot(df['d'], df['relmse'], color='red',
         marker='.', label="RelMSE vs d with m=3000")
plt.title("RelMSE vs d with m=3000 [dataset=GNUTELLA]")
plt.xlabel("d: # non-zero elements in each column of the measurement matrix")
plt.ylabel("RelMSE: Percentage Difference in l2-norm")
plt.legend(loc='upper right')
plt.savefig("RelMSEvsD_gnu.jpg",dpi=600)