from unittest import TestCase

from environ import Environment
from environ.tests import get_test_data_filepath


class EnvironmentTest(TestCase):

    def test_basic_usage(self):

        # Dan, a python developer, wants to load some environment variables to configure his application
        # to work in different modes.
        env = Environment()
        current_mode = env('MODE', default='DEBUG')

        # the `MODE` variable is not present into `env` Environment
        # then `current_mode` assumes the provided default value:
        self.assertEqual('DEBUG', current_mode)

        # Reading the documentation he learns that he can change the `MODE` value
        # using `os.environ` as variables provider.
        # Then he reload his application pre-pending the new value for `MODE` variable using this shell syntax:
        # `MODE=PRODUCTION python app.py`
        os_environ = {'MODE': 'PRODUCTION'} ## simulate the os.environ
        # And add a source into the current `env`
        env.add_source(os_environ)
        current_mode = env('MODE', default='DEBUG')
        self.assertEqual('PRODUCTION', current_mode)

        # Dan thinks that is not comfortable start its application using this shell-like syntax,
        # and reading the documentation he founds a smart way to do that using a simple .env file.
        # `echo TEST=on > .env`
        # Then he adds the source to current `env`
        env.add_source(get_test_data_filepath('functional_tests.env'))
        is_testing = env('TEST', default='off')
        self.assertEqual(is_testing, 'on', "TEST variable is not loaded from functional_tests.env")

        # Dan now wants to use the casting feature to avoid having to do manually.
        # He founds three method to do that:
        # 1: providing a caster function
        is_testing = env('TEST', cast=bool)
        self.assertIs(True, is_testing)
        # 2: calling the implicit method
        is_testing = env.bool('TEST')
        self.assertTrue(True, is_testing)
        # 3: using the smart-cast based on default value
        is_testing = env('TEST', default=bool)
        self.assertTrue(True, is_testing)

        self.fail("Finish the tests!")