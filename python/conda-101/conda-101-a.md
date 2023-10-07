# CONDA-101

**Conda** is a package manager for the Python programming language that is used to manage and deploy packages and environments. It is a tool that is part of the Anaconda distribution, which is a popular distribution of Python that includes many of the most commonly used packages for scientific computing and data analysis.

## Create a New Environment

Example 1: It will create a new env named "py-01", installing the last version of Python and Pandas package.

```bash
conda create --name py-01 python pandas
```

Example 2: It will create a new env named "py35", installing Python 3.5

```bash
conda create --name py35 python=3.5
```

## Activate an environment

Example 3: It will activate the env named "py-01"

```bash
conda activate py-01
```

## Deactivate an environment

Example 4: It will deactivate the currente env.

```bash
conda deactivate
```

## Check version of all packages

Example 5: It will list all packages and its versions.

```bash
conda list
```

## Check version of a specific package

Example 6: It will display the version of a specific package, i.e. Pandas Package.

```bash
conda list pandas
```

## Update version of a specific package

Example 7: It will update the version of a specific package to the last version, i.e. Pandas Package.

```bash
conda update pandas
```

## Update version of Conda

Example 8: It will update the version of Conda

```bash
conda update -n base -c defaults conda
```

## Install a package in the current env

Example 9: It will install a new package in the current env, i.e. Pandas version 1.2

```bash
conda install pandas=1.2
```

## Install or Update ???

Sometimes is needed to update a specific version of a package that the current version of Python is not supported. In that scenario, "update" command is not capable to update the version. So "install" command is the option to update a forced instalation.

Example 10: It will update the currente version of Python to 3.9, and Pandas to 1.2

```bash
conda install python=3.9 pandas=1.2
```

## Copy Env

Example 11: It will copy and clone a env.

```bash
conda create --name py39 --copy --clone py35
```

## Remove a package

Example 12: It will remove a package, i.e. remove Pandas

```bash
conda remove pandas
```

## Remove an env

Example 13: It will remove a env, i.e. remove env py35

´´´bash
conda env remove --name py35
´´´
