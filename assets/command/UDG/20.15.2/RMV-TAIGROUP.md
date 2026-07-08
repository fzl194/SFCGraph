---
id: UDG@20.15.2@MMLCommand@RMV TAIGROUP
type: MMLCommand
name: RMV TAIGROUP（删除指定的TAI组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TAIGROUP
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组
status: active
---

# RMV TAIGROUP（删除指定的TAI组）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来删除指定的TAI组。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 删除TAI组时，会删除该TAI组下的所有绑定的TAC号段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TAIGROUP]] · 指定的TAI组（TAIGROUP）

## 使用实例

假设运营商需要去删除一个本地已经配置的TAI组beijing：

```
RMV TAIGROUP: TAIGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TAIGROUP.md`
