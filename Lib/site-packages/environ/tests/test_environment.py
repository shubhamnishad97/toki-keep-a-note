from unittest import TestCase
from environ import Environment, readers, EnvironmentException
from environ.tests import get_test_data_filepath


class EnvironmentTest(TestCase):

    def test_adding_a_source_new_dict_with_its_variables_is_loaded(self):
        source = {'foo': 'bar'}
        env = Environment()
        env.add_source(source)
        self.assertIn(source, env._sources)

    def test_dunder_call_method_returns_value_from_latest_source_added(self):
        first_source = {'name': 'Python'}
        last_source = {'name': 'Monty Python'}
        env = Environment()
        env.add_source(first_source)
        env.add_source(last_source)
        self.assertEqual('Monty Python', env('name'))

    def test_adding_a_file_path_source_loads_variables_with_provided_reader(self):
        env = Environment()
        env_filepath = get_test_data_filepath('test_environment.env')
        env.add_source(env_filepath, reader=readers.DotEnvFileReader())
        self.assertIn({'NAME': 'Monty Python'}, env._sources)
        self.assertEqual('Monty Python', env('NAME'))

    def test_adding_a_file_path_source_raise_exception_if_no_compatible_reader_found(self):
        env = Environment()
        not_existing_file = get_test_data_filepath('file.with.invalid_extension')
        self.assertRaisesRegexp(
                EnvironmentException,
                "No compatible Reader found for source: '%s'" % not_existing_file,
                env.add_source,
                not_existing_file
        )

    def test_adding_a_file_path_source_raise_exception_if_file_not_exists(self):
        env = Environment()
        not_existing_file = get_test_data_filepath('not_existing_file.env')
        self.assertRaisesRegexp(
                IOError,
                "No such file or directory: '%s'" % not_existing_file,
                env.add_source,
                not_existing_file
        )

    def test_adding_a_dotenv_file_path_source_uses_DotEnvFileReader(self):
        env = Environment()
        env_filepath = get_test_data_filepath('test_environment.env')
        reader_instance = env.find_reader_for_source(env_filepath)
        self.assertIsInstance(reader_instance, readers.DotEnvFileReader)
