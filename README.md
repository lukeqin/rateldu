# Rateldu

Summarize disk usage of each FILE of linux platform, based on ncdu command, default unit is Byte. Default directory is current directory.

# Install
* Install ncdu tool.
1. CentOS 6 and CentOS 7: yum install -y ncdu
2. https://dev.yorhel.nl/ncdu

* Install rateldu.
1. Install python3, and argparse for python3.
2. Use binary file builed by PyInstaller for CentOS 6 and 7, download from https://github.com/lukeqin/rateldu/releases

# Usage
usage: rateldu [directory] [options]

Summarize disk usage of each FILE, based on ncdu command, default unit is Byte. Default directory is current directory.

positional arguments:

  d                     test

optional arguments:

  -h, --help            show this help message and exit
  
  -s S, --sort-number S
                        default sort by file size, display the first number
                        files after sorted by size (-s5)
                        
  -u, --human-readable  print sizes in human readable format (e.g., 1K 234M
                        2G)
                        
  -o O, --output O      export scanned directory to FILE
  
  -x E, --exclude E     exclude files that match PATTERN
  
  -v, --version         show program's version number and exit
  

SIZE is an integer and optional unit (example: 10M is 10*1024*1024). Units are K, M, G, T, P, E, Z, Y (powers of 1024) or KB, MB, ... (powers of 1000).

# Test
1. 5212708 files.
time ./rateldu -u / -x /var -o log 
Namespace(d='/', e='/var', o='log', s=0, u=True)

Toal file: 5212708

real    1m55.898s
user    1m6.264s
sys     0m9.238s

2. 219395 files.
Namespace(d='/', e=None, o='log', s=0, u=True)

Toal file: 219395

real    0m41.484s
user    0m4.003s
sys     0m0.388s

3. 1367 files.
Toal file: 1367

real    0m0.152s
user    0m0.104s
sys     0m0.028s
