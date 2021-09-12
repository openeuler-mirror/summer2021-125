import os
import shutil
from functools import partial

from commoncode.fileset import is_included

TRACE = False


def logger_debug(*args):
    pass


if TRACE:
    import logging
    import sys

    logger = logging.getLogger(__name__)
    # logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logging.basicConfig(stream=sys.stdout)
    logger.setLevel(logging.DEBUG)


    def logger_debug(*args):
        return logger.debug(' '.join(isinstance(a, str) and a or repr(a) for a in args))


def filter_picture(path, filter_files):
    for file in path:
        if os.path.isfile(file) and (
                file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.png')
                or file.endswith('.bmp') or file.endswith('.PNG')):
            filter_files.append(file)


def filter_music_radio(path, filter_files):
    for file in path:
        if os.path.isfile(file) and (
                file.endswith('.cda') or file.endswith('.MID') or file.endswith('.WAV') or file.endswith('.mp3')
                or file.endswith('.mp4') or file.endswith('.VQF') or file.endswith('.avi') or file.endswith('.MPEG')
                or file.endswith('.RA') or file.endswith('.RMVB') or file.endswith('.MOV') or file.endswith('.ASF')):
            filter_files.append(file)


def filter_bin(path, filter_files):
    for file in path:
        if os.path.isfile(file) and (
                file.endswith('.bin') or file.endswith('.BIN')):
            filter_files.append(file)


def filter_file(files, codebase):
    rids_to_remove = set()
    rids_to_remove_discard = rids_to_remove.discard
    rids_to_remove_add = rids_to_remove.add

    excludes = {pattern: 'Filter rich media files in <input>' for pattern in files}
    includes = {}
    included = partial(is_included, includes=includes, excludes=excludes)

    for resource in codebase.walk(topdown=True):
        if resource.is_root:
            continue
        resource_rid = resource.rid

        if not included(resource.path):
            for child in resource.children(codebase):
                rids_to_remove_add(child.rid)
            rids_to_remove_add(resource_rid)
        else:
            # we may have been selected for removal based on a parent dir
            # but may be explicitly included. Honor that
            rids_to_remove_discard(resource_rid)
    if TRACE:
        logger_debug('process_codebase: rids_to_remove')
        logger_debug(rids_to_remove)
        for rid in sorted(rids_to_remove):
            logger_debug(codebase.get_resource(rid))

    remove_resource = codebase.remove_resource

    # Then, walk bottom-up and remove the non-included Resources from the
    # Codebase if the Resource's rid is in our list of rid's to remove.
    for resource in codebase.walk(topdown=False):
        resource_rid = resource.rid
        if resource.is_root:
            continue
        if resource.is_dir:  # removing dirs will also remove its files
            continue
        if resource_rid in rids_to_remove:
            rids_to_remove_discard(resource_rid)
            remove_resource(resource)


def filter_foder(codebase):
    files = list()
    filter_files = list()
    for resource in codebase.walk(topdown=False):
        files.append(resource.path)
    filter_picture(files, filter_files)
    filter_music_radio(files, filter_files)
    filter_bin(files, filter_files)
    filter_file(filter_files, codebase)
    codebase.attributes.rich_media_files = filter_files
