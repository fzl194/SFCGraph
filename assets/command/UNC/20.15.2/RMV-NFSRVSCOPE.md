---
id: UNC@20.15.2@MMLCommand@RMV NFSRVSCOPE
type: MMLCommand
name: RMV NFSRVSCOPE（删除NF支持服务区信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFSRVSCOPE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务区管理
status: active
---

# RMV NFSRVSCOPE（删除NF支持服务区信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于删除NF实例支持的服务区信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SCOPENAME | 服务区名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，City_A。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSRVSCOPE]] · NF支持服务区信息（NFSRVSCOPE）

## 使用实例

运营商A需要在NFINSTANCENAME为AMF_Instance_0的NF实例下删除服务区名称CityA。

```
RMV NFSRVSCOPE: NFINSTANCENAME="AMF_Instance_0", SCOPENAME="CityA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NFSRVSCOPE.md`
