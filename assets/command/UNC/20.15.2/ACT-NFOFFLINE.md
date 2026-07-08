---
id: UNC@20.15.2@MMLCommand@ACT NFOFFLINE
type: MMLCommand
name: ACT NFOFFLINE（激活NF下线）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: NFOFFLINE
command_category: 动作类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF 状态管理
status: active
---

# ACT NFOFFLINE（激活NF下线）

## 功能

![](激活NF下线（ACT NFOFFLINE）_09652524.assets/notice_3.0-zh-cn_2.png)

该命令用于激活NF下线，该命令执行以后，服务端场景下会触发NF向NRF的去注册处理，删除在NRF的注册，造成服务消费者无法发现该NF服务，导致该NF无法向外提供服务，请谨慎操作。

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用来激活NF向NRF去注册。在NF进行升级、重装或重大网络调整等情况下，如果希望暂时不被其他NF发现，可以通过本命令触发NF到NRF的去注册。去注册会导致其他NF无法发现该NF，可能导致业务异常，请谨慎操作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFPROFILE命令中的NFINSTANCENAME值保持一致。NFINSTANCENAME值可通过LST NFPROFILE获得。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFOFFLINE]] · NF下线（NFOFFLINE）

## 使用实例

激活AMF_Instance_0向NRF去注册。

```
ACT NFOFFLINE: NFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-NFOFFLINE.md`
