---
id: UNC@20.15.2@MMLCommand@RMV VLRKEYDATA
type: MMLCommand
name: RMV VLRKEYDATA（删除用户的VLR关键信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VLRKEYDATA
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 热备容灾
status: active
---

# RMV VLRKEYDATA（删除用户的VLR关键信息）

## 功能

**适用NF：SMSF**

该命令用于删除用户的VLR关键信息。当功能调测或拨测过程中需要手动删除用户的VLR关键信息时，使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI，在本命令中，可以按指定IMSI删除对应用户的VLR关键信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRKEYDATA]] · 用户的VLR关键信息（VLRKEYDATA）

## 使用实例

操作员在功能调测过程中手动删除值为“460023500100001”的IMSI对应的用户的VLR用户关键信息，执行如下命令：

```
RMV VLRKEYDATA: IMSI="460023500100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-VLRKEYDATA.md`
