---
id: UNC@20.15.2@MMLCommand@RMV APNDNS
type: MMLCommand
name: RMV APNDNS（删除APN DNS域名策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNDNS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- APN DNS域名策略
status: active
---

# RMV APNDNS（删除APN DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于删除APN DNS域名策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。详见命令<br>[**ADD APNDNS**](增加APN DNS域名策略(ADD APNDNS)_26145932.md)<br>。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无 |
| UEACCCAP | UE接入能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE接入2/3/4G网络的能力。<br>数据来源：整网规划<br>取值范围：<br>- “GERAN/UTRAN_UE(GERAN/UTRAN UE)”<br>- “EUTRAN_UE(EUTRAN UE)”<br>- “GERAN/UTRAN/EUTRAN_UE(GERAN/UTRAN/EUTRAN UE)”<br>- “ALL_UE(ALL UE)”<br>默认值 ：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNDNS]] · APN DNS域名策略（APNDNS）

## 使用实例

删除 “APN网络标识” 为“huawei.com”， “根据UE接入能力选择” 为 “EUTRAN_UE(EUTRAN UE)” 的DNS策略:

**RMV APNDNS: APNNI="huawei.com", UEACCCAP=EUTRAN_UE;**

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNDNS.md`
