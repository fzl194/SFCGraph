---
id: UDG@20.15.2@MMLCommand@RMV ICAPSVRBINDISG
type: MMLCommand
name: RMV ICAPSVRBINDISG（删除ICAP服务器绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ICAPSVRBINDISG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器绑定
status: active
---

# RMV ICAPSVRBINDISG（删除ICAP服务器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于解除指定名称的ICAP Server Group和ICAP Server实例的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICAPSVRBINDISG]] · ICAP服务器绑定关系（ICAPSVRBINDISG）

## 使用实例

删除ICAP Server服务器is1与ICAP服务器组isg1的绑定信息：

```
RMV ICAPSVRBINDISG:ICAPSVRGRPNAME="isg1",ICAPSERVERNAME="is1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ICAPSVRBINDISG.md`
