import subprocess
import unittest


class TestMain(unittest.TestCase):

  def test_output(self):
    result = subprocess.check_output(
        ["python3", "main.py"], text=True
    ).strip()
    self.assertEqual(result, "hello MIAE")


if __name__ == "__main__":
  unittest.main()
