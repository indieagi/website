import socket
import unittest

class TestDNS(unittest.TestCase):

  def setUp(self):
    self.user_facing_site_ip = '8.8.8.8'
    self.operator_facing_site_ip = '8.8.8.8'

    self.test_cases = [
        {'hostname': 'www.indieagi.org', 'expected_ip': self.user_facing_site_ip},
        {'hostname': 'wtf.indieagi.org', 'expected_ip': self.operator_facing_site_ip},
        {'hostname': 'indieagi.org',     'expected_ip': self.user_facing_site_ip}
    ]

  def test_hostname_to_ip_resolution(self):
    for test_case in self.test_cases:
        current_hostname  = test_case['hostname']
        expected_ip_address = test_case['expected_ip']

        ip_addresses = socket.gethostbyname_ex(current_hostname)[2]

        with self.subTest(test_case=test_case):   
          self.assertIn(
            expected_ip_address, 
            ip_addresses, 
            f"Expected IP ({expected_ip_address}) not found for hostname {current_hostname}"
          )

if __name__ == '__main__':
  unittest.main()
