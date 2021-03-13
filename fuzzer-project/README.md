# Fuzzer Project
This project is automatically run through the GitLab CI.
## How to install and run manually

Clone the repository by running the command:
```console
$ https://kgcoe-git.rit.edu/jmd9065/fuzzer-project.git
```
You will need to install [MechanicalSoup](https://mechanicalsoup.readthedocs.io/en/stable/).
To install run the command:
```console
$ pip3 install mechanicalsoup
```

Next you need DVWA to run on localhost. You will need to download [Docker](https://www.docker.com/). 

Once Docker is installed, run the command to pull and run the image:
```console
$ docker run --rm -it -p 80:80 andymeneely/swen331fuzzer
```

Now that localhost is initialized, run the command for discover operations:

```console
$ python3 fuzz.py discover http://localhost --custom-auth=dvwa --common-words=words.txt --extensions=extensions.txt
```

And for test operations:

```console
$ python3 fuzz.py test http://localhost --custom-auth=dvwa --sensitive=sensitive.txt --vectors=vectors.txt --sanitized-chars=sanitized-chars.txt --slow=10
```

## DVWA Example Program Output
```
VALID LINKS GUESSED:
________________________________
http://localhost
http://localhost/phpinfo.php
http://localhost/about.php
http://localhost/index.php
________________________________
LINKS DISCOVERED ON PAGE:
________________________________
http://localhost/.
http://localhost/instructions.php
http://localhost/setup.php
http://localhost/vulnerabilities/brute/
http://localhost/vulnerabilities/exec/
http://localhost/vulnerabilities/csrf/
http://localhost/vulnerabilities/fi/.?page=include.php
http://localhost/vulnerabilities/upload/
http://localhost/vulnerabilities/captcha/
http://localhost/vulnerabilities/sqli/
http://localhost/vulnerabilities/sqli_blind/
http://localhost/vulnerabilities/weak_id/
http://localhost/vulnerabilities/xss_d/
http://localhost/vulnerabilities/xss_r/
http://localhost/vulnerabilities/xss_s/
http://localhost/vulnerabilities/csp/
http://localhost/vulnerabilities/javascript/
http://localhost/security.php
http://localhost/phpinfo.php
http://localhost/about.php
http://localhost/about.php/.
http://localhost/about.php/instructions.php
http://localhost/about.php/setup.php
http://localhost/about.php/vulnerabilities/brute/
http://localhost/about.php/vulnerabilities/exec/
http://localhost/about.php/vulnerabilities/csrf/
http://localhost/about.php/vulnerabilities/fi/.?page=include.php
http://localhost/about.php/vulnerabilities/upload/
http://localhost/about.php/vulnerabilities/captcha/
http://localhost/about.php/vulnerabilities/sqli/
http://localhost/about.php/vulnerabilities/sqli_blind/
http://localhost/about.php/vulnerabilities/weak_id/
http://localhost/about.php/vulnerabilities/xss_d/
http://localhost/about.php/vulnerabilities/xss_r/
http://localhost/about.php/vulnerabilities/xss_s/
http://localhost/about.php/vulnerabilities/csp/
http://localhost/about.php/vulnerabilities/javascript/
http://localhost/about.php/security.php
http://localhost/about.php/phpinfo.php
http://localhost/about.php/about.php
http://localhost/about.php/docs/DVWA_v1.3.pdf
http://localhost/about.php/instructions.php?doc=PHPIDS-license
http://localhost/index.php/.
http://localhost/index.php/instructions.php
http://localhost/index.php/setup.php
http://localhost/index.php/vulnerabilities/brute/
http://localhost/index.php/vulnerabilities/exec/
http://localhost/index.php/vulnerabilities/csrf/
http://localhost/index.php/vulnerabilities/fi/.?page=include.php
http://localhost/index.php/vulnerabilities/upload/
http://localhost/index.php/vulnerabilities/captcha/
http://localhost/index.php/vulnerabilities/sqli/
http://localhost/index.php/vulnerabilities/sqli_blind/
http://localhost/index.php/vulnerabilities/weak_id/
http://localhost/index.php/vulnerabilities/xss_d/
http://localhost/index.php/vulnerabilities/xss_r/
http://localhost/index.php/vulnerabilities/xss_s/
http://localhost/index.php/vulnerabilities/csp/
http://localhost/index.php/vulnerabilities/javascript/
http://localhost/index.php/security.php
http://localhost/index.php/phpinfo.php
http://localhost/index.php/about.php
________________________________
INPUTS FOUND ON PAGES:
________________________________

Database Setup - http://localhost/setup.php
	create_db
	user_token

Vulnerability: Brute Force - http://localhost/vulnerabilities/brute/
	username
	password
	Login

Vulnerability: Command Injection - http://localhost/vulnerabilities/exec/
	ip
	Submit

Vulnerability: Cross Site Request Forgery (CSRF) - http://localhost/vulnerabilities/csrf/
	password_new
	password_conf
	Change

Vulnerability: File Inclusion - http://localhost/vulnerabilities/fi/.?page=include.php
	page

Vulnerability: File Upload - http://localhost/vulnerabilities/upload/
	MAX_FILE_SIZE
	uploaded
	Upload

Vulnerability: Insecure CAPTCHA - http://localhost/vulnerabilities/captcha/
	step
	password_new
	password_conf
	Change

Vulnerability: SQL Injection - http://localhost/vulnerabilities/sqli/
	id
	Submit

Vulnerability: SQL Injection (Blind) - http://localhost/vulnerabilities/sqli_blind/
	id
	Submit

Vulnerability: Reflected Cross Site Scripting (XSS) - http://localhost/vulnerabilities/xss_r/
	name

Vulnerability: Stored Cross Site Scripting (XSS) - http://localhost/vulnerabilities/xss_s/
	txtName
	btnSign
	btnClear

Vulnerability: Content Security Policy (CSP) Bypass - http://localhost/vulnerabilities/csp/
	include

Vulnerability: JavaScript Attacks - http://localhost/vulnerabilities/javascript/
	token
	phrase
	send

DVWA Security - http://localhost/security.php
	seclev_submit
	user_token

http://localhost/about.php/vulnerabilities/fi/.?page=include.php
	page

http://localhost/about.php/instructions.php?doc=PHPIDS-license
	doc

Welcome to Damn Vulnerable Web Application! - http://localhost/index.php/vulnerabilities/fi/.?page=include.php
	page
________________________________
COOKIES:
	<Cookie PHPSESSID=8s1hldg2ev3l0uhjj9941or5d7 for localhost.local/>
	<Cookie security=low for localhost.local/>
________________________________

________________________________
TESTS
________________________________

________________________________
Database Setup - http://localhost/setup.php
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "MySQL" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential Sensitive Data Leak: The sensitive word "mysql" was found in response.

________________________________
Vulnerability: Brute Force - http://localhost/vulnerabilities/brute/
________________________________
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.

________________________________
Vulnerability: Command Injection - http://localhost/vulnerabilities/exec/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential DOS Vulnerability: This page took 16.1 ms to load with input vector: "Admin' OR '".
Potential DOS Vulnerability: This page took 15.01 ms to load with input vector: "%27+OR+%277659%27%3D%277659".
Potential DOS Vulnerability: This page took 11.95 ms to load with input vector: "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>".
Potential DOS Vulnerability: This page took 11.39 ms to load with input vector: "'; EXEC ('SEL' + 'ECT US' + 'ER')".
Potential DOS Vulnerability: This page took 10.31 ms to load with input vector: "UNI/**/ON SEL/**/ECT".
Potential DOS Vulnerability: This page took 10.55 ms to load with input vector: "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'".
Potential DOS Vulnerability: This page took 15.29 ms to load with input vector: "+or+isnull%281%2F0%29+%2F*".
Potential DOS Vulnerability: This page took 16.42 ms to load with input vector: "%27+--+&password=".
Potential DOS Vulnerability: This page took 10.46 ms to load with input vector: "'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--".
Potential DOS Vulnerability: This page took 16.2 ms to load with input vector: "%22+or+isnull%281%2F0%29+%2F*".
Potential DOS Vulnerability: This page took 12.21 ms to load with input vector: "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>".
Potential DOS Vulnerability: This page took 10.89 ms to load with input vector: "'/**/OR/**/1/**/=/**/1".
Potential DOS Vulnerability: This page took 10.87 ms to load with input vector: "Password:*/=1--".
Potential DOS Vulnerability: This page took 11.54 ms to load with input vector: "' or 1/*".
Potential DOS Vulnerability: This page took 10.29 ms to load with input vector: "OR 1=1".
Potential DOS Vulnerability: This page took 15.92 ms to load with input vector: "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>".

________________________________
Vulnerability: Cross Site Request Forgery (CSRF) - http://localhost/vulnerabilities/csrf/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential DOS Vulnerability: This page took 10.36 ms to load with input vector: "' or 1 in (select @@version)--".
Potential DOS Vulnerability: This page took 10.04 ms to load with input vector: "' union select".
Potential DOS Vulnerability: This page took 12.05 ms to load with input vector: "' SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = tablename')--".
Potential DOS Vulnerability: This page took 10.62 ms to load with input vector: ">"><script>alert("XSS")</script>&".
Potential DOS Vulnerability: This page took 10.1 ms to load with input vector: "%27+--+&password=".
Potential DOS Vulnerability: This page took 10.74 ms to load with input vector: "<IMG SRC="javascript:alert('XSS');">".
Potential DOS Vulnerability: This page took 11.54 ms to load with input vector: "'';!--"<XSS>=&{()}".
Potential DOS Vulnerability: This page took 12.03 ms to load with input vector: "' OR 1=1--".
Potential DOS Vulnerability: This page took 12.05 ms to load with input vector: "' OR 2 BETWEEN 1 and 3".
Potential DOS Vulnerability: This page took 10.01 ms to load with input vector: "<IMG SRC=javascript:alert('XSS')>".
Potential DOS Vulnerability: This page took 13.34 ms to load with input vector: "' union all select @@version--".
Potential DOS Vulnerability: This page took 13.07 ms to load with input vector: "' OR '1'='1".
Potential DOS Vulnerability: This page took 11.37 ms to load with input vector: "OR 1=1".
Potential DOS Vulnerability: This page took 10.46 ms to load with input vector: "' or 1/*".

________________________________
Vulnerability: File Upload - http://localhost/vulnerabilities/upload/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.

________________________________
Vulnerability: Insecure CAPTCHA - http://localhost/vulnerabilities/captcha/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.

________________________________
Vulnerability: SQL Injection - http://localhost/vulnerabilities/sqli/
________________________________
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.

________________________________
Vulnerability: SQL Injection (Blind) - http://localhost/vulnerabilities/sqli_blind/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential Sensitive Data Leak: The sensitive word "mysql" was found in response.
HTTP Error 404 (Not Found) with input vector "' union all select @@version--"
HTTP Error 404 (Not Found) with input vector "' union select"
HTTP Error 404 (Not Found) with input vector "' OR 1=1--"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "' or 1 in (select @@version)--"
HTTP Error 404 (Not Found) with input vector "Admin' OR '"
HTTP Error 404 (Not Found) with input vector "Password:*/=1--"
HTTP Error 404 (Not Found) with input vector "<IMG SRC=javascript:alert('XSS')>"
HTTP Error 404 (Not Found) with input vector "' or 1/*"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "%27+--+&password="
HTTP Error 404 (Not Found) with input vector "'';!--"<XSS>=&{()}"
HTTP Error 404 (Not Found) with input vector "OR 1=1"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--"
HTTP Error 404 (Not Found) with input vector "UNI/**/ON SEL/**/ECT"
HTTP Error 404 (Not Found) with input vector "' ; drop table temp --"
HTTP Error 404 (Not Found) with input vector "+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "'; EXEC ('SEL' + 'ECT US' + 'ER')"
HTTP Error 404 (Not Found) with input vector ") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;"
HTTP Error 404 (Not Found) with input vector "' OR 2 BETWEEN 1 and 3"
HTTP Error 404 (Not Found) with input vector "'/**/OR/**/1/**/=/**/1"
HTTP Error 404 (Not Found) with input vector "<IMG SRC="javascript:alert('XSS');">"
HTTP Error 404 (Not Found) with input vector "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'"
HTTP Error 404 (Not Found) with input vector "; OR '1'='1'"
HTTP Error 404 (Not Found) with input vector "%27+OR+%277659%27%3D%277659"
HTTP Error 404 (Not Found) with input vector "' group by userid having 1=1--"
HTTP Error 404 (Not Found) with input vector "' SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = tablename')--"
HTTP Error 404 (Not Found) with input vector ">"><script>alert("XSS")</script>&"
HTTP Error 404 (Not Found) with input vector "' union select * from users where login = char(114,111,111,116);"
HTTP Error 404 (Not Found) with input vector "%22+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "' or username like char(37);"

________________________________
Vulnerability: Weak Session IDs - http://localhost/vulnerabilities/weak_id/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential Sensitive Data Leak: The sensitive word "mysql" was found in response.
HTTP Error 404 (Not Found) with input vector "' union all select @@version--"
HTTP Error 404 (Not Found) with input vector "' union select"
HTTP Error 404 (Not Found) with input vector "' OR 1=1--"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "' or 1 in (select @@version)--"
HTTP Error 404 (Not Found) with input vector "Admin' OR '"
HTTP Error 404 (Not Found) with input vector "Password:*/=1--"
HTTP Error 404 (Not Found) with input vector "' OR '1'='1"
HTTP Error 404 (Not Found) with input vector "<IMG SRC=javascript:alert('XSS')>"
HTTP Error 404 (Not Found) with input vector "' or 1/*"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "%27+--+&password="
HTTP Error 404 (Not Found) with input vector "'';!--"<XSS>=&{()}"
HTTP Error 404 (Not Found) with input vector "OR 1=1"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--"
HTTP Error 404 (Not Found) with input vector "UNI/**/ON SEL/**/ECT"
HTTP Error 404 (Not Found) with input vector "' ; drop table temp --"
HTTP Error 404 (Not Found) with input vector "+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "'; EXEC ('SEL' + 'ECT US' + 'ER')"
HTTP Error 404 (Not Found) with input vector ") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;"
HTTP Error 404 (Not Found) with input vector "' OR 2 BETWEEN 1 and 3"
HTTP Error 404 (Not Found) with input vector "'/**/OR/**/1/**/=/**/1"
HTTP Error 404 (Not Found) with input vector "<IMG SRC="javascript:alert('XSS');">"
HTTP Error 404 (Not Found) with input vector "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'"
HTTP Error 404 (Not Found) with input vector "; OR '1'='1'"
HTTP Error 404 (Not Found) with input vector "%27+OR+%277659%27%3D%277659"
HTTP Error 404 (Not Found) with input vector "' group by userid having 1=1--"
HTTP Error 404 (Not Found) with input vector "' SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = tablename')--"
HTTP Error 404 (Not Found) with input vector ">"><script>alert("XSS")</script>&"
HTTP Error 404 (Not Found) with input vector "' union select * from users where login = char(114,111,111,116);"
HTTP Error 404 (Not Found) with input vector "%22+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "' or username like char(37);"

________________________________
Vulnerability: DOM Based Cross Site Scripting (XSS) - http://localhost/vulnerabilities/xss_d/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
Potential Sensitive Data Leak: The sensitive word "mysql" was found in response.
HTTP Error 404 (Not Found) with input vector "' union all select @@version--"
HTTP Error 404 (Not Found) with input vector "' union select"
HTTP Error 404 (Not Found) with input vector "' OR 1=1--"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "' or 1 in (select @@version)--"
HTTP Error 404 (Not Found) with input vector "Admin' OR '"
HTTP Error 404 (Not Found) with input vector "Password:*/=1--"
HTTP Error 404 (Not Found) with input vector "' OR '1'='1"
HTTP Error 404 (Not Found) with input vector "<IMG SRC=javascript:alert('XSS')>"
HTTP Error 404 (Not Found) with input vector "' or 1/*"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "%27+--+&password="
HTTP Error 404 (Not Found) with input vector "'';!--"<XSS>=&{()}"
HTTP Error 404 (Not Found) with input vector "OR 1=1"
HTTP Error 404 (Not Found) with input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
HTTP Error 404 (Not Found) with input vector "'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--"
HTTP Error 404 (Not Found) with input vector "UNI/**/ON SEL/**/ECT"
HTTP Error 404 (Not Found) with input vector "' ; drop table temp --"
HTTP Error 404 (Not Found) with input vector "+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "'; EXEC ('SEL' + 'ECT US' + 'ER')"
HTTP Error 404 (Not Found) with input vector ") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;"
HTTP Error 404 (Not Found) with input vector "' OR 2 BETWEEN 1 and 3"
HTTP Error 404 (Not Found) with input vector "'/**/OR/**/1/**/=/**/1"
HTTP Error 404 (Not Found) with input vector "<IMG SRC="javascript:alert('XSS');">"
HTTP Error 404 (Not Found) with input vector "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'"
HTTP Error 404 (Not Found) with input vector "; OR '1'='1'"
HTTP Error 404 (Not Found) with input vector "%27+OR+%277659%27%3D%277659"
HTTP Error 404 (Not Found) with input vector "' group by userid having 1=1--"
HTTP Error 404 (Not Found) with input vector "' SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = tablename')--"
HTTP Error 404 (Not Found) with input vector ">"><script>alert("XSS")</script>&"
HTTP Error 404 (Not Found) with input vector "' union select * from users where login = char(114,111,111,116);"
HTTP Error 404 (Not Found) with input vector "%22+or+isnull%281%2F0%29+%2F*"
HTTP Error 404 (Not Found) with input vector "' or username like char(37);"

________________________________
Vulnerability: Reflected Cross Site Scripting (XSS) - http://localhost/vulnerabilities/xss_r/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
The character ">" was not sanitized from input vector "<IMG SRC=javascript:alert('XSS')>"
The character """ was not sanitized from input vector "<IMG SRC="javascript:alert('XSS');">"
The character ";" was not sanitized from input vector "' or username like char(37);"
The character ":" was not sanitized from input vector "Password:*/=1--"
The character "*" was not sanitized from input vector ") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "' or 1/*"
The character ">" was not sanitized from input vector "'';!--"<XSS>=&{()}"
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character "|" was not sanitized from input vector "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'"
The character "/" was not sanitized from input vector ">"><script>alert("XSS")</script>&"
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "UNI/**/ON SEL/**/ECT"
The character "<" was not sanitized from input vector "'';!--"<XSS>=&{()}"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character "*" was not sanitized from input vector "+or+isnull%281%2F0%29+%2F*"
The character ";" was not sanitized from input vector "' union select * from users where login = char(114,111,111,116);"
The character ";" was not sanitized from input vector "<IMG SRC="javascript:alert('XSS');">"
The character ">" was not sanitized from input vector ">"><script>alert("XSS")</script>&"
The character ";" was not sanitized from input vector "'';!--"<XSS>=&{()}"
The character """ was not sanitized from input vector "'';!--"<XSS>=&{()}"
The character "*" was not sanitized from input vector "%22+or+isnull%281%2F0%29+%2F*"
The character "<" was not sanitized from input vector "<IMG SRC="javascript:alert('XSS');">"
The character "*" was not sanitized from input vector "'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--"
The character ";" was not sanitized from input vector "'; EXEC ('SEL' + 'ECT US' + 'ER')"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "Password:*/=1--"
The character ";" was not sanitized from input vector "'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character """ was not sanitized from input vector ">"><script>alert("XSS")</script>&"
The character "*" was not sanitized from input vector "' union select * from users where login = char(114,111,111,116);"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<IMG SRC=javascript:alert('XSS')>"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "*" was not sanitized from input vector "' or 1/*"
The character "*" was not sanitized from input vector "'/**/OR/**/1/**/=/**/1"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "; OR '1'='1'"
The character "*" was not sanitized from input vector "Password:*/=1--"
The character ":" was not sanitized from input vector "<IMG SRC="javascript:alert('XSS');">"
The character "/" was not sanitized from input vector "'/**/OR/**/1/**/=/**/1"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector "<IMG SRC=javascript:alert('XSS')>"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character ">" was not sanitized from input vector "<IMG SRC="javascript:alert('XSS');">"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "' ; drop table temp --"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector ") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;"
The character "*" was not sanitized from input vector "UNI/**/ON SEL/**/ECT"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector ">"><script>alert("XSS")</script>&"

________________________________
Vulnerability: Stored Cross Site Scripting (XSS) - http://localhost/vulnerabilities/xss_s/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"

________________________________
Vulnerability: Content Security Policy (CSP) Bypass - http://localhost/vulnerabilities/csp/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"

________________________________
Vulnerability: JavaScript Attacks - http://localhost/vulnerabilities/javascript/
________________________________
Potential Sensitive Data Leak: The sensitive word "data" was found in response.
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
The character ">" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "/" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ";" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character """ was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "<" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character "?" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"
The character ":" was not sanitized from input vector "<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>"

________________________________
DVWA Security - http://localhost/security.php
________________________________
Potential Sensitive Data Leak: The sensitive word "SQL" was found in response.
________________________________
TEST RESULTS
________________________________
Number of unsanitized inputs: 80
Number of possible sensitive data leakages: 32
Number of possible DOS vulnerabilities: 30
Number of HTTP/Response Code Errors: 98
```

