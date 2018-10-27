Datathon 27.10.2018

Kleine Anfrage der Linken Gerichtsentscheide Asyl

Downloaded pdf file
Installed tabula
Used tabula to extract relevant table into csv
Problem: csv file contains non-matching extra columns which need to be removed manually
Converted csv to excel

Attempt at automatization:
Extract the whole pdf into csv using the on the commandline
java -jar tabula-1.0.2-jar-with-dependencies.jar -g -p all -o test.cvs ../Datathon/kleine-anfrage1904961.pdf
Then extract relevant table using on the commandline
sed -n '/Klagen.*Gerichtsentscheidungen/,/Erst/p' test > test.csv
(grep cannot specify beginning and end using keywords)
Same problem with extra columns, even worse.

Easier solution:
Opened pdf file with acrobat reader and exported as word
Opened in word and exported as excel
This works better, but cannot be automatized


