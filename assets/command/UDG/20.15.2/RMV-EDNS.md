---
id: UDG@20.15.2@MMLCommand@RMV EDNS
type: MMLCommand
name: RMV EDNS（删除EDNS）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EDNS
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
- EDNS
status: active
---

# RMV EDNS（删除EDNS）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除EDNS的相关配置。用于取消用户相应的EDNS配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EDNSNAME | EDNS名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置EDNS的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EDNS的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- DNN：指定插入项的类型为DNN。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- USERDEF1：指定插入项的类型为用户自定义类型。<br>- USERDEF2：指定插入项的类型为用户自定义类型。<br>- USERDEF3：指定插入项的类型为用户自定义类型。<br>- USERDEF4：指定插入项的类型为用户自定义类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EDNS]] · EDNS（EDNS）

## 使用实例

假如运营商想删除名称为“edns1”，DataType为USERDEF1的EDNS记录：

```
RMV EDNS: EDNSNAME="edns1", DATATYPE=USERDEF1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除EDNS（RMV-EDNS）_83909786.md`
