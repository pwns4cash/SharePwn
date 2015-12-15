# SharePwn
A tool for auditing SharePoint security settings and identifying common security holes.

### Use: ###
Install Dependencies:
<code>pip install -r requirements.txt</code><br />
Run:
<code>python sharepwn.py</code>

###Features:###
* Service Discovery
* Version Identification
* User Enumeration
* System/Machine Account Discovery

### Known Issues: ###
* Changing Target/Port while in sharepwn.py does not succesfully change the target specification.
For now, sharepwn.py must be restarted to change target.
* People Enumeration is not fully functional, as I need to stand up a testing environment in order to finish
some of the details.

### Short Term Development TO-DO items: ###
* Better error handling
* Input Sanitization
* Code Clean-up
* Finish People Enumeration Functionality

### Contributing: ###
Although I've written and released the initial development version of this tool myself, I am eager
for any help in further development that I can get.  I'm not a professional developer and could use the help!
Create a Pull Request if you'd like to contribue something, or e-mail me at 0rigen[ at ]0rigen [d0t] net to discuss any work.