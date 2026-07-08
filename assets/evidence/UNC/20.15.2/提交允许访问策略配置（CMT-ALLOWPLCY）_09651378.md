# 提交允许访问策略配置（CMT ALLOWPLCY）

- [命令功能](#ZH-CN_MMLREF_0209651378__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651378__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651378__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651378__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651378)

![](提交允许访问策略配置（CMT ALLOWPLCY）_09651378.assets/notice_3.0-zh-cn_2.png)

该命令会将之前通过ADD ALLOWEDPLMNS/RMV ALLOWEDPLMNS/ADD ALLOWEDNSSAIS/RMV ALLOWEDNSSAIS/ADD ALLOWEDNFTYPES/RMV ALLOWEDNFTYPES/ADD ALLOWEDDOMAINS/RMV ALLOWEDDOMAINS配置的所有访问授权控制策略提交并生效。

**适用NF：NRF**

该命令用于提交配置的访问授权控制策略。

## [注意事项](#ZH-CN_MMLREF_0209651378)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0209651378)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651378)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMTTYPE | 提交类型 | 可选必选说明：可选参数<br>参数含义：该参数表示访问授权控制策略提交的范围。<br>数据来源：本端规划<br>取值范围：<br>- ALL（ALL）<br>默认值：ALL<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651378)

提交所有访问授权控制策略配置信息。

```
CMT ALLOWPLCY: CMTTYPE=ALL;
```
