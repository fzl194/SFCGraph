---
id: UDG@20.15.2@MMLCommand@ACT UEINJECTSEND
type: MMLCommand
name: ACT UEINJECTSEND（发送UE灌包）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: UEINJECTSEND
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包测试
status: active
---

# ACT UEINJECTSEND（发送UE灌包）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](发送UE灌包（ACT UEINJECTSEND）_82837098.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，使能UE灌包功能会导致CPU负载率增高和对应UE的计费问题，需使能灌包操作前确认是否可以实施此操作。

该命令用于配置是否向指定UE执行下行灌包。

## 注意事项

- 该命令执行后只对已激活用户生效。
- 给UE灌包存在风险，需使能灌包操作前确认是否可以实施此操作。
- 为了保证正常业务不受影响，若DPE负载率高于80%，则暂停灌包。
- 建议当前灌包结束或者命令停止当前用户灌包后，再对下一个用户灌包，多个用户同时灌包，可能后灌包的用户会失败。可以通过DSP UEINJECTSTAT命令查询当前灌包用户的信息。
- 下行灌包报文的Server地址需要从下行流量中学习，因此下行灌包使能后需要有下行背景流量才会执行灌包。
- 系统优选PSA-UPF实施灌包。若采用I-UPF和PSA-UPF分离部署的方式，则会在I-UPF上产生下行灌包报文对应的计费信息；若采用I-UPF和PSA-UPF合一部署的方式，则不会在I-UPF或PSA-UPF上产生下行灌包报文对应的计费信息。
- 系统RMM日志会记录下行灌包次数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>- IMEI：用于指定用户标识为IMEI。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户ID信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。 3、当用户ID类型为IMEI时，长度范围是1～16，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否向指定用户ID标识的UE执行下行灌包。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PF_ACT_DISABLE：执行去使能。<br>- PF_ACT_ENABLE：执行使能。<br>默认值：PF_ACT_ENABLE<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示灌包UE所在的APN，仅对指定APN下的激活UE进行灌包，避免UE有多个APN时，同时灌包。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示灌包UE的IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [发送UE灌包（UEINJECTSEND）](configobject/UDG/20.15.2/UEINJECTSEND.md)

## 使用实例

使能指定imsi为12345678901234的UE下行灌包操作：

```
ACT UEINJECTSEND: USERID=IMSI, USERIDINFO="12345678901234", SWITCH=PF_ACT_ENABLE, APN="apn1.com", IPTYPE = IPv4;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/发送UE灌包（ACT-UEINJECTSEND）_82837098.md`
