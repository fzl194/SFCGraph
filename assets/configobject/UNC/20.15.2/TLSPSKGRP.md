---
id: UNC@20.15.2@ConfigObject@TLSPSKGRP
type: ConfigObject
name: TLSPSKGRP（预共享密钥组信息）
nf: UNC
version: 20.15.2
object_name: TLSPSKGRP
object_kind: entity
status: active
---

# TLSPSKGRP（预共享密钥组信息）

## 说明

该命令用于增加预共享密钥组。

当需要建立HTTPS链路且使用预共享密钥方式进行认证时，可通过此命令添加预共享密钥组，用于关联一个或多个预共享密钥。

客户端发起建链时会随机选择组内某一个预共享密钥，并在TLS建链消息中携带预共享密钥标识。服务端从TLS建链消息中提取预共享密钥标识，匹配组内预共享密钥标识，获取对应的预共享密钥进行建链协商。

当需要平滑替换某个预共享密钥，可先后在服务端和客户端通过命令 [**ADD TLSPSK**](../HTTP TLS预共享密钥管理/增加预共享密钥（ADD TLSPSK）_07669721.md) 在同一组内添加新的预共享密钥信息，然后先后在客户端和服务端执行 [**RMV TLSPSK**](../HTTP TLS预共享密钥管理/删除预共享密钥（RMV TLSPSK）_57029816.md) 命令删除不再使用的预共享密钥信息，保证业务无损。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TLSPSKGRP]] · ADD TLSPSKGRP
- [[command/UNC/20.15.2/LST-TLSPSKGRP]] · LST TLSPSKGRP
- [[command/UNC/20.15.2/MOD-TLSPSKGRP]] · MOD TLSPSKGRP
- [[command/UNC/20.15.2/RMV-TLSPSKGRP]] · RMV TLSPSKGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/TLSPSKGRP.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPSKGRP.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPSKGRP.md`
- 原始手册：`evidence/UNC/20.15.2/TLSPSKGRP.md`
