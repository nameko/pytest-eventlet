# -*- coding: utf-8 -*-
pytest_plugins = "pytester"


def test_patched(testdir):

    testdir.makepyfile(
        """
        import eventlet

        def test_patched():
            assert eventlet.patcher.is_monkey_patched("socket")
            assert eventlet.patcher.is_monkey_patched("os")
            assert eventlet.patcher.is_monkey_patched("select")
            assert eventlet.patcher.is_monkey_patched("thread")
            assert eventlet.patcher.is_monkey_patched("time")
        """
    )
    result = testdir.runpytest()
    assert result.ret == 0
