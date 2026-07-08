# 增加DNAI信息（ADD DNAIINFO）

- [命令功能](#ZH-CN_MMLREF_0000001210605246__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001210605246__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001210605246__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001210605246__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001210605246)

**适用NF：SMF、PGW-C**

该命令用于增加DNAI信息。

## [注意事项](#ZH-CN_MMLREF_0000001210605246)

- 该命令执行后立即生效。

- 最多可输入10000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001210605246)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001210605246)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SHUNTDIRECT | 分流方向 | 可选必选说明：可选参数<br>参数含义：该参数用于控制分流的方向。<br>数据来源：全网规划<br>取值范围：<br>- “NORMAL（正向）”：正向分流<br>- “REVERSE（反向）”：反向分流<br>默认值：NORMAL<br>配置原则：<br>该参数配置为正向分流，园区业务分流到辅锚点；<br>该参数配置为反向分流，园区业务分流到主锚点。 |
| SHUNTLOC | 分流位置 | 可选必选说明：可选参数<br>参数含义：该参数用于指示DNAI的分流位置。<br>数据来源：全网规划<br>取值范围：<br>- “HOME（归属地）”：归属地分流<br>默认值：HOME<br>配置原则：<br>该参数对I-SMF不生效。 |
| ALWAYSSHUNTSW | Always分流开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制DNAI是否支持Always分流。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不支持Always分流<br>- “ENABLE（使能）”：支持Always分流<br>默认值：DISABLE<br>配置原则：<br>开关默认关闭，DNAI不支持Always分流；<br>当DNAI规划为整网范围内生效时，需打开Always分流开关。 |

## [使用实例](#ZH-CN_MMLREF_0000001210605246)

增加cmnet_dnai的分流方向为正向分流，分流位置为归属地分流，关闭Always分流开关

```
ADD DNAIINFO: DNAI="cmnet_dnai", SHUNTDIRECT=NORMAL, SHUNTLOC=HOME, ALWAYSSHUNTSW=DISABLE;
```
