---
id: UNC@20.15.2@MMLCommand@RMV BSFINFO
type: MMLCommand
name: RMV BSFINFO（删除BSF信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BSFINFO
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# RMV BSFINFO（删除BSF信息）

## 功能

**适用NF：SMF**

该命令用于删除BSF实例信息。删除BSF后，AF无法选到正确的PCF，导致语音业务受影响。

## 注意事项

- 该命令执行后立即生效。

- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSFINFO]] · BSF信息（BSFINFO）

## 使用实例

删除当前配置的某BSF，其实例名称是BSF_Instance_0：

```
RMV BSFINFO: BSFINSTANCENAME="BSF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BSFINFO.md`
