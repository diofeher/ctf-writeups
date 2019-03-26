# Usage
Edit HOST inside `new_runc`, Start `nc -nvlp <port>` and run `python3 sss.py`

# Notes
- This exploit is destructive: it'll overwrite `/usr/bin/docker-runc` binary *on the host* with the
payload. It'll also overwrite `/bin/sh` inside the container.
- Tested only on Debian 9.
- No attempts were made to make it stable or reliable, it's only tested to work when a `docker exec
<id> /bin/sh` is issued on the host.

More complete explanation [here](https://github.com/lxc/lxc/commit/6400238d08cdf1ca20d49bafb85f4e224348bf9d).


-------
Attacks

https://www.twistlock.com/labs-blog/breaking-docker-via-runc-explaining-cve-2019-5736/

https://www.openwall.com/lists/oss-security/2019/02/13/3

https://www.twistlock.com/labs-blog/breaking-docker-via-runc-explaining-cve-2019-5736/

https://raw.githubusercontent.com/twistlock/RunC-CVE-2019-5736/master/malicious_image_POC/overwrite_runc.c
