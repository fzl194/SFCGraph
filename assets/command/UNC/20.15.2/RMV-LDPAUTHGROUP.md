---
id: UNC@20.15.2@MMLCommand@RMV LDPAUTHGROUP
type: MMLCommand
name: RMV LDPAUTHGROUP（删除LDP认证组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LDPAUTHGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP认证组管理
status: active
---

# RMV LDPAUTHGROUP（删除LDP认证组）

## 功能

该命令用于删除LDP认证组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| AUTHPEERGROUPNAME | 认证组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定认证组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPAUTHGROUP]] · LDP认证组（LDPAUTHGROUP）

## 使用实例

删除LDP认证组：

```
RMV LDPAUTHGROUP:VRFNAME="_public_",AUTHPEERGROUPNAME="bb";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LDPAUTHGROUP.md`
