---
id: UNC@20.15.2@MMLCommand@RMV AUTOSCALINGOSPFPROCGRP
type: MMLCommand
name: RMV AUTOSCALINGOSPFPROCGRP（删除OSPF进程组自动化配置模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGOSPFPROCGRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- OSPF入不转板自动化配置
status: active
---

# RMV AUTOSCALINGOSPFPROCGRP（删除OSPF进程组自动化配置模板）

## 功能

该命令用于删除OSPF进程组自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 删除该模板时，要保证该模板添加过，且没有被引用。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | OSPF进程组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定OSPF进程组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16。<br>默认值：无 |
| VERSION | OSPF版本号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示自动化配置模板中OSPF版本号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OSPFv2：OSPFv2。<br>- OSPFv3：OSPFv3。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOSCALINGOSPFPROCGRP]] · OSPF进程组自动化配置模板（AUTOSCALINGOSPFPROCGRP）

## 使用实例

删除一个OSPF进程组ID为1的自动化配置模板：

```
RMV AUTOSCALINGOSPFPROCGRP:GROUPID=1,VERSION=OSPFv2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AUTOSCALINGOSPFPROCGRP.md`
