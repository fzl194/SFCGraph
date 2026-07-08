---
id: UDG@20.15.2@MMLCommand@RMV LACGROUP
type: MMLCommand
name: RMV LACGROUP（删除指定的LAC组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LACGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- LAC组
status: active
---

# RMV LACGROUP（删除指定的LAC组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除指定的LAC组。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 当LAC组下绑定LAC号段时，同时可以删除该LAC组下的所有绑定的LAC号段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | 指定LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LACGROUP]] · 指定的LAC组（LACGROUP）

## 使用实例

假设运营商需要去删除一个本地已经配置的LAC组beijing：

```
RMV LACGROUP:LACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除指定的LAC组（RMV-LACGROUP）_06054836.md`
