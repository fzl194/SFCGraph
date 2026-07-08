---
id: UNC@20.15.2@MMLCommand@MOD CAUSEGRP
type: MMLCommand
name: MOD CAUSEGRP（修改原因值映射组配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CAUSEGRP
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
- 移动性管理
- 原因值管理
- 原因值映射组配置
status: active
---

# MOD CAUSEGRP（修改原因值映射组配置）

## 功能

**适用网元：SGSN、MME**

此命令用于修改原因值映射组配置。每个原因值映射组表示一个原因值映射规则集合，通常将一个源接口和一个目标接口的原因值映射规则作为一个映射组，如Gr Cause to L3 cause，GTPC cause to L3 cause。CAUSEGRP通常是一组CAUSEMAP的集合。

## 注意事项

- 此命令执行后立即生效。
- 当软参[“BYTE_EX_B86”BIT5](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT6](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT7](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT8](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B87”BIT1](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B87”BIT2](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：待修改的原因值组标识。<br>数据来源：整网规划<br>取值范围：1～127<br>默认值：无 |
| CAUSEGRPNM | 原因值组名称 | 可选必选说明：可选参数<br>参数含义：待修改的原因值名称。<br>数据来源：整网规划<br>取值范围：1～32位的字符串<br>默认值：无 |

## 操作的配置对象

- [原因值映射组配置（CAUSEGRP）](configobject/UNC/20.15.2/CAUSEGRP.md)

## 使用实例

当修改原因值组标识为126的原因值组名称时，把CAUSEGRPNM（原因值组名称）修改为aaa：

MOD CAUSEGRP: CAUSEGRPID=126, CAUSEGRPNM="aaa";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改原因值映射组配置(MOD-CAUSEGRP)_72345091.md`
