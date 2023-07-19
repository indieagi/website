I am getting the following actual_output. I want to get expected_output. What do I need to change?

<run_tests.sh>
#!/bin/bash

python -m unittest discover
</run_tests.sh>

<smoke_test.py>
import socket
import unittest

class TestSmoke(unittest.TestCase):

  def test_hostname_to_ip_resolution(self):
    self.hostnames = [
        www.indieagi.org',
        wtf.indieagi.org',
        indieagi.org'
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

</smoke_test.py>

<expected_output>
# ran x tests successfully
</expected_output>

<actual_output>
(dev_venv) toby@dt:~/src/main-website/tests$ ./run_tests.sh 

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
</actual_output>