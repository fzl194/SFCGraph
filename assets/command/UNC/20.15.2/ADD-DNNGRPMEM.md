---
id: UNC@20.15.2@MMLCommand@ADD DNNGRPMEM
type: MMLCommand
name: ADD DNNGRPMEM（增加DNN群组成员）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD DNNGRPMEM（增加DNN群组成员）

## 功能

**适用NF：AMF**

该命令用于为DNN群组添加DNN成员，一次执行添加一个群组成员。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN群组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该参数依赖于DNNGRP对象，请确保相应DNNGRP已创建。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置到群组的DNN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNNGRPMEM]] · DNN群组成员（DNNGRPMEM）

## 使用实例

将DNNa添加到名称为“BIG_GROUP”的DNN群组中，执行如下命令：

```
ADD DNNGRPMEM: DNNGRPID="BIG_GROUP", DNN="DNNa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DNNGRPMEM.md`
