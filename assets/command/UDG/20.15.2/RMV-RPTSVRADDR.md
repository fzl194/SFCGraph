---
id: UDG@20.15.2@MMLCommand@RMV RPTSVRADDR
type: MMLCommand
name: RMV RPTSVRADDR（删除报表服务器接入点配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RPTSVRADDR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器地址
status: active
---

# RMV RPTSVRADDR（删除报表服务器接入点配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除报表服务器接入点。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACCESSNAME | 接入点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的接入点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [报表服务器接入点配置（RPTSVRADDR）](configobject/UDG/20.15.2/RPTSVRADDR.md)

## 使用实例

删除报表服务器接入点：

```
RMV RPTSVRADDR: ACCESSNAME="access01":;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除报表服务器接入点配置（RMV-RPTSVRADDR）_06453266.md`
