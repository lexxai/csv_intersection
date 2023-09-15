#   csv intersection
Intersection of two csv files by a key column. 

Where column is a string with the file name. 

Result saved to new csv file. 

### help

```
main.py [-h] [-V] [--work WORK] --input1 INPUT1 --input2 INPUT2 [--output OUTPUT] [--input1_key_idx INPUT1_KEY_IDX] [--input2_key_idx INPUT2_KEY_IDX] [--verbose]

options:
  -h, --help            show this help message and exit
  -V, --version         show version of app
  --work WORK           Directory for work. Is prefix for all other directories that is not absolute, default ''
  --input1 INPUT1       Path to input1 file (main)
  --input2 INPUT2       Path to input2 file (reference)
  --output OUTPUT       Path for output file, default 'output.csv'
  --input1_key_idx INPUT1_KEY_IDX
                        Key index for input1, default 0
  --input2_key_idx INPUT2_KEY_IDX
                        Key index for input2, default 1
  --verbose             verbose output
```



### result 

```
1

```