---
id: UNC@20.15.2@MMLCommand@RMV CHARGECHAR
type: MMLCommand
name: RMV CHARGECHAR（删除对本地用户、漫游用户、拜访用户所采用的计费属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHARGECHAR
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 基本计费属性
status: active
---

# RMV CHARGECHAR（删除对本地用户、漫游用户、拜访用户所采用的计费属性）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除计费属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCNAME | 计费属性名称 | 可选必选说明：必选参数<br>参数含义：计费属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对本地用户、漫游用户、拜访用户所采用的计费属性（CHARGECHAR）](configobject/UNC/20.15.2/CHARGECHAR.md)

## 使用实例

删除计费属性名称为“cc”的所有配置信息：

```
RMV CHARGECHAR:CCNAME="cc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV-CHARGECHAR）_09896811.md`
