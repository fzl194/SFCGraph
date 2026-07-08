---
id: UNC@20.15.2@MMLCommand@RMV NFPROFILE
type: MMLCommand
name: RMV NFPROFILE（删除NF实例概述信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFPROFILE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF概述信息管理
status: active
---

# RMV NFPROFILE（删除NF实例概述信息）

## 功能

![](删除NF实例概述信息（RMV NFPROFILE）_09651742.assets/notice_3.0-zh-cn_2.png)

当执行此命令时，会触发NF到NRF的去注册。去注册会导致其他NF无法发现该NF，可能导致业务异常，请谨慎操作。

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于删除NF实例的概述信息。

## 注意事项

- 该命令执行后立即生效。

- 当NF在注册态时，执行此命令后，会触发NF到NRF的去注册。如后续重新加回此配置时，需要重新执行ACT NFONLINE命令进行NF的注册。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，AMF_Instance_0。<br>- 本参数来源于ADD NFUUID命令中的“NF实例名称”参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFPROFILE]] · NF实例概述信息（NFPROFILE）

## 使用实例

运营商A需要删除NFINSTANCENAME为AMF_Instance_0的NF实例概述信息。

```
RMV NFPROFILE: NFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NFPROFILE.md`
