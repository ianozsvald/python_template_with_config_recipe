import unittest

# inspired by https://github.com/ioos/conda-recipes/blob/master/recipes/quantities/run_test.py
# see also http://conda.pydata.org/docs/building/meta-yaml.html#test-section

suite = unittest.TestLoader().discover('python_template_with_config')
unittest.TextTestRunner(verbosity=1).run(suite)
