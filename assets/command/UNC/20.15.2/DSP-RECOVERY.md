---
id: UNC@20.15.2@MMLCommand@DSP RECOVERY
type: MMLCommand
name: DSP RECOVERY（显示本端重启次数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RECOVERY
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- Recovery管理
status: active
---

# DSP RECOVERY（显示本端重启次数）

## 功能

**适用网元：SGSN、MME、AMF**

该命令用于查询整系统中所有UPP进程内存中的本端Recovery值和所有LCP\SPP\UPP进程上CDB、DDB、内存中的本端Recovery值。本端Recovery值表示本端系统重启的次数。

## 注意事项

- 当用户输入的为简要信息时，显示的为整系统中所有UPP进程内存中的Recovery值。
- 当用户输入的为详细信息时，显示的为整系统中所有UPP/LCP/SPP进程上内存、DDB、CDB中的本端Recovery值。
- 当命令**[SET AMFN26PLCY](../../../../../接口管理/GTP-C接口配置管理/N26接口管理/N26策略管理/设置AMF N26接口策略（SET AMFN26PLCY）_62817114.md)**的参数“N26ITFMODE”取值为“COMBINE”时，该命令适用于SGSN、MME、AMF，否则，该命令仅适用于SGSN、MME。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选。<br>参数含义：该参数用于指定查询的是简要信息还是详细信息。其中简要信息查询的为整系统中所有UPP进程内存中的Recovery值，详细信息查询的为整系统中所有LCP/UPP/SPP进程内存、DDB表和CDB表中的Recovery值。<br>数据来源：本端规划。<br>取值范围：枚举类型<br>- “BRIEF（简要信息）”<br>- “DETAILS(详细信息)”<br>默认值：<br>“BRIEF（简要信息）” |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：SERVICETYPE需要填写LINK_VNFC或者USN_VNFC的名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RECOVERY]] · 本端重启次数（RECOVERY）

## 使用实例

1. 查询本端recovery简略信息：
  DSP RECOVERY: QUERYTYPE=BRIEF,SERVICETYPE="USN_VNFC";
  ```
  %%DSP RECOVERY: QUERYTYPE=BRIEF,
  SERVICETYPE="USN_VNFC"
  ;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------------------
  RU名称              进程类型        进程号      是否绑定GTP-C地址             进程内存中的Recovery值

  USN_SP_RU_0065      UPP             0           是                            2
  USN_SP_RU_0064      UPP             0           否                            2
  (结果个数 = 2)
  ---    END
  ```
2. 查询本端recovery详细信息：
  DSP RECOVERY: QUERYTYPE=DETAILS,SERVICETYPE="USN_VNFC";
  ```
  %%DSP RECOVERY: QUERYTYPE=DETAILS,
  SERVICETYPE="USN_VNFC"
  ;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
  RU名称             进程类型        进程号       是否绑定GTP-C地址           进程内存中的Recovery值       DDB表中的Recovery值    CDB表中的Recovery值

  USN_SP_RU_0065     LCP             0            否                          2                            2                      2
  USN_SP_RU_0064     LCP             0            否                          2                            2                      2
  USN_SP_RU_0064     SPP             4            否                          2                            2                      2
  USN_SP_RU_0064     SPP             3            否                          2                            2                      2
  USN_SP_RU_0065     SPP             2            否                          2                            2                      2
  USN_SP_RU_0064     SPP             1            否                          2                            2                      2
  USN_SP_RU_0065     SPP             4            否                          2                            2                      2
  USN_SP_RU_0064     SPP             2            否                          2                            2                      2
  USN_SP_RU_0065     SPP             1            否                          2                            2                      2
  USN_SP_RU_0064     SPP             0            否                          2                            2                      2
  USN_SP_RU_0064     UPP             0            否                          2                            2                      2
  USN_SP_RU_0065     UPP             0            是                          2                            2                      2
  USN_SP_RU_0065     SPP             3            否                          2                            2                      2
  USN_SP_RU_0065     SPP             0            否                          2                            2                      2    
  (结果个数 = 14)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RECOVERY.md`
