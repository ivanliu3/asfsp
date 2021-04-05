# asfsp

## Get started
This is a package used for calcualting various population genetics
statistics based on site frequency spectrum (SFS) and doing basic operations
on SFS. It is still under development.


## Install
```
git clone https://github.com/ivanliu3/asfsp
cd asfsp
python setup.py install --user
```

## Usage example:
0 help information
```
python asfsp.py -h
```

1.1 Calculate Hudson's Fst for 2dSFS
```
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 11,7 --calc fst
```

1.2 Calculate dXY for 2dSFS
```
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 11,7 --calc dxy
```

1.3 Calcualte pi for 1dSFS
```
python asfsp.py --input ./tests/example_1d_21.sfs --dim 21 --calc pi
```

1.4 Calculate Watterson's theta for 1dSFS
```
python asfsp.py --input ./tests/example_1d_21.sfs --dim 21 --calc theta
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors
* **Xiaodong Liu**  -*liuxiaodong.uu@gmail.com*
