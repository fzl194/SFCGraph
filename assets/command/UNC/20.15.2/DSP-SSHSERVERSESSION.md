---
id: UNC@20.15.2@MMLCommand@DSP SSHSERVERSESSION
type: MMLCommand
name: DSP SSHSERVERSESSION（显示SSH服务端会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SSHSERVERSESSION
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 接入配置管理
- SSH Server
- 服务端会话信息
status: active
---

# DSP SSHSERVERSESSION（显示SSH服务端会话信息）

## 功能

本命令用于显示SSH服务器session信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SSHSERVERSESSION]] · SSH服务端会话信息（SSHSERVERSESSION）

## 使用实例

显示SSH服务器session信息：

```
DSP SSHSERVERSESSION:;
```

```

RETCODE = 0 操作成功

结果如下
------------------------
  SSH服务端的会话号  =  1
    SSH服务端的索引  =  VTY 0
            SSH版本  =  2.0
          SSH用户名  =  admin
       会话重试次数  =  1
       Ctos加密算法  =  aes256-ctr
       Stoc加密算法  =  aes256-ctr
      Ctos HMAC算法  =  hmac-sha2-256
      Stoc HMAC算法  =  hmac-sha2-256
       Ctos压缩算法  =  none
       Stoc压缩算法  =  none
           交换算法  =  diffie-hellman-group-exchange-sha256
     会话的密钥类型  =  DSA
         服务端类型  =  stelnet
           认证类型  =  密码
         服务端端口  =  6000
         客户端端口  =  1936
       服务端IP地址  =  192.168.2.3
       客户端IP地址  =  192.168.2.5
        VPN实例名称  =  __mpp_vpn_outer__
           空闲时间  =  00:00:00
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SSHSERVERSESSION.md`
