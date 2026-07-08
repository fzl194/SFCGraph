---
id: UNC@20.15.2@MMLCommand@DSP MMCTXEXT
type: MMLCommand
name: DSP MMCTXEXT（显示MM上下文扩展信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MMCTXEXT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP MMCTXEXT（显示MM上下文扩展信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查看移动性管理(MM)上下文的相关扩展信息。

## 注意事项

- 该命令执行后立即生效。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：可选参数<br>参数说明：该参数用于指定查询MM上下文的查询方式。<br>取值范围：<br>- “BYIMSI(指定IMSI)”：表示根据IMSI查询用户的MM上下文。<br>- “BYMSISDN(指定MSISDN)”：表示根据MSISDN查询用户的MM上下文。<br>- “BYGUTI(指定GUTI)”：表示根据GUTI查询用户的MM上下文。<br>- “BYPTMSI(指定PTMSI)”：表示根据P-TMSI查询用户的MM上下文。<br>- “BYIMEI(指定IMEI)”：表示根据IMEI查询用户的MM上下文。<br>默认值：<br>“BYIMSI(指定IMSI)”<br>说明：- 针对开启一号多卡功能的用户，此命令不支持根据MSISDN直接查询用户移动上下文。如需根据MSISDN查询，可通过[**DSP IMSI**](显示指定MSISDN用户IMSI(DSP IMSI)_72345951.md)查询MSISDN对应的IMSI，再通过此命令根据IMSI查询对应的用户移动性管理上下文。<br>- 根据IMEI查询仅适用于无USIM卡的紧急呼叫用户。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYIMSI(指定IMSI)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定移动台国际ISDN号码。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYMSISDN(指定MSISDN)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |
| GUTI | GUTI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定GUTI号。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYGUTI(指定GUTI)”<br>后生效。<br>取值范围：19～20位16进制码字符串<br>默认值：无 |
| PTMSI | PTMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定P-TMSI号。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYPTMSI(指定PTMSI)”<br>后生效。<br>取值范围：1～10位16进制码字符串<br>默认值：无 |
| IMEI | ME标识 | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定用户设备的国际移动设备标识。<br>前提条件：此参数在<br>“查询方式”<br>设置为<br>“BYIMEI(指定IMEI)”<br>后生效。<br>取值范围：1～15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMCTXEXT]] · MM上下文扩展信息（MMCTXEXT）

## 使用实例

DSP MMCTXEXT: QUERYOPT=BYIMSI, IMSI="123031601000001";

```
%%DSP MMCTXEXT: QUERYOPT=BYIMSI, IMSI="123031601000001";%%
RETCODE = 0  操作成功。

结果如下
------------------
			      查询方式  =  指定IMSI
                                进程号  =  0
                                  IMSI  =  123031601000001
                                MSISDN  =  8613516000001
                                  GUTI  =  12303800116c3666c8c
                                ME标识  =  NULL
                                 PTMSI  =  NULL
                      PCRF签约FULLNAME  =  NULL
                     PCRF签约SHORTNAME  =  NULL
                                RU名称  =  USN_SP_RU_0064
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MM上下文扩展信息(DSP-MMCTXEXT)_09366008.md`
