# asfsp

## Get started
This is a package used for calcualting various population genetics
statistics based on site frequency spectrum (SFS) and doing basic operations
on SFS. It is still under development.


## Install
```
git clone https://github.com/ivanliu3/asfsp
cd asfsp
python setup.py install
```

## Usage example:
--dim/-D should be the number of haploid alleles in the population(s). See example below

0 help information
```
python asfsp.py -h
```

1.1 Calculate Hudson's Fst for 2dSFS
```
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 10,6 --calc fst
```

1.2 Calculate dXY for 2dSFS
```
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 10,6 --calc dxy
```

1.3 Calcualte pi for 1dSFS
```
python asfsp.py --input ./tests/example_1d_21.sfs --dim 20 --calc pi
```

1.4 Calculate Watterson's theta for 1dSFS
```
python asfsp.py --input ./tests/example_1d_21.sfs --dim 20 --calc theta

```

2.1 Marginalize 2dSFS to 1dSFS
```
# for the first population
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 10,6 --oper margin1

# for the second population
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 10,6 --oper margin2
```
2.2 Print SFS
```
python asfsp.py --input ./tests/example_2d_11_7.sfs --dim 10,6 --oper print
```

2.3 Plot SFS
```
python asfsp.py --input  ./tests/example_2d_11_7.sfs --dim 10,6 --oper plot
```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors
* **Xiaodong Liu**  -*liuxiaodong.uu@gmail.com*

## Acknowledgement
Many thanks to Casia Nursyifa and Genis Garcia-Erill for the help with testing the codes.
