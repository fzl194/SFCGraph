---
id: UDG@20.15.2@MMLCommand@RMV L2TPRDSCLIENT
type: MMLCommand
name: RMV L2TPRDSCLIENT（删除APN绑定的L2TP接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L2TPRDSCLIENT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- APN绑定L2TP接口
status: active
---

# RMV L2TPRDSCLIENT（删除APN绑定的L2TP接口）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除指定APN上的源端Gi接口绑定关系。若用户不再使用指定APN下绑定的接口作为系统与LNS交互时的源端接口时，可以使用该命令删除绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令不指定源端接口名称场景，只删除没有用户存在的绑定关系，可以使用LST L2TPRDSCLIENT命令查询删除结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。<br>默认值：无<br>配置原则：无 |
| INTERFACENAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：指定源端Gi接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPRDSCLIENT]] · APN绑定的L2TP接口（L2TPRDSCLIENT）

## 使用实例

假设客户不再使用APN “huawei.com”下绑定的“giif1/0/0”接口作为与LNS交互时的源端接口时，使用该命令删除绑定关系：

```
RMV L2TPRDSCLIENT:APN="huawei.com",INTERFACENAME="giif1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-L2TPRDSCLIENT.md`
