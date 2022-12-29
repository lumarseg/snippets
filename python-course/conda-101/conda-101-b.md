# CONDA-102

## Let`s create a new env

Example 1:

```bash
conda create --name py39 python=3.9 pandas=1.2
conda activate py39
```

## Install a package from a specific channel

Example 2:

```bash
conda install --channel conda-forge boltons
```

## List Install Revisions

Example 3:

```bash
conda list --revision
```

## Rollback a previus revision

Example 4:

```bash
conda install --revision 0
```

## Export env

Example 5:

```bash
conda env export --no-builds
```

Example 6:

```bash
conda env export --from-history
```

Example 7:

```bash
conda env export --from-history --file environment.yaml
```

## Import env

Example 8:

```bash
conda env create --file environment.yaml
```
