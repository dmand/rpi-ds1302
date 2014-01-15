#!/usr/bin/env python
from distutils.core import setup, Extension

c_nviro = Extension('ds1302',
					sources = ['python.c'],
					libraries = ['wiringPi', 'm'],
					extra_compile_args = ['-std=c99'],
				)

setup(name='rpi_rtc',
	  version="0.1",
	  description='Python library for handling DS1302 RTC with Raspberry Pi',
	  ext_modules=[c_nviro],
	  py_modules=['rpi_time', 'hwclock'],
	  )
