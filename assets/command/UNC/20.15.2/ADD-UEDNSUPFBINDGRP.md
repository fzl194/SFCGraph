---
id: UNC@20.15.2@MMLCommand@ADD UEDNSUPFBINDGRP
type: MMLCommand
name: ADD UEDNSUPFBINDGRP（增加UPF和DNS关联的UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UEDNSUPFBINDGRP
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
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- DNS关联的UPF组管理
status: active
---

# ADD UEDNSUPFBINDGRP（增加UPF和DNS关联的UPF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加UPF和DNS关联的UPF组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 一个UPF可以被绑定多个UPF组，但在实际配置中，建议一个UPF只绑定一个UPF组。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UEDNSUPGROUP命令配置生成。 |
| UPFID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEDNSUPFBINDGRP]] · UPF和DNS关联的UPF组的绑定关系（UEDNSUPFBINDGRP）

## 使用实例

添加UPF和UPF组的绑定关系，UPF组为upfgrp1，UPF为upf_instance_1：

```
ADD UEDNSUPFBINDGRP: UPFGRPNAME="upfgrp1", UPFID="upf_instance_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF和DNS关联的UPF组的绑定关系（ADD-UEDNSUPFBINDGRP）_73321230.md`
