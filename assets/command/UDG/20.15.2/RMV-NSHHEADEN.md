---
id: UDG@20.15.2@MMLCommand@RMV NSHHEADEN
type: MMLCommand
name: RMV NSHHEADEN（删除NSH头增强）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NSHHEADEN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- NSH参数
status: active
---

# RMV NSHHEADEN（删除NSH头增强）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除NSH头增强的相关配置。用于取消用户相应的NSH头增强配置。

## 注意事项

- 该命令执行后立即生效。
- 已经被绑定到GLBNSHHDNPLY命令中的NSH头增强不允许全删除，若需要删除全部该NSH头增强的信息，需要先执行RTR GLBNSHHDNPLY命令解除绑定关系后，再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSHNAME | NSH头增强名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置NSH头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSH头增强的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- RAT1：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- MCC_MNC1：指定插入项的类型为MCC_MNC1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NSH头增强（NSHHEADEN）](configobject/UDG/20.15.2/NSHHEADEN.md)

## 使用实例

假如运营商想删除名称为“nsh”，加密为“MSISDN1”的NSH头增强记录：

```
RMV NSHHEADEN: NSHNAME="nsh", DATATYPE=MSISDN1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除NSH头增强（RMV-NSHHEADEN）_28121345.md`
