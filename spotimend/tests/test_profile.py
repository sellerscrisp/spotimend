import os
import tempfile

from unittest import TestCase

from spotimend.profile import profile


class TestCase(TestCase):
    """Test profile page"""

    def setUp(self):
        """Create test client"""
