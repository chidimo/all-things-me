# How to

## Javascript kernel for jupyter noteook

<https://github.com/n-riesco/ijavascript>

<https://packaging.python.org/guides/distributing-packages-using-setuptools/#scripts>

## Packaging and deploying python applications

Note that *package* and *project* are used interchangeably here.

1. Start with storborg's [Python packaging tutorial](https://python-packaging.readthedocs.io/en/latest/minimal.html). But note the following exception. Don't use the `$ python setup.py sdist upload` or any of the `upload` command. The [twine](https://pypi.python.org/pypi/twine) homepage gives reasons why.
1. Create a git *tag* after you have laid out the project structure. In your package landing page on [PyPi](https://pypi.python.org/pypi), a download url will be specified. You can set this url to link to a specific location hosted on [github](https://github.com/) that is separate from your master development version. Thanks to [Peter Downs](http://peterdowns.com/posts/first-time-with-pypi.html) for this section.
1. See all tags with

    `$ git tag`

1. Add and push a tag

    `$ git tag <number or name>`

    `$ git push --tags origin <whichever branch you want to add the tag to>`

1. Tag urls follow the pattern `https://github.com/{username}/{module_name}/archive/{tag}.tar.gz.`
1. To  Remove a tag

    `$ git tag -d <number or name> # -d for delete`

    `$ git push origin :refs/tags/<number or name>`

1. **License**: To include a license, just add a `LICENSE.txt` file in your project root folder. Don't know what to put inside your license file or don't know what license to use? Check out [Choose A License](https://choosealicense.com/). If your aim is opensource, then you may like to take a look at [David A. Wheeler's](https://www.dwheeler.com/essays/gpl-compatible.html) essay on license GPL-compatibility.

1. **Classifiers**: To see what classifiers are acceptable look [here](https://pypi.python.org/pypi?%3Aaction=list_classifiers)
1. **Creating the pip installation package**

    `$ python setup.py sdist # create a source distribution`

    Note that you may have to use this commands a lot because the upload process may fail a number of times and each time it does you have to rush to make corrections, recreate the source distribution and then try to upload again.

1. **Putting your package up there**: For this step you'll need [twine](https://pypi.python.org/pypi/twine)

    `pip install twine`

1. Testing locally

    `$ python setup.py develop`

    `$ pip install .`

    `$ pip install -e .`

1. Prepare locally

    `$ python setup.py develop`

    `$ python setup.py sdist`

    `$ python setup.py sdist bdist_wheel`

1. Uploading

    `$ # these two files are inside the dist folder`

    `$ twine upload dist/* # upload everything in folder`

    `$ twine upload dist/project_name-x.y.z.tar.gz`

    `$ twine upload dist/mypkg-0.1-py2.py3-none-any.whl`

1. Having completed the above steps you're now in a better position to [dive in](http://www.diveintopython3.net/packaging.html)

## Jupyter notebook kernels

1. See all kernels `jupyter kernelspec list` or inside a jupyter notebook cell use `!jupyter kernelspec list`
