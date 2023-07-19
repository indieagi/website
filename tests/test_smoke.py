import socket
import unittest
import requests

class TestSmoke(unittest.TestCase):

  def test_hostname_to_ip_resolution(self):
    self.hostnames = [
        'www.indieagi.org',
        'wtf.indieagi.org',
        'indieagi.org'
    ]

    for hostname in self.hostnames:   
      with self.subTest(hostname=hostname):
        try:
          ip = socket.gethostbyname(hostname)
          response = requests.get(f'http://{hostname}')
          self.assertEqual(
            response.status_code, 
            200, 
            f"Received non-200 status code: {response.status_code} for {hostname}"
            )
        
        except socket.gaierror:
          self.fail(f"DNS resolution failed for {hostname}")

        except requests.exceptions.RequestException as e:
          self.fail(f"DNS resolution succeeded but failed to get 200 OK for {hostname}. Error: {str(e)}")

if __name__ == '__main__':
  unittest.main()
