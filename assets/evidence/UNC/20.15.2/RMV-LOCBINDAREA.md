# 删除UPF位置信息与该UPF优先支持的服务区的绑定关系（RMV LOCBINDAREA）

- [命令功能](#ZH-CN_MMLREF_0209652353__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652353__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652353__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652353__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652353)

**适用NF：SMF、SGW-C、GGSN、PGW-C**

该命令用于删除UPF位置信息与该UPF优先支持的服务区的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0209652353)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652353)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652353)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~150。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF优先支持的服务区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。该参数取值应与配置PNFSMFSERAREA中的SmfServingArea保持一致，可通过LST PNFSMFSERAREA命令查询。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPAREA中事先配置，可执行LST UPAREA进行查看。注意查询结果中“UPF服务区名称”须包含要绑定的“UPF服务区名称”。 |

## [使用实例](#ZH-CN_MMLREF_0209652353)

删除UPF位置区与该UPF优先支持的服务区名称的绑定关系，其中UPF位置区为“locality1”，覆盖区域名称为“area1”：

```
RMV LOCBINDAREA: LOCALITY="locality1",AREANAME="area1";
```
