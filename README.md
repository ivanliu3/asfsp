# asfsp

This is a package used for calcualting various population genetics
statistics based on site frequency spectrum (SFS) and doing basic operations
on SFS. It is still under development.


Usage:
# help information
python asfsp.py -h

# Calculate Hudson's Fst for 2dSFS
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 11,7 --calc fst

# Calculate dXY for 2dSFS
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 11,7 --calc dxy

...
