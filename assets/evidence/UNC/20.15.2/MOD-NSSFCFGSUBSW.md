# 修改按签约NSSAI分配Configed NSSAI的PLMN级别开关（MOD NSSFCFGSUBSW）

- [命令功能](#ZH-CN_MMLREF_0000001098061326__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001098061326__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001098061326__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001098061326__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001098061326)

**适用NF：NSSF**

该命令用于修改按签约NSSAI生成configuredNssai信元的PLMN级别开关。

## [注意事项](#ZH-CN_MMLREF_0000001098061326)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001098061326)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001098061326)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| CFGWITHSUBSW | 按签约NSSAI分配configuredNssai开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NSSF在处理切片选择请求时，响应消息中configuredNssai信元是否直接使用UE签约NSSAI生成。开关打开，configuredNssai信元为UE签约NSSAI；开关关闭，configuredNssai信元为PLMN支持NSSAI和UE签约NSSAI的交集。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001098061326)

假如运营商希望修改一条移动国家码为248、移动网号为37、按签约NSSAI分配configuredNssai开关为关闭的记录，执行以下命令。

```
MOD NSSFCFGSUBSW: MCC="248", MNC="37", CFGWITHSUBSW=FUNC_ON;
```
