---
id: UDG@20.15.2@MMLCommand@SET PDFUNC
type: MMLCommand
name: SET PDFUNC（设置报文检测功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PDFUNC
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 数据转发控制
- 报文检测功能
status: active
---

# SET PDFUNC（设置报文检测功能配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置Tx-U接口的下行报文检测功能。如果开关使能，则系统会对Tx-U接口的下行报文进行校验。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TXUDOWN |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TXUDOWN | Tx-U接口下行报文 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭Tx-U接口下行报文检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [报文检测功能配置（PDFUNC）](configobject/UDG/20.15.2/PDFUNC.md)

## 使用实例

将Tx-U接口的下行报文检测功能设置为使能：

```
SET PDFUNC: TXUDOWN=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置报文检测功能配置（SET-PDFUNC）_70282538.md`
