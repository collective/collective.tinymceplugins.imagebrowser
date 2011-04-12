from setuptools import setup, find_packages
import os

version = '0.1-dev'

setup(name='collective.tinymceplugins.imagebrowser',
      version=version,
      description="A TinyMCE plugin to provide thumbnail image browsing",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Programming Language :: JavaScript",
        ],
      keywords='tinymce plugin thumbnail image browsing',
      author='Joscha Krutzki',
      author_email='joka@jokasis.de',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.tinymceplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.monkeypatcher',
          'Products.TinyMCE >= 1.1.8',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
