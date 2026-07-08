---
id: UNC@20.15.2@MMLCommand@RMV RFSP
type: MMLCommand
name: RMV RFSP（删除RFSP配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RFSP
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
- RFSP管理
- RFSP策略管理
- RFSP参数配置
status: active
---

# RMV RFSP（删除RFSP配置）

## 功能

**适用网元：SGSN、MME**

此命令用于删除RFSP ID配置记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置RFSP ID的用户范围。<br>取值范围：<br>- “ALL_IMSI(所有用户)”<br>- “SPECIAL_IMSI(指定用户)”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户群的IMSI前缀。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSI(指定用户)”<br>时有效。<br>取值范围：5～15位数字<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：<br>该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RFSP]] · RFSP配置（RFSP）

## 使用实例

场景参见 [**ADD RFSP**](增加RFSP配置(ADD RFSP)_26305350.md) 的命令使用实例。

删除NOID为0对应的漫游用户的RFSP ID，使NOID为0的漫游用户按照用户范围ALL_IMSI(业务优先级策略)配置的数据RFSP ID为3对应的频点优先级进行驻留控制：

RMV RFSP: SUBRANGE=FOREIGN_USER, NOID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除RFSP配置(RMV-RFSP)_72345137.md`
