first of all, install requirements:

    pip3 install  -r requirements.txt


run this to get headers from [here](http://h.bilibili.com/)

    python3 comic.py beginIndex endIndex

Example:
search headers from http://h.bilibili.com/dy10 to http://h.bilibili.com/dy100:

    python3 comic.py 10 100

--------------------------------
search covers:

    python3 example.py beginIndex endIndex minScore


Example:
search covers from http://h.bilibili.com/dy10 to http://h.bilibili.com/dy100 which score are higher than 7:

    python3 example.py 10 100 7
