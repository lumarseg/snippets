#!/bin/bash

conda update -n base -c defaults conda -y
conda env create --file environment.yaml