# test-driven-dev

## Operation

    1. Activate conda

```
conda activate swe4s
```
    2. Install matplotlib

```
conda install matplotlib
```

    3. Running viz.py
```
$ bash gen_data.sh | \
    python viz.py \
        --output_file_name test_file.png \
        --plot_type combo
```
        This will create a combonation boxplot and histogram with the file name "test_file.png"

## math_lib.py

    1. Created testing file test_math_lib.py
        - Created tests for None input
        - Created tests for null input
        - Created tests for non-list input
        - Created tests for empty list input
        - Created tests for array of ones
        - Created looped test for random integer array input
        - Created looped test for random float array input
        - Created test for invalid list elements
        - Created looped test for array with both intergers and floats


    2. Added calcuating functionality for math_lib.py
    
    3. Added error-catching for math_lib.py
        - Returns None given None
        - Throws TypeError given null input
        - Throws TypeError given non-list input
        - Returns None for empty list input

## get_data.py

    1. Created testing file test_get_data.py
        - Created test for None input
        - Created tests for null input
        - Created tests for non-int input
        - Created test to return constant input value
        - Created looped test to return randomized input values
    
    2. Added error-catching for get_data.py
        - Throws TypeError given null input
        - Throws TypeError given incorrect input
    
    3. Added column-return capabilities
        - Tested indpendently of unittest due to stdin input complexity

## data_viz.py

    1. Created testing file test_data_viz.py
        - Created test for None input
        - Created tests for null input
        - Created tests for non-int/float input
        - Created tests for invalid list elements
        - Created tests to ensure file creation

    2. Added error-catching for math_lib.py
        - Returns None given None
        - Throws TypeError given null input
        - Throws TypeError given non-list input
        - Returns None for empty list input
        - Returns None if file name is already used

    3. Added Plotting Features for data_viz.py
        - box plot with mean, stdev in title
        - histogram with mean, stdev in title
        - combo with mean, stdev in title

## viz.py

    1. Created script for visualizing piped data
        - Uses get_data.py to acquire date from stdin
        - Uses data_viz.py to create plots from data
        - Uses math_lib.py to calculate mean and stdev of data 