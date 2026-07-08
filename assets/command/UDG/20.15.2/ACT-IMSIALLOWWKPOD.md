---
id: UDG@20.15.2@MMLCommand@ACT IMSIALLOWWKPOD
type: MMLCommand
name: ACT IMSIALLOWWKPOD（允许IMSI在特定的Worker Pod上激活配置）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: IMSIALLOWWKPOD
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 允许IMSI在特定的Worker POD上激活
status: active
---

# ACT IMSIALLOWWKPOD（允许IMSI在特定的Worker Pod上激活配置）

## 功能

**适用NF：PGW-U、UPF**

允许IMSI在特定的Worker Pod上激活配置。

## 注意事项

- 激活或更新前已经配置ImsiAllowWkPod/ImsiBlockWkPod的用户，本命令是新数据流生效，否则是新激活或更新的用户生效。
- 同一个IMSI，同一个WORKERTYPE同一个PodName不允许既配置ACT ImsiAllowWkPod又配置ACT ImsiBlockWkPod。
- 该命令和ACT ImsiBlockWkPod总规格为64。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| WORKERTYPE | Worker类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Worker类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- to：TCP优化。<br>默认值：无<br>配置原则：无 |
| PODNAME | Pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：WORKERTYPE参数填写为to时，该参数需配置成TO-POD类型的POD名称。 |
| TIMEOUT | 超时时长 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置生效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～7200，单位是分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [允许IMSI在特定的Worker Pod上激活配置（IMSIALLOWWKPOD）](configobject/UDG/20.15.2/IMSIALLOWWKPOD.md)

## 使用实例

当需要允许IMSI 1234567890与to-pod-0、类型为to的POD的绑定关系时，且超时时长为120分钟，进行如下设置：

```
ACT IMSIALLOWWKPOD: IMSI="1234567890", PODNAME="to-pod-0", TIMEOUT=120, WORKERTYPE=to;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/允许IMSI在特定的Worker-Pod上激活配置（ACT-IMSIALLOWWKPOD）_87601019.md`
