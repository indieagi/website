I am getting the following error when running this python file. How can I make the subtest fail instead of crash if there is an NXDOMAIN issue?

<file>
import socket
import unittest

class TestDNS(unittest.TestCase):

  def setUp(self):
    self.user_facing_site_ip = '104.196.232.237'

    self.test_cases = [
        {'hostname': 'www.indieagi.org', 'expected_ip': self.user_facing_site_ip},
        {'hostname': 'wtf.indieagi.org', 'expected_ip': self.user_facing_site_ip},
        {'hostname': 'indieagi.org',     'expected_ip': self.user_facing_site_ip}
    ]

  def test_hostname_to_ip_resolution(self):
    for test_case in self.test_cases:
      current_hostname  = test_case['hostname']
      expected_ip_address = test_case['expected_ip']
      
      with self.subTest(test_case=test_case):
        try:
          ip_addresses = socket.gethostbyname_ex(current_hostname)[2]
        except socket.gaierror:
          self.fail(f"Hostname resolution failed for {current_hostname}")
           
        self.assertIn(
          expected_ip_address, 
          ip_addresses, 
          f"Expected IP ({expected_ip_address}) not found for hostname {current_hostname}"
        )

if __name__ == '__main__':
  unittest.main()

</file>

<error>
(dev_venv) toby@dt:~/src/main-website/tests$ ./run_tests.sh 
E
======================================================================
ERROR: test_hostname_to_ip_resolution (test_dns.TestDNS.test_hostname_to_ip_resolution)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/toby/src/main-website/tests/test_dns.py", line 20, in test_hostname_to_ip_resolution
    ip_addresses = socket.gethostbyname_ex(current_hostname)[2]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -2] Name or service not known

----------------------------------------------------------------------
Ran 1 test in 0.005s

FAILED (errors=1)
</error>