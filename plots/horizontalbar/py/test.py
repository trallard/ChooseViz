import os
import shutil

os.makedirs('../tmp')
shutil.copyfile('plot.py', '../tmp/plot.py')
os.system('cd ../tmp; python plot.py; cd ..')
assert 'plot.png' in [x for x in os.walk('../tmp')][0][-1]
shutil.rmtree('../tmp')
