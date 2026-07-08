---
id: UDG@20.15.2@MMLCommand@SET SFTPALG
type: MMLCommand
name: SET SFTPALG（设置SFTP协议算法）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFTPALG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 文件传输
status: active
---

# SET SFTPALG（设置SFTP协议算法）

## 功能

设置SFTP协议是否使用兼容性算法。

![](设置SFTP协议算法(SET SFTPALG)_33293650.assets/notice_3.0-zh-cn.png)

如果将 “SFTP协议算法开关” 设置为 “ON（开启兼容算法）” ，系统会使用兼容算法，请谨慎处理。

> **说明**
> 使用 [**SET SFTPALG**](设置SFTP协议算法(SET SFTPALG)_33293650.md#ZH-CN_MMLREF_0000001733293650) 关闭兼容算法后为保证业务连续性，不会将之前建立的SFTP链接关闭，建议用户重新建立SFTP链接，保证系统安全。
>
> *表1 SFTP算法列表*
>
> | 算法类型 | 交互算法类型 | 算法 |
> | --- | --- | --- |
> | 不兼容算法 | 密钥交换算法 | curve25519-sha256@libssh.org、 curve25519-sha256、curve448-sha512、 ecdh-sha2-nistp521、ecdh-sha2-nistp384、 ecdh-sha2-nistp256、diffie-hellman-group-exchange-sha256、diffie-hellman-group18-sha512、diffie-hellman-group17-sha512、diffie-hellman-group16-sha512、 diffie-hellman-group15-sha512、diffie-hellman-group14-sha256 |
> | 不兼容算法 | 主机加密算法 | aes256-gcm@openssh.com、aes256-ctr、chacha20-poly1305@openssh.com、aes192-ctr、aes128-gcm@openssh.com、aes128-ctr |
> | 不兼容算法 | MAC算法 | hmac-sha2-512-etm@openssh.com、hmac-sha2-512、hmac-sha2-256-etm@openssh.com、hmac-sha2-256 |
> | 不兼容算法 | 主机密钥算法 | ssh-ed25519-cert-v01@openssh.com、ggssh-ed25519、sk-ssh-ed25519@openssh.com、sk-ecdsa-sha2-nistp256@openssh.com、rsa-sha2-512-cert-v01@openssh.com、rsa-sha2-512、rsa-sha2-256-cert-v01@openssh.com、rsa-sha2-256、ecdsa-sha2-nistp521-cert-v01@openssh.com、nistp521、ecdsa-sha2-nistp384-cert-v01@openssh.com、nistp384、ecdsa-sha2-nistp256-cert-v01@openssh.com、nistp256 |
> | 兼容算法 | 密钥交换算法 | curve25519-sha256@libssh.org、curve25519-sha256、curve448-sha512、ecdh-sha2-nistp521、ecdh-sha2-nistp384、ecdh-sha2-nistp256、diffie-hellman-group-exchange-sha256、diffie-hellman-group18-sha512、diffie-hellman-group17-sha512、diffie-hellman-group16-sha512、 diffie-hellman-group15-sha512、diffie-hellman-group14-sha256、diffie-hellman-group-exchange-sha1、diffie-hellman-group14-sha1、diffie-hellman-group1-sha1 |
> | 兼容算法 | 主机加密算法 | aes256-gcm@openssh.com、aes256-ctr、aes192-ctr、aes128-gcm@openssh.com、aes128-ctr、chacha20-poly1305@openssh.com、aes256-cbc、aes192-cbc、aes128-cbc、arcfour256、arcfour128、blowfish-cbc、3des-cbc |
> | 兼容算法 | MAC算法 | hmac-sha2-512-etm@openssh.com、hmac-sha2-512、hmac-sha2-256-etm@openssh.com、hmac-sha2-256、hmac-sha1-etm@openssh.com、hmac-sha1、hmac-sha1-96、hmac-md5-96、hmac-md5 |
> | 兼容算法 | 主机密钥算法 | ssh-ed25519-cert-v01@openssh.com、ssh-ed25519、sk-ssh-ed25519@openssh.com、sk-ecdsa-sha2-nistp256@openssh.com、rsa-sha2-512-cert-v01@openssh.com、rsa-sha2-512、rsa-sha2-256-cert-v01@openssh.com、rsa-sha2-256、ecdsa-sha2-nistp521-cert-v01@openssh.com、nistp521、ecdsa-sha2-nistp384-cert-v01@openssh.com、nistp384、 ecdsa-sha2-nistp256-cert-v01@openssh.com、nistp256、ssh-rsa、ssh-rsa-cert-v01@openssh.com、ssh-dss-cert-v01@openssh.com、ssh-dss |

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFTPALGSWITCH | SFTP协议算法开关 | 可选必选说明：必选参数。<br>参数含义：SFTP协议算法开关<br>取值范围：<br>- ON（开启兼容算法）<br>- OFF（关闭兼容算法）<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [SFTP协议算法（SFTPALG）](configobject/UDG/20.15.2/SFTPALG.md)

## 使用实例

设置 “SFTP协议算法开关” 为 “ON（开启兼容算法）” 。

```
%%SET SFTPALG: SFTPALGSWITCH=ON;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置SFTP协议算法(SET-SFTPALG)_33293650.md`
