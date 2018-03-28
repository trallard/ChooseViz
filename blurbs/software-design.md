# Software design

## Code organization

Vizzard is a [Flask](http://flask.pocoo.org/) app hosted on [heroku](https://www.heroku.com/) with a python backend dependent on [matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/) and [scipy](https://www.scipy.org/).

## Best practice

_Extensibility_ to other scripting languages is ensured by the folder structure chosen for the git repository:

* `plots/histogram/`
  * `meta.txt`
  * `description.md`
  * `py/`
     * `plot.py`
     * `test.py`
     * `plot.png`

* `plots/piechart/`
  * `meta.txt`
  * `description.md`
  * `py/`
    * `plot.py`
    * `test.py`
    * `plot.png`

* ...

It is evident that each of these subfolders could be expanded to contain an `R` folder:

* `plots/histogram/`
  * `meta.txt`
  * `description.md`
  * `py/`
    * `plot.py`
    * `test.py`
    * `plot.png`
  * `R/`
    * `plot.R`
    * `test.R`
    * `plot.png`

* ...

Basic _testing_ functionality is available: testing scripts ensure every backend python script produces a png file. 

## Contributing code

Vizzard's source code can be found [on Github](https://github.com/trallard/ChooseViz). Feel free to extend Vizzard by adding an additional graph type or scripting language as described above. Ensure you use keywords that Vizzard recognises. A list of such keywords can be found below:

* `categorical`
* `continuous`


