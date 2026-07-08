---
id: UDG@20.15.2@MMLCommand@RMV GRAYUPTSTUSER
type: MMLCommand
name: RMV GRAYUPTSTUSER（删除灰度升级拨测用户）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GRAYUPTSTUSER
command_category: 配置类
applicable_nf:
- UPF
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 灰度升级拨测用户信息
status: active
---

# RMV GRAYUPTSTUSER（删除灰度升级拨测用户）

## 功能

**适用NF：UPF、SGW-U、PGW-U**

该命令用于删除拨测用户信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRAYUSERNAME | 拨测用户名称 | 可选必选说明：必选参数<br>参数含义：拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GRAYUPTSTUSER]] · 灰度升级拨测用户（GRAYUPTSTUSER）

## 使用实例

删除拨测用户的IMSI信息，命令为：

```
RMV GRAYUPTSTUSER: GRAYUSERNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-GRAYUPTSTUSER.md`
