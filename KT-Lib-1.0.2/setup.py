import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
				 name="KT-Lib",
				 version="1.0.2",
				 author="KISS Institute",
				 author_email="info@KIPR.org",
				 description="This is a simple python wrapper package. It wraps the Tello EDU SDK 2.0 for use in the KIPR Aerial Botball Challenge Program.",
				 long_description=long_description,
				 long_description_content_type="text/markdown",
				 url="https://github.com/kipr",
				 packages=setuptools.find_packages(),
				 classifiers=[
							  "Programming Language :: Python :: 3",
							  "License :: OSI Approved :: MIT License",
							  "Operating System :: OS Independent",
							  ],
				 python_requires='>=3.6',
				 )
