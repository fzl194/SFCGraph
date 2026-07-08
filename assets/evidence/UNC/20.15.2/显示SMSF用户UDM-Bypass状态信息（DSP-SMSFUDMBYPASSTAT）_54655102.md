# 显示SMSF用户UDM Bypass状态信息（DSP SMSFUDMBYPASSTAT）

- [命令功能](#ZH-CN_MMLREF_0000001354655102__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001354655102__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001354655102__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001354655102__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001354655102__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001354655102)

**适用NF：SMSF**

该命令用于显示SMSF用户UDM Bypass状态信息。

## [注意事项](#ZH-CN_MMLREF_0000001354655102)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001354655102)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001354655102)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询SMSF用户UDM Bypass状态信息的方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：用户的SUPI信息<br>- “GPSI（GPSI）”：用户的GPSI信息<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYOPT"配置为"SUPI"时为条件可选参数。<br>参数含义：该参数用于指定用户的SUPI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYOPT"配置为"GPSI"时为条件可选参数。<br>参数含义：该参数用于指定用户的GPSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001354655102)

当运营商希望查询SMSF用户UDM Bypass状态信息，执行如下命令：

```
DSP SMSFUDMBYPASSTAT: QUERYOPT=SUPI, SUPI="460023500100001";
```

## [输出结果说明](#ZH-CN_MMLREF_0000001354655102)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询方式 | 该参数用于表示查询SMSF用户UDM Bypass状态信息的方式。<br>取值说明：<br>- “SUPI（SUPI）”：用户的SUPI信息<br>- “GPSI（GPSI）”：用户的GPSI信息 |
| SUPI | 该参数用于指定用户的SUPI信息。 |
| GPSI | 该参数用于指定用户的GPSI信息。 |
| UDM Bypass状态标记 | 该参数用于标识用户的UDM Bypass状态标记。<br>取值说明：<br>- “Bypass（Bypass）”：UDM处于Normal状态<br>- “Normal（Normal）”：UDM处于Bypass状态 |
| 进入UDM Bypass的时间 | 该参数用于表示用户进入UDM Bypass的时间。 |
