# 删除BSF实例与IPRANGE之间的绑定关系（RMV BSFIPRANGEBIND）

- [命令功能](#ZH-CN_MMLREF_0209652154__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652154__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652154__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652154__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652154)

**适用NF：SMF**

该命令用于删除BSF（Binding Support Function）所管辖的IP地址范围。

## [注意事项](#ZH-CN_MMLREF_0209652154)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652154)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652154)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |
| IPRANGENAME | IPRANGE名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该BSF实例所管辖的IP地址范围的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652154)

删除NF实例标识为BSF_Instance_0的BSF的rang1的IP地址管辖：

```
RMV BSFIPRANGEBIND: BSFINSTANCENAME="BSF_Instance_0", IPRANGENAME="range1";
```
