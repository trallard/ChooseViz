# ChooseViz

ChooseViz is the source repository for the web app Vizzard. Vizzard was initiated as part of the [Software Sustainability Institute Collaboration Workshop 2018](https://www.software.ac.uk/cw18/)'s Hackday.

# What is Vizzard?
Vizzard is an interactive tool designed to help researchers plot their data in a clear, appropriate and reproducible way. Depending on a data description provided by the user, Vizzard provides justified suggestions for which plot suits their data well. Furthermore, it provides researchers with a downloadable python script representing their plot.

# Why is Vizzard useful?

Reproducibility is a key aspect of good Science. Established plotting tools such as Excel or SPSS rely on not necessarily repeatable user input (lots of clicks!). Using scripting languages such as [R](https://www.rdocumentation.org/) or [Matplotlib](https://matplotlib.org/users/index.html) requires a higher level of coding skills and plenty of time to read a convoluted documentation, but providing such scripts can enhance reproducibility. Vizzard aims to provide a well-explained pathway to navigate from naive, widely-used plotting tools towards more reproducible plotting tools.

# How is Vizzard different from its alternatives?

Visualization is a key part of science communication, and needs to be done in an effective, appropriate and reproducible way (1,2). Many data visualization tools exist, but Vizzard is unique in that it tries to educate and push towards reproducibility at the same time. This text explores some of the differences between existing visualization tools and Vizzard.

## Visual Vocab

[Visual Vocabulary](http://ft-interactive.github.io/visual-vocabulary/) is a resource describing many visualization methods categorized by the sort of data relationship they emphasize. The main differences to Vizzard are:
1. Vizzard tailors the proposed visualization methods to the individual user's data
2. Vizzard provides a code template to encourage reproducible data visualization
3. Vizzard is designed to be educational

## Python and R Graph Galleries

The [Python Graph Gallery](https://python-graph-gallery.com/) and the [R Graph Gallery](https://www.r-graph-gallery.com/) exemplify possible ways of visualizing data using a scripting language, but do not relate to the user's data.

## D3.js
[D3.js](https://d3js.org/) is a Javascript library to visualize data, but does not offer the possibility to narrow down the choice of plot to suit the data at hand.

## General advice
[OxShef:dataviz](https://oxshef.github.io/oxshef/training-resources.html) (and presumably others) provides general advice on how to visualize data, but are not interactive.

### References

1. Cleveland, W. and McGill, R. (1984). Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods. _Journal of the American Statistical Association_, 79(387), p.531.
2. Cleveland, W. and McGill, R. (1985). Graphical Perception and Graphical Methods for Analyzing Scientific Data. _Science_, 229(4716), pp.828-833.


# Software design

## Code organization

Vizzard is a [Flask](http://flask.pocoo.org/) app hosted on [heroku](https://www.heroku.com/) with a python backend dependent on [matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/) and [scipy](https://www.scipy.org/). Any changes to the master branch on the Github repository will automatically trigger a build on heroku.

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


# Future potential

Add-ons to Vizzard may include the possibility to upload your own data (currently an example data set is used) or expand the number of scripting languages available (currently just matplotlib). More details can be found in this repository's issues


