---
id: UNC@20.15.2@MMLCommand@ADD DNNGRP
type: MMLCommand
name: ADD DNNGRP（增加DNN群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNNGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- DNN群组标识管理
status: active
---

# ADD DNNGRP（增加DNN群组）

## 功能

**适用NF：AMF**

该命令用于配置DNN群组。AMF支持为具有相同属性（比如发现相同的目标SMF）的DNN配置到同一个群组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入16条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个DNN群组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对DNN群组的描述信息，在运维过程中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNGRP]] · DNN群组（DNNGRP）

## 使用实例

某集团旗下的企业使用了DNNa、DNNb等多个DNN，企业员工在使用上述DNN时都需要选择到指定服务范围的目标SMF，为了节省配置记录，将上述DNN配置到同一个群组。首先添加DNN群组标识，执行命令如下：

```
ADD DNNGRP: DNNGRPID="BIG_GROUP", DESC="for SMF selection";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DNN群组（ADD-DNNGRP）_64343822.md`
