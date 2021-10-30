from tabula.io import convert_into_by_batch
import os

mainpath=os.path.abspath(os.getcwd())
path=mainpath+"/PDF/"
convert_into_by_batch(path, output_format='csv', pages='all')