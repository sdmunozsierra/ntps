"""Whitebox test file for hook.py"""
from ntps.Hook import hook


def test_run_hook():
    """Test hook class."""
    test_hook = hook.TestHook("dummy", "description", True)
