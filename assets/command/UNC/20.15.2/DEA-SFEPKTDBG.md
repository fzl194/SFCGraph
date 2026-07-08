---
id: UNC@20.15.2@MMLCommand@DEA SFEPKTDBG
type: MMLCommand
name: DEA SFEPKTDBG（去激活报文调测过滤）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: SFEPKTDBG
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 软转发报文调测
status: active
---

# DEA SFEPKTDBG（去激活报文调测过滤）

## 功能

该命令用来去除报文调测过滤配置及去激活调测功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～60。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEPKTDBG]] · 报文调测过滤（SFEPKTDBG）

## 使用实例

去激活资源单元名称为“VNODE_VNRS_VNFC_IPU_0064”的所有配置信息：

```
DEA SFEPKTDBG: RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活报文调测过滤（DEA-SFEPKTDBG）_00841097.md`
