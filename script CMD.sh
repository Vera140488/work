#!/bin/bash

mkdir -p ./1/2/
cd 1
touch f1 f2 f3 f4 f5
cp f* 2/
rm f*
