# streamlit_vapor

Setup for this requires following https://www.vapor.ucar.edu/pages/vaporPythonDownloads.html

```
# probably need to do conda init, or source .bashrc first
conda create -n vapor_python


conda activate vapor_python


conda install -c conda-forge -c ncar-vapor vapor
pip install streamlit
ln -s $CONDA_PREFIX/lib/python3.9/site-packages/vapor/example_notebooks/ ex
ln -s $CONDA_PREFIX/lib/python3.9/site-packages/vapor/example_notebooks/ script_examples
cd script_examples
cp ../vapor_test.py .
streamlit run vapor_test.py
```


