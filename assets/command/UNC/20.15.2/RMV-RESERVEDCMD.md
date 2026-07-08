---
id: UNC@20.15.2@MMLCommand@RMV RESERVEDCMD
type: MMLCommand
name: RMV RESERVEDCMD（删除补丁预留配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESERVEDCMD
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- SGSN
- MME
- SGW-C
- GGSN
- PGW-C
- SMSF
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 预留配置
status: active
---

# RMV RESERVEDCMD（删除补丁预留配置）

## 功能

**适用NF：AMF、SMF、NRF、SGSN、MME、SGW-C、GGSN、PGW-C、SMSF、NCG、NSSF**

删除补丁预留配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：功能名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESERVEDCMD]] · 补丁预留配置（RESERVEDCMD）

## 使用实例

删除补丁预留配置，其中功能名称为BALCKLIST，请运行以下命令：

```
RMV RESERVEDCMD: CMDNAME="BALCKLIST";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESERVEDCMD.md`
