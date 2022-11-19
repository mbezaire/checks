# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import requests
import getpass

site = "gradescope"
BASE_URL = f'https://www.{site}.com'
files = ["calculator.c"]
crs = '409862'
asgn = '2274993'

class APIClient:
      
    def __init__(self):
        self.session = requests.Session()
    
    def post(self, *args, **kwargs):
        return self.session.post(*args, **kwargs)
    
    def log_in(self, email, password):
        url = "{base}/api/v1/user_session".format(base=BASE_URL)
    
        form_data = {"email": email, "password": password}
        r = self.post(url, data=form_data)
    
        self.token = r.json()['token']
    
    def upload_programming_submission(self, course_id, assignment_id, student_email, filenames):
        url = "{base}/api/v1/courses/{0}/assignments/{1}/submissions".format(course_id, assignment_id, base=BASE_URL)
    
        form_data = {"owner_email": student_email}
        files = [('files[]', (filename, open(filename, 'rb'))) for filename in filenames]
    
        request_headers = {'access-token': self.token}
        r = self.post(url, data=form_data, headers=request_headers, files=files)
        return r


@check50.check()
def exists():
    """Program was submitted via check50"""
    check50.exists(*files)

@check50.check(exists)
def submit_gs():
    """Program made it into Gradescope"""
    if __name__ == '__main__':
      try:
        if 'client' not in locals() and 'client' not in globals():
          client = APIClient()
          stuhandle = input("Please provide the em" + "ail for your " +
                            site.capitalize() + " account: ")
          password = getpass.getpass('Password: ')
          client.log_in(stuhandle, password)
          status = client.upload_programming_submission(crs, asgn, stuhandle, files)
          if status.ok:
            check50.log(
              "Your work was submitted to Gradescope, head on over to check it out!"
            )
          else:
              check50.log("You can download your files and submit to {base}/courses/{0}/assignments/{1}".format(crs, asgn, base=BASE_URL))
              raise check50.Failure("Failed to submit", help=status.reason)
      except:
          check50.log("You can download your files and submit to {base}/courses/{0}/assignments/{1}".format(crs, asgn, base=BASE_URL))
          raise check50.Failure("Submission canceled")
