# VOD dev-kit.
# Code written by Oscar Beijbom, 2019.

import os
import unittest

from vod import VOD


class TestVOD(unittest.TestCase):

    def test_load(self):
        """
        Loads up VOD.
        This is intended to simply run the VOD class to check for import errors, typos, etc.
        """

        assert 'NUSCENES' in os.environ, 'Set NUSCENES env. variable to enable tests.'
        nusc = VOD(version='v1.0-mini', dataroot=os.environ['NUSCENES'], verbose=False)

        # Trivial assert statement
        self.assertEqual(nusc.table_root, os.path.join(os.environ['NUSCENES'], 'v1.0-mini'))


if __name__ == '__main__':
    unittest.main()
