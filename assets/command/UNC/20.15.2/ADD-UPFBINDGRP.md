---
id: UNC@20.15.2@MMLCommand@ADD UPFBINDGRP
type: MMLCommand
name: ADD UPFBINDGRP（增加UPF和UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFBINDGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配UPF组管理
status: active
---

# ADD UPFBINDGRP（增加UPF和UPF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加UPF和UPF组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 当UPF组的地址规划类型是Local或DHCP类型时，一个UPF实例只能绑定一个UPF组，但一个UPF组可以绑定多个UPF实例。
- 当UPF组的地址规划类型是UDM或Radius类型时，一个UPF实例可以绑定多个UPF组，但一个UPF组最多绑定300个UPF实例。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRUPGROUP命令配置生成。 |
| UPFID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于标识绑定的UPF的优先级，只有当UPFGRPNAME对应的类型为UDM或RADIUS时参数才生效，数值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：255<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFBINDGRP]] · UPF和UPF组的绑定关系（UPFBINDGRP）

## 使用实例

添加UPF和UPF组的绑定关系，UPF组为upfgrp1，UPF为upf_instance_1：

```
ADD UPFBINDGRP: UPFGRPNAME="upfgrp1", UPFID="upf_instance_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UPFBINDGRP.md`
