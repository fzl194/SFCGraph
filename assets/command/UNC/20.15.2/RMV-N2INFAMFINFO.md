---
id: UNC@20.15.2@MMLCommand@RMV N2INFAMFINFO
type: MMLCommand
name: RMV N2INFAMFINFO（删除AMF的N2接口信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: N2INFAMFINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF的N2接口信息管理
status: active
---

# RMV N2INFAMFINFO（删除AMF的N2接口信息）

## 功能

**适用NF：AMF**

该命令用于删除当前AMF的N2接口信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2INFAMFINFO]] · AMF的N2接口信息（N2INFAMFINFO）

## 使用实例

运营商A需要删掉当前AMF的N2接口信息。

```
RMV N2INFAMFINFO: NFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-N2INFAMFINFO.md`
