CSS_Extractor
=============

CSS Extractor: is a set of python scripts for reading and extracting css code from list of URL sites.

The main goal of these scripts is to automate reading and extacting wanted css codes from may sites.

Also provided scripts for statistcal analysis f overall css code.


List of scripts:

1.ExternalCSSFinder.py -> Finds and saves all external css links in given list of sites (reportExternalCSS.txt)

2.InternalCSSFinder.py -> Finds and saves all inlince css in given list of sites (reportInlineCSS.txt)

3.ExtCSSParser.py -> Reads list of urls that point to css files and saves css files (reportExtAll.txt)

4.BeutifyCSS.py -> Reads all css files from previous steps and creates a new file without css declarations

5.Criteria.py and CriteriaCSS.py provide statistics about the selectors that are actually used.


In CSSDB.txt we provide all css selectors of 100 first Alexa sites.

/*ExternalCSSFinder and IntenalCSSFinder.py use Selenium automation library!

/*All the folder can imported in eclipse folder and those scripts can be run automated in the above order to produse css results
