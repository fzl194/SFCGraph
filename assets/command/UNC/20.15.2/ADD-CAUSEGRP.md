---
id: UNC@20.15.2@MMLCommand@ADD CAUSEGRP
type: MMLCommand
name: ADD CAUSEGRP（增加原因值映射组配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CAUSEGRP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 127
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 原因值管理
- 原因值映射组配置
status: active
---

# ADD CAUSEGRP（增加原因值映射组配置）

## 功能

**适用网元：SGSN、MME**

此命令用于增加一个原因值映射组配置记录。每个原因值映射组表示一个原因值映射规则集合，通常将一个源接口和一个目标接口的原因值映射规则作为一个映射组，如Gr Cause to L3 cause，GTPC cause to L3 cause。CAUSEGRP通常是一组CAUSEMAP的集合。

## 注意事项

- 此命令最大记录数为127。
- 此命令执行后立即生效。
- 当软参[“BYTE_EX_B86”BIT5](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT5 控制MME发送给UE的Attach Reject消息中携带的EMM _babd70be_99362835.md)、[“BYTE_EX_B86”BIT6](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT6 控制MME发送给UE的Detach Request消息中携带的EMM_08cd63ac_99564219.md)、[“BYTE_EX_B86”BIT7](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT7 控制MME发送给UE的Service Reject消息中携带的EMM_02416554_01403356.md)、[“BYTE_EX_B86”BIT8](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B86 BIT8 控制MME发送给UE的TAU Reject消息中携带的EMM Cau_4ecaf854_01163560.md)、[“BYTE_EX_B87”BIT1](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT1 控制SGSN发送给MS的RAU Reject消息中携带的GMM Ca_d12fb174_99123339.md)、[“BYTE_EX_B87”BIT2](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B87 BIT2 控制在inter-MME TAU流程中由于二次Context Res_a61ceb84_00684116.md)中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：整网规划<br>取值范围：1～127<br>默认值：无 |
| CAUSEGRPNM | 原因值组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当前CAUSEGRPID对应的字符名称。<br>数据来源：整网规划<br>取值范围：1～32位的字符串<br>默认值：noname |

## 操作的配置对象

- [原因值映射组配置（CAUSEGRP）](configobject/UNC/20.15.2/CAUSEGRP.md)

## 使用实例

当某个协议的缺省原因值导致外围设备异常，要使用新增的原因值映射规则。增加一个CAUSEGRPID（原因值组标识）为126的原因值映射规则时，执行如下命令：

ADD CAUSEGRP: CAUSEGRPID=126, CAUSEGRPNM="default1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加原因值映射组配置(ADD-CAUSEGRP)_72225173.md`
