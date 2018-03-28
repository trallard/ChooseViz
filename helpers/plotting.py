import os
import glob

def find_plots(plottype):
    plot_list = []
    for meta in glob.iglob('./plots/**/meta.txt'):
        data1= plottype.lower()
        # print(os.path.relpath(meta))
        with open(meta, 'r') as f:
            datatype = f.read()
            if datatype == plottype.lower():
                plot_list.append(os.path.relpath(meta))
    build_dict(plot_list)
    return plot_list

def build_dict(plot_list):
    plot_dict = dict()
    for plot_ in plot_list:
        container = os.path.split(plot_)[0]
        print(container)
        plot_img = os.path.join(container, 'py/plot.png')
        plot_code = os.path.join(container, 'py/plot.py')
        plot_dict.update(dict(path=plot_img))

    print(plot_dict)

