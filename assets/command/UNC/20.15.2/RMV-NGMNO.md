---
id: UNC@20.15.2@MMLCommand@RMV NGMNO
type: MMLCommand
name: RMV NGMNO（删除5G模式移动网络运营商信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGMNO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 5G 移动网络运营商管理
status: active
---

# RMV NGMNO（删除5G模式移动网络运营商信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于删除移动网络运营商基本信息。

“NOID”为0的默认记录不允许被删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统内唯一标识移动网络运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMNO]] · 5G模式移动网络运营商信息（NGMNO）

## 使用实例

删除退网运营商的信息，执行如下命令：

```
RMV NGMNO: NOID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGMNO.md`
