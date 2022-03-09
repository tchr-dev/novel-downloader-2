# novel-downloader 2
Novel-downloader is a simple Python 3 script to download web novel from  following sources:
1. https://lightnovelreader.org/

Currently, no support for other sources

Usage:
1. `$ python3 main.py -b https://lightnovelreader.org/i-reincarnated-but-will-try-to-live-without-using-my-cheat-ability -l https://lightnovelreader.org/i-reincarnated-but-will-try-to-live-without-using-my-cheat-ability/chapter-1`

Option `[-b]` will start creating book
Option `[-l]` will receive list of chapters from any available chapter in the novel

After downloading you will have html-like file

To convert it to **epub** or other useful format simply add extension **.html** first

Then install <a href="https://pandoc.org/installing.html">pandoc</a> and use following code:
`$ pandoc -o "Novel name.epub" "Novel name.html"`

09-03-2022