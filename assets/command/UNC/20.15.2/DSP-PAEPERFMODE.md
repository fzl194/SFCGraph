---
id: UNC@20.15.2@MMLCommand@DSP PAEPERFMODE
type: MMLCommand
name: DSP PAEPERFMODE（显示PAE的性能模式）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPERFMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 性能模式
status: active
---

# DSP PAEPERFMODE（显示PAE的性能模式）

## 功能

该命令用于显示PAE的性能模式。

## 注意事项

深度隔离场景即启动参数/proc/cmdline里同时存在irqaffinity、nohz_full、rcu_nocbs、rcu_nocb_poll的场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD类型，可以通过使用命令<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPERFMODE]] · 配置表中的PAE性能模式（PAEPERFMODE）

## 使用实例

显示PAE的性能模式：

```
+++    UNC/*MEID:0 MENAME:unc*/        2024-06-13 20:40:42
O&M    #218
%%DSP PAEPERFMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
Pod类型      进程ID                 PAEDP性能模式  sdra的性能模式

comtest-pod  comtest-pod-0__103__0  低性能模式0    使用默认性能模式
sfpod        sfpod-0__103__0        低性能模式0    使用默认性能模式
vusn-pod     vusn-pod-0__103__0     低性能模式0    使用默认性能模式
vup-pod      vup-pod-0__103__0      低性能模式0    使用默认性能模式
lbpod        lbpod-0__103__0        低性能模式0    使用默认性能模式
(结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE的性能模式（DSP-PAEPERFMODE）_39408166.md`
