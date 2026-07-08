---
id: UNC@20.15.2@MMLCommand@SET GLBDFTCHFGROUP
type: MMLCommand
name: SET GLBDFTCHFGROUP（设置全局默认CHF组）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBDFTCHFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# SET GLBDFTCHFGROUP（设置全局默认CHF组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置系统缺省的CHF组。

## 注意事项

- 该命令执行后立即生效。

- 该命令参数输入空格或者null（不区分大小写）清空参数值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PRIMARYCHFGRP | SECONDARYCHFGRP |
| --- | --- |
| null | null |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRIMARYCHFGRP | 主CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主CHF组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBDFTCHFGROUP查询当前参数配置值。<br>配置原则：<br>该参数使用<br>[**ADD TNFGRP**](../../../../接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)<br>命令配置生成。 |
| SECONDARYCHFGRP | 备CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备CHF组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBDFTCHFGROUP查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [全局默认CHF组（GLBDFTCHFGROUP）](configobject/UNC/20.15.2/GLBDFTCHFGROUP.md)

## 使用实例

配置系统缺省的chf组主为“CHF1”，备为“CHF2”：

```
SET GLBDFTCHFGROUP: PRIMARYCHFGRP="CHF1", SECONDARYCHFGRP="CHF2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置全局默认CHF组（SET-GLBDFTCHFGROUP）_09651523.md`
