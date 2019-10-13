## Updating the numbers: 2018 Q3 to 2019

Taking some notes, to make my job easier next time
Manually look for the reports
Our last article had data until mid 2018

2018 Q3:
http://dipbt.bundestag.de/dip21/btd/19/067/1906786.pdf

2018 all year:
http://dipbt.bundestag.de/dip21/btd/19/087/1908701.pdf

2019 Q1:
http://dipbt.bundestag.de/dip21/btd/19/110/1911001.pdf

First, do the 2018 all year data. Extract the table on page 44. The last rows look broken.

Done manually in tabula, chose Lattice, clean the worst to produce
`2018_klagen.csv, 2018_berufungen.csv, 2018_revisionen.csv`

Remove thousand separating dots.
When it is csvclean, cut the columns of interest with `csvcut -c 1,4,5,6,7,8,10 2018_klagen.csv`, and produce your chart.
To identify countries with less than 1000 real decisions - those do not go into the percentage picture - we have to subtract the "sonstige Erledigungen" from the total number of decisions. Turning to python pandas for this:

```
import pandas as pd
df = pd.read_csv("./2018_klagen.csv")
print(df.columns.values)
df_all_dec_nixsonst=df[' Gerichtsentscheidungen gesamt']-df[' sonst. Verfahrenserledigungen (z.B. Ruecknahmen) absolut']
df.merge(df_all_dec_nixsonst.to_frame(),left_index=True, right_index=True).sort_values(0)
```






