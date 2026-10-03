# Tiered Investigation Hints
* **Hint 1**: Legitimate TXT queries typically query SPF (`v=spf1...`) or DKIM records. Subdomains containing Base64 padding (`==`) are highly indicative of tunneling.
* **Hint 2**: To decode standard base64 in Python: `import base64; base64.b64decode("c2VjcmV0...").decode()`.
