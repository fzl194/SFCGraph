---
id: UDG@20.15.2@MMLCommand@RMV CFWHITEURLLST
type: MMLCommand
name: RMV CFWHITEURLLST（删除URL过滤白名单列表）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFWHITEURLLST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- URL过滤白名单列表配置
status: active
---

# RMV CFWHITEURLLST（删除URL过滤白名单列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除一个URL过滤白名单列表。

## 注意事项

该命令执行后60s生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTNAME | URL过滤白名单名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置URL过滤白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFWHITEURLLST]] · URL过滤白名单列表（CFWHITEURLLST）

## 使用实例

删除一个URL过滤白名单列表：

```
RMV CFWHITEURLLST: WHITELISTNAME="whitelist1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CFWHITEURLLST.md`
