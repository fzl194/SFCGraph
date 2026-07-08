# 查询UE重载控制策略（LST UEOVERLDCTRL）

- [命令功能](#ZH-CN_MMLREF_0000002126826613__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002126826613__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002126826613__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002126826613__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002126826613__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002126826613)

**适用NF：AMF**

该命令用于查询指定用户（群）的重载控制策略参数。

## [注意事项](#ZH-CN_MMLREF_0000002126826613)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000002126826613)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002126826613)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF上配置重载控制策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户群，策略匹配的优先级从高到低依次为：“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用重载控制策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000002126826613)

- 查询系统内当前配置的重载控制策略：
  ```
  %%LST UEOVERLDCTRL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    用户范围  =  所有用户
    IMSI前缀  =  NULL
  MPSMCS开关  =  开启
  (结果个数 = 1)

  ---    END
  ```
- 查询系统内当前配置“用户范围”为“IMSI前缀”且IMSI前缀为“123456”的重载控制策略：
  ```
  %%LST NGPEIPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    用户范围  =  指定IMSI前缀
    IMSI前缀  =  123456
  MPSMCS开关  =  关闭
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000002126826613)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户范围 | 该参数用于表示AMF上配置重载控制策略的用户范围。 |
| IMSI前缀 | 该参数用于指定应用重载控制策略的用户的IMSI前缀。 |
| MPSMCS开关 | 该参数用于配置AMF是否支持MPS/MCS功能。功能开关开启后，如果用户没有匹配的ADD NGMMSUBDATA配置，或者匹配的ADD NGMMSUBDATA配置中“MPSMCS优先级（MPSMCSPRI）”取值为“SUB_FIRST(签约优先)”且签约的MPS/MCS有效时，AMF将UDM签约的MPS/MCS能力下发给UE，否则将本地配置(使用ADD NGMMSUBDATA命令配置)的MPS/MCS下发给UE。 |
