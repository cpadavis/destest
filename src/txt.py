import numpy as np

import catalog

class write_methods(object):

  @staticmethod
  def write_append(line,cat,label='',create=False,newline=True):
    """
    Text output routine used in many functions to standardise output.
    """

    if newline:
      n='\n'
      print line
    else:
      n=''
      print line,

    if create:
      with open('text/'+label+'_'+cat.name+'.txt','w') as f:
        f.write(line+n)
    else:
      with open('text/'+label+'_'+cat.name+'.txt','a') as f:
        f.write(line+n)

    return


  @staticmethod
  def heading(line,cat,label='',create=False):
    """
    Header formatting.
    """

    write_methods.write_append('',cat,label=label,create=create)
    write_methods.write_append('------------------',cat,label=label,create=create)
    write_methods.write_append('   '+line+'   ',cat,label=label,create=False)
    write_methods.write_append('------------------',cat,label=label,create=False)
    write_methods.write_append('',cat,label=label,create=create)

    return

  @staticmethod
  def get_file(cat,label=''):
    """
    Default filename.
    """

    return 'text/'+label+'_'+cat.name+'.txt'