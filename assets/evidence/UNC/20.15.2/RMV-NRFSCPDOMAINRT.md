# 删除SCP Domain最长匹配后缀转发路由（RMV NRFSCPDOMAINRT）

- [命令功能](#ZH-CN_MMLREF_0000001183743802__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001183743802__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001183743802__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001183743802__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001183743802)

**适用NF：NRF**

该命令用于删除基于SCP Domain的最长匹配后缀转发路由。

## [注意事项](#ZH-CN_MMLREF_0000001183743802)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001183743802)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001183743802)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCPDOMAINSUFFIX | SCP Domain后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SCP Domain后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于SCP domain的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## [使用实例](#ZH-CN_MMLREF_0000001183743802)

删除一条SCP Domain后缀为32123ASDF，归属NRF组名称为azh0701的最长匹配后缀的转发路由配置，执行如下命令：

```
RMV NRFSCPDOMAINRT: SCPDOMAINSUFFIX="32123ASDF", NEXTNRFGRPNAME="azh0701";
```
