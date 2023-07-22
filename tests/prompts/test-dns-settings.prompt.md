I am having trouble with my website configuration. Please give me step by step instructions to resolve the issue.

The website actual behavior is demonstrated in `<actual-behavior>`.

The website desired behavior is demonstrated in `<desired-behavior>`.

My namecheap DNS settings are described in `<dns>`.

```
<actual-behavior>
toby@toby-desktop-kubuntu:~$ wget www.indieagi.org
--2023-07-21 19:55:39--  http://www.indieagi.org/
Resolving www.indieagi.org (www.indieagi.org)... 104.196.232.237
Connecting to www.indieagi.org (www.indieagi.org)|104.196.232.237|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.indieagi.org/ [following]
--2023-07-21 19:55:39--  https://www.indieagi.org/
Connecting to www.indieagi.org (www.indieagi.org)|104.196.232.237|:443... connected.
ERROR: no certificate subject alternative name matches
        requested host name ‘www.indieagi.org’.
To connect to www.indieagi.org insecurely, use `--no-check-certificate'.
</actual-behavior>

<desired-behavior>
oby@toby-desktop-kubuntu:~$ wget www.indieagi.org
--2023-07-21 19:55:26--  http://www.indieagi.org/
Resolving www.indieagi.org (www.indieagi.org)... 104.196.232.237
Connecting to www.indieagi.org (www.indieagi.org)|104.196.232.237|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.indieagi.org/ [following]
--2023-07-21 19:55:26--  https://www.indieagi.org/
Connecting to www.indieagi.org (www.indieagi.org)|104.196.232.237|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 328 [text/html]
Saving to: ‘index.html’

index.html                             100%[============================================================================>]     328  --.-KB/s    in 0s      

2023-07-21 19:55:26 (95.1 MB/s) - ‘index.html’ saved [328/328]
</desired-behavior>

<dns>
Type            Host                  Value
CNAME           fm1._domainkey        fm1.indieagi.org.dkim.fmhosted.com.  
CNAME           fm2._domainkey        fm2.indieagi.org.dkim.fmhosted.com.  
CNAME           fm3._domainkey        fm3.indieagi.org.dkim.fmhosted.com.  
TXT             @                     v=spf1 include:spf.messagingengine.com ?all  
CNAME           www                   g3mdfobq.up.railway.app.  
A Record        @                     104.196.232.237
</dns>
```
