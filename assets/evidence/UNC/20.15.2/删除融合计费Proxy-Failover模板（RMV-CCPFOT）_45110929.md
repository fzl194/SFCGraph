# 删除融合计费Proxy Failover模板（RMV CCPFOT）

- [命令功能](#ZH-CN_MMLREF_0245110929__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245110929__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245110929__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245110929__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0245110929)

![](删除融合计费Proxy Failover模板（RMV CCPFOT）_45110929.assets/notice_3.0-zh-cn_2.png)

该命令用于删除融合计费模板标识。若删除可能导致NCG代应答时不携带默认流量或处理相应异常返回码时不按预期规则向OCS进行重新发现或不按预期向SMF代应答。

**适用NF：NCG**

该命令用于删除融合计费Proxy Failover模板。

## [注意事项](#ZH-CN_MMLREF_0245110929)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0245110929)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0245110929)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FOTNM | Failover模板标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245110929)

删除Failover模板标识名称为“ccpfot1”的融合计费Proxy Failover模板：

```
RMV CCPFOT: FOTNM="ccpfot1";
```
