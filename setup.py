try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand

class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests', '--with-coverage'])

config = {
    'description': 'Collecting and analyzing social data.',
    'author': 'NewsAI',
    'url': 'https://github.com/news-ai/SoNet',
    'download_url': 'https://github.com/news-ai/SoNet',
    'author_email': 'abhi@newsai.org',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['sonet'],
    'tests_require': ['nose'],
    'cmdclass': {'test': NoseTestCommand},
    'scripts': [],
    'name': 'SoNet'
}

setup(**config)