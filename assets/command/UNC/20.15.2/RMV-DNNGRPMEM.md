---
id: UNC@20.15.2@MMLCommand@RMV DNNGRPMEM
type: MMLCommand
name: RMV DNNGRPMEM（删除DNN群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNNGRPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- DNN群组成员管理
status: active
---

# RMV DNNGRPMEM（删除DNN群组成员）

## 功能

**适用NF：AMF**

该命令用于删除DNN群组成员。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN群组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该参数依赖于DNNGRP对象，请确保相应DNNGRP已创建。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置到群组的DNN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNN群组成员（DNNGRPMEM）](configobject/UNC/20.15.2/DNNGRPMEM.md)

## 使用实例

将DNNb从名称为“BIG_GROUP”的DNN群组下删除，执行如下命令：

```
RMV DNNGRPMEM: DNNGRPID="BIG_GROUP", DNN="DNNb";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNN群组成员（RMV-DNNGRPMEM）_64343906.md`
