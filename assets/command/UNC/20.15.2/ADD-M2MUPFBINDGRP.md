---
id: UNC@20.15.2@MMLCommand@ADD M2MUPFBINDGRP
type: MMLCommand
name: ADD M2MUPFBINDGRP（增加UPF和M2M关联的UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: M2MUPFBINDGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M关联的UPF组管理
status: active
---

# ADD M2MUPFBINDGRP（增加UPF和M2M关联的UPF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于添加UPF和M2M关联的UPF组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MUPGROUP命令配置生成。 |
| UPFID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MUPFBINDGRP]] · UPF和M2M关联的UPF组的绑定关系（M2MUPFBINDGRP）

## 使用实例

添加UPF和UPF组的绑定关系，UPF组为upfgrp1，UPF为upf_instance_1：

```
ADD M2MUPFBINDGRP: UPFGRPNAME="upfgrp1", UPFID="upf_instance_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-M2MUPFBINDGRP.md`
