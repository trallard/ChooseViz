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
    plot_dic = build_dict(plot_list)
    return plot_dic

def build_dict(plot_list):
    plot_dict = []
    for plot_ in plot_list:
        container = os.path.split(plot_)[0]
        name = container.split('/')[-1]
        print(container)
        plot_img = os.path.join(container, 'py/plot.png')
        plot_code = os.path.join(container, 'py/plot.py')
        plot_description = os.path.join(container, 'description.md')
        with open(plot_description, 'r') as des:
            description = des.read()
        with open(plot_code, 'r') as code:
            code_full = code.read()
        plot_dict.append({
            'dir': container,
            'img': plot_img,
            'code': code_full,
            'description': description
        })

    return (plot_dict)