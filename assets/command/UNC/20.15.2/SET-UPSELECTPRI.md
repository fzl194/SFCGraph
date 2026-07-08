---
id: UNC@20.15.2@MMLCommand@SET UPSELECTPRI
type: MMLCommand
name: SET UPSELECTPRI（设置UPF选择策略次序）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPSELECTPRI
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择策略次序
status: active
---

# SET UPSELECTPRI（设置UPF选择策略次序）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置SMF选择UPF场景下的UPF选择策略次序。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FIRSTPRIORITY | SECONDPRIORITY | THIRDPRIORITY |
| --- | --- | --- |
| Combined | LocS11Priority | Load |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FIRSTPRIORITY | 第一优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于标识SMF选择UPF时的第一优先级。<br>数据来源：本端规划<br>取值范围：<br>- “Combined（合一的UPF）”：应用此优先级条件时，会优先选择主锚点与IUPF合一、辅锚点与UL CL/BP合一、SGW-U与PGW-U合一的UPF。<br>- “LocS11Priority（位置区或S11口优先级）”：应用此优先级条件时，优先选择位置区优先级高或者S11口优先级高的UPF。其中位置区优先级的配置需要与命令SET UPSELECTFLAG和命令ADD LOCBINDAREA配合使用；S11口的优先级配置需要与命令ADD UPBINDS11配合使用。其中当且仅当4G S1切换场景下，SGW-C未能从MME处获取用户位置信息时，该优先级条件标识为S11口优先级条件进行选择；其他场景下该优先级条件标识位置区优先级条件进行UPF选择。<br>- “Load（负载均衡策略）”：应用此优先条件时，会优先基于负载均衡策略选择UPF，依赖UPSELECTFLAG命令中LOADFLTFLAG开关，开关开启时该优选条件生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTPRI查询当前参数配置值。<br>配置原则：<br>第一优先级，第二优先级与第三优先级不能存在相同值。 |
| SECONDPRIORITY | 第二优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于标识SMF选择UPF时的第二优先级。<br>数据来源：本端规划<br>取值范围：<br>- “Combined（合一的UPF）”：应用此优先级条件时，会优先选择主锚点与IUPF合一、辅锚点与UL CL/BP合一、SGW-U与PGW-U合一的UPF。<br>- “LocS11Priority（位置区或S11口优先级）”：应用此优先级条件时，优先选择位置区优先级高或者S11口优先级高的UPF。其中位置区优先级的配置需要与命令SET UPSELECTFLAG和命令ADD LOCBINDAREA配合使用；S11口的优先级配置需要与命令ADD UPBINDS11配合使用。其中当且仅当4G S1切换场景下，SGW-C未能从MME处获取用户位置信息时，该优先级条件标识为S11口优先级条件进行选择；其他场景下该优先级条件标识位置区优先级条件进行UPF选择。<br>- “Load（负载均衡策略）”：应用此优先条件时，会优先基于负载均衡策略选择UPF，依赖UPSELECTFLAG命令中LOADFLTFLAG开关，开关开启时该优选条件生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTPRI查询当前参数配置值。<br>配置原则：<br>第一优先级，第二优先级与第三优先级不能存在相同值。 |
| THIRDPRIORITY | 第三优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于标识SMF选择UPF时的第三优先级。<br>数据来源：本端规划<br>取值范围：<br>- “Combined（合一的UPF）”：应用此优先级条件时，会优先选择主锚点与IUPF合一、辅锚点与UL CL/BP合一、SGW-U与PGW-U合一的UPF。<br>- “LocS11Priority（位置区或S11口优先级）”：应用此优先级条件时，优先选择位置区优先级高或者S11口优先级高的UPF。其中位置区优先级的配置需要与命令SET UPSELECTFLAG和命令ADD LOCBINDAREA配合使用；S11口的优先级配置需要与命令ADD UPBINDS11配合使用。其中当且仅当4G S1切换场景下，SGW-C未能从MME处获取用户位置信息时，该优先级条件标识为S11口优先级条件进行选择；其他场景下该优先级条件标识位置区优先级条件进行UPF选择。<br>- “Load（负载均衡策略）”：应用此优先条件时，会优先基于负载均衡策略选择UPF，依赖UPSELECTFLAG命令中LOADFLTFLAG开关，开关开启时该优选条件生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTPRI查询当前参数配置值。<br>配置原则：<br>第一优先级，第二优先级与第三优先级不能存在相同值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPSELECTPRI]] · UPF选择策略次序（UPSELECTPRI）

## 使用实例

设置SMF选择UPF场景下第一优先级条件为位置区或s11口优先级，第二优先级条件为合一的UPF，第三优先级为负载均衡策略：

```
SET UPSELECTPRI: FIRSTPRIORITY=LocS11Priority, SECONDPRIORITY=Combined,THIRDPRIORITY=Load;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-UPSELECTPRI.md`
