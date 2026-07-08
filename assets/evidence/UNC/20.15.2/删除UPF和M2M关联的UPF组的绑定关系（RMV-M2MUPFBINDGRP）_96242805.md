# 删除UPF和M2M关联的UPF组的绑定关系（RMV M2MUPFBINDGRP）

- [命令功能](#ZH-CN_MMLREF_0296242805__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242805__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242805__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242805__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296242805)

**适用NF：PGW-C、SMF**

该命令用于删除UPF和M2M关联的UPF组的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0296242805)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0296242805)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242805)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MUPGROUP命令配置生成。 |
| UPFID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0296242805)

删除UPF和UPF组的绑定关系, UPFID为upf_instance_1：

```
RMV M2MUPFBINDGRP: UPFGRPNAME="upfgrp1", UPFID="upf_instance_1";
```
