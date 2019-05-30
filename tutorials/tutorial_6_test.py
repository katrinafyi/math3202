import unittest 

import tutorial_6

points = [(0,0), (-1, 0), (-2, 0), (-2, 1)]
points_rotated = [(0, 0), (0, 1), (0, 2), (1, 2)]

class TestTutorial6(unittest.TestCase):
    def test_rotate_cw(self):
        x = list(tutorial_6.rotate_cw(points))
        self.assertEqual(x, points_rotated)

    def test_rotate_4(self):
        x = list(points)
        for i in range(4):
            x = list(tutorial_6.rotate_cw(x))
        self.assertEqual(x, points)

    def test_rotations(self):
        x = tutorial_6.rotations({(-2, 1): })

if __name__ == "__main__":
    unittest.main()