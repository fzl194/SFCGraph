---
id: UNC@20.15.2@MMLCommand@RMV CAUSEGRP
type: MMLCommand
name: RMV CAUSEGRP（删除原因值映射组配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV CAUSEGRP（删除原因值映射组配置）

## 功能

**适用网元：SGSN、MME**

此命令用于删除一个原因值映射组配置记录。

## 注意事项

- 此命令执行后立即生效。
- 当删除一个原因值映射组时，一定确保在GMMPROCTRL、PMMPROCTRL、EMMPROCTRL、EMMPROCTRLIMSI、GBSMPROCTRL、IUSMPROCTRL、S1SMPROCTRL和CAUSEMAP命令中无引用该ID记录，否则执行删除时系统提示CAUSEGRPID已被某个协议参数值使用，然后中断删除操作。建议通过查询命令确认在哪里使用CAUSEGRPID并删除那一条记录，再执行此删除命令。
- 当软参[“BYTE_EX_B86”BIT5](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT6](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT7](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B86”BIT8](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B87”BIT1](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)、[“BYTE_EX_B87”BIT2](../../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明_57771184.md)中的任意一个设置为“1”时，如果使用了该配置，进行配置增删改操作时需要同时考虑软参控制的场景。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：必选参数<br>参数含义：待删除的原因值组标识。<br>取值范围：1～127<br>默认值：无 |

## 操作的配置对象

- [原因值映射组配置（CAUSEGRP）](configobject/UNC/20.15.2/CAUSEGRP.md)

## 使用实例

当CAUSEGRPID值为126的原因值组标识未被任何协议使用时，删除CAUSEGRPID（原因值组标识）为126的原因值映射组记录：

RMV CAUSEGRP: CAUSEGRPID=126;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除原因值映射组配置(RMV-CAUSEGRP)_26305304.md`
