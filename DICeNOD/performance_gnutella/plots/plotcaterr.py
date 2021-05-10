import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("errortable_m.csv", header=0)
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
plt.plot(df['m'], df['caterr'], color='red',
         marker='.', label="Categorization Error vs m with d=100")
plt.title("CatERR vs m with d=100 [dataset=GNUTELLA]")
plt.xlabel("m : Number of measurements")
plt.ylabel("CatERR: Number of mismatches with TopK indices")
plt.legend(loc='upper right')
plt.savefig("CatERRvsM_gnu.jpg",dpi=600)

df = pd.read_csv("errortable_d.csv", header=0)

fig = plt.figure()
plt.plot(df['d'], df['caterr'], color='red',
         marker='.', label="Categorization Error vs m with m=3000")
plt.title("CatERR vs d with m=3000 [dataset=GNUTELLA]")
plt.xlabel("d: # non-zero elements in each column of the measurement matrix")
plt.ylabel("CatERR: Number of mismatches with TopK indices")
plt.legend(loc='upper right')
plt.savefig("CatERRvsD_gnu.jpg",dpi=600)