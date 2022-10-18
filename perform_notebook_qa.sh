#!/bin/bash

# script takes a Jupyter Notebook as argument and calls
# validation and static code analysis tools for this notebook

# usage help
usage() { 
  echo "Usage: $0 NOTEBOOK_TO_CHECK.ipynb" 1>&2 
}

# call tools for given notebook
perform_qa() {
  py.test --nbval $1
  nbqa isort $1
  nbqa black --line-length=79 $1
  nbqa flake8 $1
}

# check if command line argument is present
if [ "$#" -ne 1 ]; then
    echo "No notebook (.ipynb) was provided";
    usage;
    exit 1;
fi

perform_qa $1
