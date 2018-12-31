# Pdf Split & Merge

Simple tool to split and merge multiple pdf files at once

## Install

```
pip3 install git+https://github.com/gaborvecsei/pdf-split-merge.git
```

## Usage

Write a config file like this (`sample_config.txt`):

```
D:/my_folder/my_pdf_1.pdf 1-10,16,22
D:/my_folder/my_pdf_23.pdf 1-40
D:/my_folder/my_pdf_4.pdf 6,8,9-20

```

This means it will process the files sequentially top-down and include only the defined
pages in the final pdf document.

```
pdfsm -i sample_config.txt -o split_and_merge.pdf
```

You can use different file encoding:

```
pdfsm -i sample_config.txt -o split_and_merge.pdf -e utf8
```

## About

Gábor Vecsei

- [Website](https://gaborvecsei.com)
- [Personal Blog](https://gaborvecsei.wordpress.com/)
- [LinkedIn](https://www.linkedin.com/in/gaborvecsei)
- [Twitter](https://twitter.com/GAwesomeBE)
- [Github](https://github.com/gaborvecsei)
