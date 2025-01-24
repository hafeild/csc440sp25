# CSC440 Data Mining and Visualization, Spring 2025

## Contents

  * `data` -- this is a place to put datasets; no datasets are included in the
              repository since they are not code and take up a lot of space;
              datasets that various scripts rely on are described below, as
              well as how to obtain them.
  * `notebooks` -- contains Jupyter Notebooks for performing analyses.
  * `scripts` -- contains stand alone Bash and Python scripts for processing data.


## Datasets

## `apache-logs`

This is a set of access logs from 2017-2023 from my personal server.

You can access this from the [pcloud folder for the class](https://u.pcloud.link/publink/show?code=kZahQF5ZqbGUH6iD57LfwTPNEAY6uui2G7qy)
in `data/apache-logs.tbz`. It's a bzipped tarball, so after downloading it
to the `data` directory, run this command to extract it:

```bash
tar xjf apache-logs.tbz
```

