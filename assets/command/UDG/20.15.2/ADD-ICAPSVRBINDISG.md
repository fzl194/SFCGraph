---
id: UDG@20.15.2@MMLCommand@ADD ICAPSVRBINDISG
type: MMLCommand
name: ADD ICAPSVRBINDISG（增加ICAP服务器绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ICAPSVRBINDISG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 300
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器绑定
status: active
---

# ADD ICAPSVRBINDISG（增加ICAP服务器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于向ICAP Server Group实例中绑定ICAP Server信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为300。
- 要配置此命令，需要首先配置ICAP Server和ICAP Server Group。
- 一个ICAP Server Group实例中最多可以配置10个ICAP Server。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSVRGRP命令配置生成。 |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSERVER命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICAPSVRBINDISG]] · ICAP服务器绑定关系（ICAPSVRBINDISG）

## 关联任务

- [[UDG@20.15.2@Task@0-00261]]

## 使用实例

增加ICAP Server服务器绑定信息：

```
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="isg1",ICAPSERVERNAME="is1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加ICAP服务器绑定关系（ADD-ICAPSVRBINDISG）_29222372.md`
