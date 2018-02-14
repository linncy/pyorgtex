# pyorgtex
A Python package which integrates Python, Emacs, OrgMode and Latex into one robust system for reproducible research.

## convert
Used for data format conversion.
### csv2dict(CSVname)
csv2dict(CSVname)
Read CSV and convert it into dict.
### fdf2csv(FDFname)
Read FDF and convert it into dict.
### json2dict(JSONname)
Read JSON and convert it into dict.
### dict2json(jsondict,JSONname)
Convert dict into json and write it as .json.
### extractFilename(path)
Extract file name from path.
### eclass2dict(eclassXLSname)
Read XLS downloaded from eclass and create initial classjson.

## orgexport
Evaluate all code blocks and export .org as PDF/HTML/LaTeX/ASCII .
### export2pdf(ORGname)
Evaluate all code blocks and export .org as PDF.
### export2tex(ORGname)
Evaluate all code blocks and export .org as tex.
### export2html(ORGname)
Evaluate all code blocks and export .org as HTML.
### export2ascii(ORGname)
Evaluate all code blocks and export .org as ASCII.

## generate
Generate desired files for reproducible research in batches.
### generate_from_classjson(JSONname,ORGname,exportformat='pdf',dirname='./',dependencylist=[])
Read classjson and generate files according to classjson.
### generate_from_par(dictPar,ORGname,format='pdf',dirname='./',dependencylist=[])
Generate files according to given dictPar.
