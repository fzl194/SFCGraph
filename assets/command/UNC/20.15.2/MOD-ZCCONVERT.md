---
id: UNC@20.15.2@MMLCommand@MOD ZCCONVERT
type: MMLCommand
name: MOD ZCCONVERT（修改区域码转换策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ZCCONVERT
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
- 区域漫游限制管理
- 区域码转换
status: active
---

# MOD ZCCONVERT（修改区域码转换策略）

## 功能

**适用网元：SGSN、MME**

此命令用于修改区域码转换策略。

## 注意事项

- 此命令执行后立即生效。
- 区域码转换策略仅在[**SET MMFUNC**](../../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)的参数“区域码”设置为“YES（是）”时，才能生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改区域码转换策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无<br>说明：区域码转换策略优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）”。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO运营商标识。 对于本网用户，该参数是为该用户归属的MNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定区域码转换的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| CONVERTPLCY | 转换策略 | 可选必选说明：必选参数<br>参数含义：本参数取值为“IGNORE_SUB_ZC（忽略签约ZC）”时，表示忽略用户的签约ZC，<br>UNC<br>不再根据签约ZC进行接入控制，直接允许用户接入。本参数取值为“OVERWRITE_DIRECTLY（采用指定ZC）”时，表示无论用户是否存在签约ZC，均使用本命令指定的ZC进行ZC接入限制。本参数取值为“OVERWRITE_IF_SUB（签约则采用指定ZC）”时，表示如果用户存在签约ZC，使用本命令指定的ZC进行ZC接入限制。<br>数据来源：全网规划<br>取值范围：<br>- “IGNORE_SUB_ZC(忽略签约ZC)”<br>- “OVERWRITE_DIRECTLY(采用指定ZC)”<br>- “OVERWRITE_IF_SUB(签约则采用指定ZC)”<br>默认值：无 |
| ZC | 区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定区域码。<br>前提条件：该参数需要在<br>[**ADD ZC**](../区域码/增加区域码(ADD ZC)_26305376.md)<br>中事先配置，可执行<br>[**LST ZC**](../区域码/查询区域码(LST ZC)_26145566.md)<br>进行查看。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 输入16进制数时，可以直接输入，也可以在数字前加0X或0x。 |

## 操作的配置对象

- [区域码转换策略（ZCCONVERT）](configobject/UNC/20.15.2/ZCCONVERT.md)

## 使用实例

场景参见 [**ADD ZCCONVERT**](增加区域码转换策略(ADD ZCCONVERT)_26305378.md) 的命令使用实例。

将运营商标识为1的本网用户的转换策略修改为IGNORE_SUB_ZC：

MOD ZCCONVERT: SUBRANGE=HOME_USER, NOID=1, CONVERTPLCY=IGNORE_SUB_ZC;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改区域码转换策略(MOD-ZCCONVERT)_72345165.md`
