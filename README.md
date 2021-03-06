# Rateldu

Summarize disk usage of each FILE of linux platform, based on ncdu command, default unit is Byte. Default directory is current directory.

# Install
* Install ncdu tool.
1. CentOS 6 and CentOS 7:  yum install -y ncdu
2. Other linux: https://dev.yorhel.nl/ncdu

* Install rateldu.
1. python3 rateldu.py: Install python3, and argparse for python3.
2. ./rateldu: Use binary file builed by PyInstaller for CentOS 6 and 7, download from https://github.com/lukeqin/rateldu/releases

# Usage
usage: rateldu [directory] [options]

Summarize disk usage of each FILE, based on ncdu command, default unit is Byte. Default directory is current directory.

positional arguments:

  d                     directory

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

4. 6688192 files, file size is 535MB.

Namespace(d='/', e=None, o='log', s=0, u=True)

Toal file: 6688192

real    2m27.138s
user    1m30.821s
sys     0m15.475s

5. 9713047 files.

time ./rateldu-centos6 -u -olog -x data1 /
Namespace(d='/', e='data1', o='log', s=0, u=True)

Toal file: 9713047

real    9m5.072s
user    3m23.103s
sys     0m28.346s

# Bug and feature

* Display files the size over specified size.
* Exclude files that match any pattern in FILE, use ncdu --exclude-from FILE.
