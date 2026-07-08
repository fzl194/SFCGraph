---
id: UNC@20.15.2@MMLCommand@STR VERIFICATION
type: MMLCommand
name: STR VERIFICATION（启动一次FEI与FES之间的对账操作）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: VERIFICATION
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 转发对账平滑
status: active
---

# STR VERIFICATION（启动一次FEI与FES之间的对账操作）

## 功能

通过手动启动对账命令行操作，可以实现表项的平滑与老化操作，使FEI与FES之前表项保持一致。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VERIFICATION]] · 一次FEI与FES之间的对账操作（VERIFICATION）

## 使用实例

对所有转发表进行对账操作：

```
STR VERIFICATION:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动一次FEI与FES之间的对账操作（STR-VERIFICATION）_00840905.md`
