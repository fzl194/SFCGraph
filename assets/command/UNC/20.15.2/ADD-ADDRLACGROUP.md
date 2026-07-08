---
id: UNC@20.15.2@MMLCommand@ADD ADDRLACGROUP
type: MMLCommand
name: ADD ADDRLACGROUP（增加LAC组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ADDRLACGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配LAC组
status: active
---

# ADD ADDRLACGROUP（增加LAC组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来添加一个新的LAC组。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRLACGROUP]] · LAC组（ADDRLACGROUP）

## 使用实例

添加一个新的LAC组“beijing”：

```
ADD ADDRLACGROUP:LACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ADDRLACGROUP.md`
