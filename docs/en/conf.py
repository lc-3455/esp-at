# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses ../conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from conf_common import *  # noqa: F401, F403 - need to make available everything from common
from local_util import download_file_if_missing  # noqa: E402 - need to import from common folder

# General information about the project.
project = u'ESP-AT User Guide'
copyright = u'2021, Espressif Systems (Shanghai) Co., Ltd.'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# Download font file that is stored on a separate server to save on esp-idf repository size.
print("Downloading font file")
download_file_if_missing('https://dl.espressif.com/dl/esp-idf/docs/_static/DejaVuSans.ttf', '../_static')

# Set up font for blockdiag, nwdiag, rackdiag and packetdiag
blockdiag_fontpath = '../_static/DejaVuSans.ttf'
seqdiag_fontpath = '../_static/DejaVuSans.ttf'
actdiag_fontpath = '../_static/DejaVuSans.ttf'
nwdiag_fontpath = '../_static/DejaVuSans.ttf'
rackdiag_fontpath = '../_static/DejaVuSans.ttf'
packetdiag_fontpath = '../_static/DejaVuSans.ttf'
