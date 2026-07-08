# 增加NRF管理的ProxySMF（ADD NRFPROXYSMF）

- [命令功能](#ZH-CN_MMLREF_0000001823782730__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001823782730__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001823782730__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001823782730__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001823782730)

**适用NF：NRF**

该命令用于增加本NRF管理的ProxySMF，对于国际漫游业务，通过本命令配置的ProxySMF可以使NRF在服务发现流程中识别是否是ProxySMF。

## [注意事项](#ZH-CN_MMLREF_0000001823782730)

- 该命令执行后立即生效。

- 最多可输入128条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001823782730)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001823782730)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |
| NFNAME | NF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001823782730)

增加NRFPROXYSMF，NF实例标识为Nfinstanceid01，NF名称为ProxySMF01

```
ADD NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01", NFNAME="ProxySMF01";
```
