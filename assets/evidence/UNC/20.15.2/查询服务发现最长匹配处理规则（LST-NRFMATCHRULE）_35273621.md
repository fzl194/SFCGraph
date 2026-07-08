# 查询服务发现最长匹配处理规则（LST NRFMATCHRULE）

- [命令功能](#ZH-CN_MMLREF_0000001135273621__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135273621__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135273621__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135273621__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135273621__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135273621)

**适用NF：NRF**

该命令用于查询服务发现最长匹配规则。

## [注意事项](#ZH-CN_MMLREF_0000001135273621)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135273621)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135273621)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF服务发现的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- SMF（SMF ）<br>- BSF（BSF）<br>- UDR（UDR）<br>- UDM（UDM）<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001135273621)

查询服务发现最长匹配规则。

```
LST NRFMATCHRULE:;
%%LST NRFMATCHRULE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
网元类型      匹配开关  

UDM           关闭      
AMF           关闭      
SMF           关闭      
AUSF          关闭      
PCF           关闭      
UDR           关闭      
BSF           关闭      
CHF           关闭      
CUSTOM_OCS    关闭      
SMSF          关闭      
NWDAF         关闭      
(结果个数 = 11)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135273621)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于表示NRF服务发现的目标网元类型。 |
| 匹配开关 | 该参数用于表示NRF服务发现时是否开启最长匹配功能。<br>开关设置为“FUNC_ON”时， 对于AMF/SMF/NWDAF而言，表示使用TAI匹配目标NF TAIRANGE，如果匹配出多个NF，选择最长匹配（匹配到的区间最小）的NF返回；<br>对于BSF而言，表示使用UeIpv4Address/UeIpv6Prefix匹配目标BSF Ipv4AddressRanges/Ipv6PrefixRanges，如果匹配出多个BSF，选择最长匹配（匹配到的区间最小）的BSF返回；<br>对于UDR/UDM/AUSF/PCF/CHF/CUSTOM_OCS/SMSF而言，表示NRF在号段匹配时会选择与请求方NF携带的号段匹配度最高的NF返回（即选择号段匹配最长的NF返回，号段可以匹配但非最长号段匹配的NF被认为不满足号段发现条件）；<br>开关设置为“FUNC_OFF”时，会返回所有匹配上的NF。 |
