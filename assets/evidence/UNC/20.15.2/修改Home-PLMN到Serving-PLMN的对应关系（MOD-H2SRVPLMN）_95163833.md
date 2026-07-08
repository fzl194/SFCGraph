# 修改Home PLMN到Serving PLMN的对应关系（MOD H2SRVPLMN）

- [命令功能](#ZH-CN_MMLREF_0000001295163833__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001295163833__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001295163833__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001295163833__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001295163833)

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF**

改命令用于修改Home PLMN到Serving PLMN的对应关系。

## [注意事项](#ZH-CN_MMLREF_0000001295163833)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001295163833)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001295163833)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HMCC | Home PLMN移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>- 只允许配置十进制数字（0-9）。<br>- 该参数通过ADD NGHPLMN的MCC进行配置。 |
| HMNC | Home PLMN移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>- 只允许配置十进制数字（0-9）。<br>- 该参数通过ADD NGHPLMN的MNC进行配置。 |
| SRVPLMNIDX | Serving PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN关联的Serving PLMN Index。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数通过ADD NGSRVPLMN的PLMNIDX进行配置。 |

## [使用实例](#ZH-CN_MMLREF_0000001295163833)

将Home PLMN （12303）关联的Serving PLMN索引修改为2，执行如下命令：

```
MOD H2SRVPLMN: HMCC="123", HMNC="03", SRVPLMNIDX=2;
```
