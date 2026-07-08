---
id: UNC@20.15.2@MMLCommand@ADD NFSERVICEVER
type: MMLCommand
name: ADD NFSERVICEVER（添加NF服务版本信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFSERVICEVER
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF服务版本管理
status: active
---

# ADD NFSERVICEVER（添加NF服务版本信息）

## 功能

![](添加NF服务版本信息（ADD NFSERVICEVER）_09653292.assets/notice_3.0-zh-cn_2.png)

若APIFULLVERSION配置不符合规范，会导致业务校验APIVERSIONINURI失败。

**适用NF：AMF、SMF、NSSF、NRF、SMSF、NCG**

该命令用于添加NFS实例的版本信息。NF向NRF注册的时候可以将NFS的该版本信息带给NRF，在后续的NF发现流程中，NRF可以自行根据版本信息进行决策。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NFS实例所归属的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NFS实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数与ADD NFSERVICE命令中的SRVINSTANCEID值一致时生效。 |
| APIFULLVERSION | API版本信息 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NFS的全量版本信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 本参数的构成字符建议是字母A～Z或a～z、数字0～9、点“.”、加号“+”，和中划线“-”，例如1.0.0，1.0.0-alpha.1，3.0.1+orange.2020-09。<br>- 此参数点分格式的第一段即为注册到NRF的API缩略版本信息，即例如此参数为1.0.0，则API缩略版本信息为v1。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFSERVICEVER]] · NF服务版本信息（NFSERVICEVER）

## 使用实例

运营商A需要在NFINSTANCENAME为AMF_Instance_0，SRVINSTANCEID为Service_Instance_0的服务实例下添加1.0.0版本号。

```
ADD NFSERVICEVER: NFINSTANCENAME="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", APIFULLVERSION="1.0.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NFSERVICEVER.md`
