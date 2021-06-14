#!/usr/bin/python3

import unittest

from src.rules import vbsConverter


class TestSum(unittest.TestCase):
    def test_needsParenthesis(self):
        needsParenthesis = [
            ".press",
            ".maximize",
            ".doubleClickCurrentCell",
            ".select",
            ".setFocus",
        ]
        for item in needsParenthesis:
            expect = f"check{item}()"
            self.assertEqual(
                vbsConverter(f"check{item}"), expect, f"Should be {expect}"
            )

    def test_vbsConvert(self):
        testString = 'session.findById("wnd[0]").sendVKey 0'
        expect = 'session.findById("wnd[0]").sendVKey (0)'
        self.assertEqual(vbsConverter(testString), expect, f"Should be {expect}")


if __name__ == "__main__":
    unittest.main()
