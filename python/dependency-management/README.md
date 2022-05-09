# Dependency Management Tutorial
Versions
```bash
conda 4.12.0
conda-lock 1.0.5
```

## Overview
The primary takeway here is that you want to think of your dependencies as two kinds: (1) [_direct dependencies_](#direct-depedency) and (2) [_transitively pinned dependencies_](#transitively-pinned-dependencies). Loose definitions are at the bottom of this page. I owe the majority of my understanding to [Itamar Turner-Trauring at Python⇒Speed](#resources) but it also took a lot of messing about [conda-lock](#resources) to get things just right.

## Asumptions
1. You are using conda to manage your environment and packages (avoid pip and use the conda channel `conda-forge` always and forever)
2. I am using a really example where there is some application we are trying to make reproducible and upgradeable
```bash
.
└── app.py
```
```python
# ./app.py
import pandas as pd
```
3. I prefer to install `conda-lock` into my `(base)` enviroment since it helps me manage packages, but that is up to you. For this tutorial, it is assumed you have it installed in `(base)`:
```bash
(base) $ conda install -c conda-forge conda-lock=1.0.5
```

## Walkthrough
### Locking dependencies for a new project:
As you run multiple `conda install -c conda-forge <package>=<version>`, you can rest certain that, once you have installed the minimum number of direct dependencies to get your project moving, you can run the following to get your `environment.yml` file:
```bash
$ conda env export --from-history > environment.yml
```
The nice thing about the `--from-history` flag is that it only takes into account your _direct dependencies_. However, if you did not specify versions when you explicity ran the  `conda install` command, you will need to add versions of your _direct dependencies_ manually to your `environment.yml`. You can use `conda list` for this:
```bash
$ conda list | grep <package>
```
You may prefer a more programatic way of accomplishing the above.

Warning: `--from-history` not work from an imported environment since your imported environment treats all dependencies as direct.

### Locking dependencies for an existing project:
1. If you already have a python application you are trying to make reproducible and upgradeable, it is wise to start from scratch to get all of your direct dependencies right first. Create a file named `environment.yml` and put this inside:

```yaml
name:
channels:
  - conda-forge
dependencies:
```

2. Install one of your known direct dependecies (e.g., `conda install -c conda-forge pandas`)
3. Try to run your app. Errors? Repeat Steps 2-3 until you can. Otherwise, move on.
4. The installs you just did were for your direct dependencies. We want to make sure we specify their versions (including which Python we are using) in the `environment.yml`. You can quickly get this info by running the command `conda list | grep <package_name>`. It might look something like this:

```yaml
name:
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pandas=1.4.2
```

5. Fill in that name: with the name of the environment you want to create. Let's use `name: dependency-demo` for this walkthrough.
6. Now that your direct dependency file is filled, and your app is working, we can now take care of transitively pinned dependencies which is a fancy way of saying we're going to lock down all dependencies exactly where they are (rememeber, there are dependencies underneath your direct dependencies). As of the writing of this tutorial, `conda-lock` was undergoing some doc updates, so this may change but it was hard to figure out in the current state of things. You want to create a lock file from your direct dependency `environment.yml` file. We will leave out Windows os and do this: `conda-lock -f environment.yml`. This step creates a file called `conda-lock.yml` which represents your transitively pinned dependencies file.
### Importing from locked environment:
#### From `.lock` file
```bash
TBD
```
#### From .yml file
```bash
$ conda-lock install -n <whatever_env_name_you_want>
...
$ conda activate <the_env_name_from_above>
```
# Terms

#### direct depedency
1. a dependency that is directly imported to run <br>
    \\\\ e.g., import pandas as pd means pandas is a direct dependency  <br>
    \\\\ in the above example, pandas depends on numpy, but numpy is not a direct dependency here

#### transitively pinned dependencies
1. when the dependency of a dependency is pinned (i.e., locked)  <br>
    \\\\ in the above example with pandas, numpy would need to be transitively pinned
    
# Resources
* pythonspeed — [Reproducible and upgradable Conda environments with conda-lock](https://pythonspeed.com/articles/conda-dependency-management/)
* conda-lock — [github repo](https://github.com/conda-incubator/conda-lock)
