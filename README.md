Code comment matcher
----------------
Script matching comments in a git repository source code to a predefined set of patterns.

Dependencies
----------------
This script relies on the following packages:
 * GitPython==2.1.5
 * comment-parser==1.0.3

To check and install the dependencies simply run the command `pip install -r requirements.txt`

Usage
----------------
From the root directory execute:
`python parse.py`

Input
----------------
The script takes as input the file `patterns.txt`, in which the patterns to be matched are specified.

Output
----------------
The output of the script is stored in the file `output_parsing.tsv`, which contains the source code comments matching the patterns.
The three columns of the output file are:
 * File name: Location of the souce code file in which the matched comment appears
 * Keyword: Pattern keyword(s) contained in the matched comment
 * Comment: Content of the matched source code comment

Notes
----------------
 * The got repository to be analyzed is currently hardcoded in the script. Change the variable `git_repository_url` to utilize a different repository.
 * The language of the repository has to be specified in the MIME type variable `MIME`. For the mapping of languages to MIME types refer to the documentation of the [comment_parser](https://pypi.python.org/pypi/comment_parser/1.0.3) package.
 * Extensions types of the files to be considered during the parsing have to be specified in the extension variable `extensions`

* Currently supported languages:
  * C
  * C++
  * Go
  * Java
  * Javascript
  * Bash/Sh
  
Credits and license
----------------
Author: 
* Roberto Verdecchia (roberto.verdecchia@gssi.it)

Sample patterns were taken from the dataset of the research "An Exploratory Study on Self-Admitted Technical Debt" by Potdar et. al available [here](http://users.encs.concordia.ca/~eshihab/data/ICSME2014/satd.html).

This project is licensed under the MIT License - see the file `license.txt`
