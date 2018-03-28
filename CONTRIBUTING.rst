============
Contributing
============

If you feel there is something missing from Vizzard, PRs are always welcome!
Just follow our contributing guidelines below, and don't be afraid make contact
with one of the team.

If you don't feel comfortable opening a pull request, then feel free to open an
`issue <https://github.com/trallard/ChooseViz/issues>`_!

To start your own work, fork the Vizzard repository:

``git clone https://github.com/trallard/ChooseViz.git``


Code organization
-----------------

Vizzard is a `Flask <http://flask.pocoo.org/>`_ app hosted on
`heroku <https://www.heroku.com/>`_ with a Python backend dependent on
`matplotlib <https://matplotlib.org/>`_, `pandas <https://pandas.pydata.org/>`_
and `scipy <https://www.scipy.org/>`_. Note that any changes to the master
branch on the Github repository will automatically trigger a build on heroku.

Best practice
-------------

_Extensibility_ to other scripting languages is ensured by the folder structure
chosen for the git repository:

* ``plots/histogram/``
  - ``meta.txt``
  - ``description.md``
  - ``py/``
     + ``plot.py``
     + ``test.py``
     + ``plot.png``

* ``plots/piechart/``
  - ``meta.txt``
  - ``description.md``
  - ``py/``
    + ``plot.py``
    + ``test.py``
    + ``plot.png``

* ...

Here:

- ``meta.txt`` contains a series of keywords separated by a space. These keywords
  describe the datatypes for which the plot is relevant.
- ``description.md`` is a short description of the plot to be rendered in the
  web-app.
- The remaining subdirectory contains a Python script for generating the plot in
  question, a test for that script, and an image of that plot to be rendered in
  the web-app.

It is evident that each of these subfolders could be expanded to contain an `R`
folder:

* ``plots/histogram/``
  - ``meta.txt``
  - ``description.md``
  - ``py/``
    + ``plot.py``
    + ``test.py``
    + ``plot.png``
  - ``R/``
    + ``plot.R``
    + ``test.R``
    + ``plot.png``

* ...

Basic _testing_ functionality is available: testing scripts ensure every backend
python script produces a png file.

Vizzard's source code can be found
on `GitHub <https://github.com/trallard/ChooseViz>`_. Feel free to extend
Vizzard by adding an additional graph type or scripting language as described
above. Ensure you use keywords that Vizzard recognises. A list of keywords
currently implemented is given below:

* ``categorical``
* ``continuous``
