---
id: UDG@20.15.2@ConfigObject@KEYCHAIN
type: ConfigObject
name: KEYCHAIN（Keychain的配置）
nf: UDG
version: 20.15.2
object_name: KEYCHAIN
object_kind: entity
status: active
---

# KEYCHAIN（Keychain的配置）

## 说明

该命令用于设置Keychain的全局属性。

Keychain提供对所有应用层协议的认证，并且Keychain能够在不丢包的情况下，动态更改密码链。

为了安全，在网络上需要不断对应用层的认证信息进行更改。通过认证算法和共享安全密钥共同决定信息在不安全的网络上进行传输时是否被篡改。这种认证方式对数据进行认证时，需要数据发送者和接收者之间共享安全密钥和认证算法。并且密钥不能在网络上进行传输。

如果每个应用层协议维护一套认证规则（包括认证算法和密钥），将会有大量的应用程序采用相同的认证方式。这将导致认证信息被复制和更改。同样，如果每个应用程序都采用一个固定的认证密钥，每次更改需要网络管理员手工修改。手工更改密钥或认证算法将是非常复杂和烦琐的，要想实现更改所有路由器的密码而不丢包将是非常困难的。

因此，需要系统能够集中管理所有的认证处理和更改认证算法和密钥，而无需过多的人工干预。Keychain就实现了这个功能。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-KEYCHAIN]] · ADD KEYCHAIN
- [[command/UDG/20.15.2/LST-KEYCHAIN]] · LST KEYCHAIN
- [[command/UDG/20.15.2/MOD-KEYCHAIN]] · MOD KEYCHAIN
- [[command/UDG/20.15.2/RMV-KEYCHAIN]] · RMV KEYCHAIN

## 证据

- 原始手册：`evidence/UDG/20.15.2/KEYCHAIN.md`
- 原始手册：`evidence/UDG/20.15.2/KEYCHAIN.md`
- 原始手册：`evidence/UDG/20.15.2/KEYCHAIN.md`
- 原始手册：`evidence/UDG/20.15.2/KEYCHAIN.md`
