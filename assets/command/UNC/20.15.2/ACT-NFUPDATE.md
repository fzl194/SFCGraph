---
id: UNC@20.15.2@MMLCommand@ACT NFUPDATE
type: MMLCommand
name: ACT NFUPDATE（更新NF注册信息）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: NFUPDATE
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

# ACT NFUPDATE（更新NF注册信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于手动更新NF注册信息。在NF信息更新异常情况下，也可以尝试通过此命令进行手动更新。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHTYPE | 更新类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定更新注册信息的类型。<br>数据来源：对端协商<br>取值范围：<br>- PUTSWITCH（PUTSWITCH）<br>- PATCHSWITCH（PATCHSWITCH）<br>默认值：无<br>配置原则：<br>- PUTSWITCH(PUTSWITCH)：NF向NRF发起NF信息的全量更新。即使NF只有部分信息修改，也会将全部NF信息推送到NRF。<br>- PATCHSWITCH(PATCHSWITCH)：NF向NRF发起NF信息的部分更新。即，只更新NF变更的信息到NRF。为减轻NRF的负担，推荐采用部分更新的方式。 |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要更新注册信息的NF的实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数需要与ADD NFPROFILE命令中的NFINSTANCENAME值保持一致。<br>默认值：无<br>配置原则：<br>该参数需要与ADD NFPROFILE命令中的NFINSTANCENAME值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFUPDATE]] · 更新NF注册信息（NFUPDATE）

## 使用实例

需要全量更新实例名为AMF_Instance_0的NF注册信息：

```
ACT NFUPDATE: SWITCHTYPE=PUTSWITCH, NFINSTANCENAME="AMF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-NFUPDATE.md`
