generate-smoke-test.prompt.md

Complete the following smoke test

<smoke_test.py>
import socket
import unittest

class SmokeTest(unittest.TestCase):

  def test_hostname_to_ip_resolution(self):
    self.hostnames = [
        www.indieagi.org',
        wtf.indieagi.org',
        indieagi.org'
    ]

    for hostname in self.hostnames:   
      with self.subTest(hostname=hostname):
        # test passes if the hostname returns 200 OK
        # test fails with a descriptive message if DNS resolution fails
        # test fails with a descriptive message if DNS succeeds but we don't get a 200 OK

if __name__ == '__main__':
  unittest.main()

</smoke_test.py>