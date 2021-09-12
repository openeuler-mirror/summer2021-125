#
# Copyright (c) 2020 DLUT
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import attr
from plugincode.pre_scan import pre_scan_impl, PreScanPlugin

from filtercode.filter_code import filter_foder
from commoncode.cliutils import PluggableCommandLineOption, PRE_SCAN_GROUP



@pre_scan_impl
class FilterCode(PreScanPlugin):
    """
    Add the "license_risks" attribute to the codebase if it contains a
    detected license key while available in license_key.yml file
    """

    sort_order = 300

    options = [
        PluggableCommandLineOption(('-f', '--filter-code'),
                                   is_flag=True, default=False,
                                   help='Filter rich media files in a folder',
                                   help_group=PRE_SCAN_GROUP)
    ]
    # codebase_attributes = dict([
    #     ('rich-media-files', attr.ib(default=attr.Factory(list))),
    # ])
    codebase_attributes = dict(rich_media_files=attr.ib(default=attr.Factory(dict)))

    def is_enabled(self, filter_code, **kwargs):
        return filter_code

    def process_codebase(self, codebase, filter_code, **kwargs):

        filter_foder(codebase)

