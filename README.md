# Klagen gegen Entscheidungen des BAMF

> Rechtsmitteln und Gerichtsentscheidungen im Bereich Asyl

Datathon 27.10.2018

## Prep

- Get [Tabula](https://tabula.technology/) and [tabula-java](https://github.com/tabulapdf/tabula-java/releases) (the table extraction engine behind Tabula, which can also be used as a command-line tool).

## Data

- Search `Asylstatistik Gerichtsentscheidungen` on [kleineanfragen.de](https://kleineanfragen.de/search?q=Asylstatistik%20Gerichtsentscheidungen&sort=published_at:desc) to get all the PDFs;
- The search returned 24 files from 2013Q3 till today (2018Q2).
  - Only statistics for Q1-Q3 but **no Q4** each year are provided;
  - Instead the **whole year** statistics were also published;
  - During the years, several items were added to the statistics, so the recent publications are a little bit more detailed than the first ones;
  - Small **format changes** were also made.

## Extraction with Adobe Acrobat

Adobe Acrobat has a well optimized engine for PDF to Word / Excel conversion. However **Acrobat Standard or Pro is required** (not Acrobat Reader). Batch conversion is available in Acrobat Pro.

We converted the yearly reports from 2013-2017 to MS Word files and imported the tables for `Erst- und Folgeanträge` from 2015-2017 to the Excel file **`Gerichtsentscheidungen.xlsx`**. Note that starting 2017 `Klagen`, `Berufungen` and `Revisionen` are listed separately.

Tips:
You may need to change the number separators to english format. To do it in MS Word, replace `.([0-9][0-9][0-9])` with `\1` and `,([0-9])%` with `.\1%`.
  
## Extraction with Tabula 1.2.1

The tables in the published statistics are well recognizable in Tabula. It could be easier with Tabula if we want to process more files (like the quarterly reports) or build an automatic solution.

- Run and browse to Tabula;
- **Import** PDF files;
- Click **Extract Data**;
- On the "Select Tables" page select **Autodetect Tables** and click **Preview**;
- On the "Preview of Extracted Tabular Data" page change **Extraction Method** to **Lattice** and **Export Format** to **zip of CSVs**;
- Click **Export** to download the CSV files.

This procedure will export everything recognized as a table by Tabula to a CSV file and thus generate a lot of CSV files. Now we need to do a full-text search with `,Gerichtsentscheidungen,` to find out the files we really need.

Check **`Gerichtsentscheidungen`** folder for the files.

Problem: It seems to **work well with recent reports** but some CSV files from older reports contain non-matching extra columns / rows which need to be removed manually.

### Attempt at automatization with tabula-java

Extract the whole PDF into CSV using the [command line](https://github.com/tabulapdf/tabula-java/blob/master/README.md) ([Wiki](https://github.com/tabulapdf/tabula-java/wiki/Using-the-command-line-tabula-extractor-tool#download-tabula-java)):

    java -jar tabula-1.0.2-jar-with-dependencies.jar -g -p all -o test.cvs ../Datathon/kleine-anfrage1904961.pdf

Then extract the relevant table using the command line:

    sed -n '/Klagen.*Gerichtsentscheidungen/,/Erst/p' test > test.csv

(grep cannot specify beginning and end using keywords)

Same problem with extra columns, even worse. tabula-java saves all tables found to one single CSV file, resulting in misalignments.

An alternative may be exporting into JSON:

    java -jar .tabula-1.0.2-jar-with-dependencies.jar -g -p all -o test.json -f JSON ../Datathon/kleine-anfrage1904961.pdf

## Data Cleanup

[OpenRefine](http://openrefine.org/) may be helpful.

## Infographics with Datawrapper

We cleaned up the `Klagen` data for `Gerichtsentscheidungen` in 2017 and made a demo graph with Datawrapper:
https://datawrapper.dwcdn.net/OJiFm/

---

> @kjc66 and @onefork contributed to this document.
