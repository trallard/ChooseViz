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
    plot_dict = {}
    for plot_ in plot_list:
        container = os.path.split(plot_)[0]
        name = container.split('/')[-1]
        print(container)
        plot_img = os.path.join(container, 'py/plot.png')
        plot_code = os.path.join(container, 'py/plot.py')
        plot_description = os.path.join(container, 'description.md')
        plot_dict[name] = {
            'dir': container,
            'img': plot_img,
            'code': plot_code,
            'description': plot_description
        }

    print(plot_dict)