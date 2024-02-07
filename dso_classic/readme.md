
## 2. Run DSR, PQT, VPG, GPMeld

### Our Modification
We add our dataoracle and remove the steps of loading a large ".csv" file to a active query API.



### 2.0 prequisites
Make sure you have alredy install the `anaconda` or `miniconda` in your computer.
1. install python environment 3.7 though conda : `conda create -n py37 python=3.7.16`.
2. use the environment `conda env py37`.
3. install `dso` software

```cmd
cd ./dso_classic/dso
pip install --upgrade setuptools pip numpy Cython
export CFLAGS="-I $(python -c "import numpy; print(numpy.get_include())") $CFLAGS"
pip install -e ./dso
```

4. pick one configuration file inside the `dso_classic/config` folder.



5. run `DSR`, `PQT`, `VPG`, `GPMeld` models.
   If you want to run DSR, PQT, VPG, GPMeld on **trigonometric** datasets.

You need to modify the values for `py37` and `basepath` in the file `/dso_classic/scripts/trigonometric/run_dso_series.desktop.sh`. 

After that, you can use any line of code inside `/dso_classic/scripts/trigonometric/onekey.sh`.

For example, going to the folder `/dso_classic/scripts/trigonometric/` and run the program by

`./run_dso_series.desktop.sh inv 2 11`