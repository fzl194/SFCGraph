---
id: UDG@20.15.2@ConfigObject@PWDBLACKLIST
type: ConfigObject
name: PWDBLACKLIST（密码禁用词）
nf: UDG
version: 20.15.2
object_name: PWDBLACKLIST
object_kind: entity
status: active
---

# PWDBLACKLIST（密码禁用词）

## 说明

该命令用于增加密码禁用词。配置密码禁用词后，所有包含密码禁用词的字符串（不区分大小写）都不能被配置成本地用户的密码。可以通过执行查询本地用户（ [**LST OP**](../用户/查询本地用户（LST OP）_59036769.md) ）命令查看本地用户的信息。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-PWDBLACKLIST]] · ADD PWDBLACKLIST
- [[command/UDG/20.15.2/LST-PWDBLACKLIST]] · LST PWDBLACKLIST
- [[command/UDG/20.15.2/RMV-PWDBLACKLIST]] · RMV PWDBLACKLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除密码禁用词（RMV-PWDBLACKLIST）_59036566.md`
- 原始手册：`evidence/UDG/20.15.2/增加密码禁用词（ADD-PWDBLACKLIST）_59036534.md`
- 原始手册：`evidence/UDG/20.15.2/查询密码禁用词（LST-PWDBLACKLIST）_59036662.md`
