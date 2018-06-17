# rateldu

usage: rateldu [directory] [options]

Summarize disk usage of each FILE, based on ncdu command, default unit is
Byte. Default directory is current directory.

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

SIZE is an integer and optional unit (example: 10M is 10*1024*1024). Units are
K, M, G, T, P, E, Z, Y (powers of 1024) or KB, MB, ... (powers of 1000).

