# IPv6 Normalizer

This is a pet project I took up while I was struggling to standardize a bunch of IPv6 addresses.

I required a utility which was really portable and even shareable with others - hence this project was moved to JavaScript implementation from the original Python code

## Disclosure
The logic used in the HTML/JS page is completely based on my reading and understanding of the [RFC5952](https://tools.ietf.org/html/rfc5952#page-10).
My understanding may or may not be accurate. Use at own risk.

Corrections or enhancements to the logic is welcomed.


## Python version
This uses the `socket` module and uses the functions `inet_pton` and `inet_ntop` which has dependencies on POSIX library. Hence this Python code cannot be run on Windows machines.

This code is included so as to be run on Unix like systems which support the POSIX library.

### Usage
```
# For console based conversions
$ python ipv6_normalizer.py
>> 2001:0db8:85a3:0000:0000:8a2e:0370:7334
>> 2001:db8:85a3::8a2e:370:7334

# For file based conversions
$ python ipv6_normalizer.py < iplist.txt >normalized_ips.txt
$
