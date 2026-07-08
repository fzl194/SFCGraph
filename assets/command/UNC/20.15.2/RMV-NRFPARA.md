---
id: UNC@20.15.2@MMLCommand@RMV NRFPARA
type: MMLCommand
name: RMV NRFPARA（删除NRF协议参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- NRF配置参数管理
status: active
---

# RMV NRFPARA（删除NRF协议参数）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于删除NRF协议相关的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NRF命令中的“NRF实例名称”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [NRF协议参数（NRFPARA）](configobject/UNC/20.15.2/NRFPARA.md)

## 使用实例

删除实例名为NRF_Instance_0的NRF的参数配置信息。

```
RMV NRFPARA: NRFINSTANCENAME="NRF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NRF协议参数（RMV-NRFPARA）_09651539.md`
