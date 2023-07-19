What CNAME records should I change or modify to my Namecheap DNS configuration to achieve my desired configuration?

Current settings:
Type            Host                  Value
CNAME           fm1._domainkey        fm1.indieagi.org.dkim.fmhosted.com.
CNAME           fm2._domainkey        fm2.indieagi.org.dkim.fmhosted.com.
CNAME           fm3._domainkey        fm3.indieagi.org.dkim.fmhosted.com.
TXT             @                     v=spf1 include:spf.messagingengine.com ?all
CNAME           www                   g3mdfobq.up.railway.app.
A Record        @                     104.196.232.237

Desired configuration:
- indieagi.org     resolves to g3mdfobq.up.railway.app.
- www.indieagi.org resolves to g3mdfobq.up.railway.app.
- *.indieagi.org resolves to g3mdfobq.up.railway.app.