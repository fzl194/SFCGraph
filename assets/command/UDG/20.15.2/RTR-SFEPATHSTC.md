---
id: UDG@20.15.2@MMLCommand@RTR SFEPATHSTC
type: MMLCommand
name: RTR SFEPATHSTC（清除FEI Path统计）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: SFEPATHSTC
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI消息统计
status: active
---

# RTR SFEPATHSTC（清除FEI Path统计）

## 功能

该命令用来清除FEI Path统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：指定系统中有效的资源单元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| PATHID | Path ID | 可选必选说明：必选参数<br>参数含义：指定Path的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [FEI Path统计（SFEPATHSTC）](configobject/UDG/20.15.2/SFEPATHSTC.md)

## 使用实例

清除FEI Path统计：

```
RTR SFEPATHSTC:RUNAME="VNODE_VNRS_VNFC_IPU_0065",PATHID=88;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除FEI-Path统计（RTR-SFEPATHSTC）_00866129.md`
