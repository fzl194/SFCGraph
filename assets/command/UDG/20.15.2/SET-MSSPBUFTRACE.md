---
id: UDG@20.15.2@MMLCommand@SET MSSPBUFTRACE
type: MMLCommand
name: SET MSSPBUFTRACE（设置PBUF轨迹设置的开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MSSPBUFTRACE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# SET MSSPBUFTRACE（设置PBUF轨迹设置的开关）

## 功能

![](设置PBUF轨迹设置的开关（SET MSSPBUFTRACE）_85410312.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF轨迹开关，开启后会降低性能且在用户指定的时间之后会自动去使能，关闭后会恢复性能。默认时间是24小时。

此命令用于设置MSS的PBUF轨迹设置开关，轨迹功能用来记录该PBUF所经过的各种操作。

用户打开开关后，系统收集运行信息，导致转发面性能下降。打开开关后在用户指定的时间自动关闭，默认时间是24小时。

## 注意事项

- 该命令执行后立即生效。
- 本命令用于打开PBUF轨迹开关，开启后会降低性能且在用户指定的时间之后会自动关闭，关闭后会恢复性能。默认时间是24小时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组;

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| POOLNAME | 内存池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示内存池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSFMMSUMMARY](显示FMM的PBUF概要信息（DSP MSSFMMSUMMARY）_92520028.md)**<br>查看内存池名称。 |
| TRACESWITCH | 轨迹开关标记 | 可选必选说明：必选参数<br>参数含义：该参数用于表示轨迹开关标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| TIME | 轨迹开关持续时间（min） | 可选必选说明：条件可选参数<br>前提条件：该参数在“TRACESWITCH”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示本次规则设置的持续时间，单位为分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～43200。<br>默认值：1440 |

## 操作的配置对象

- [PBUF轨迹设置的开关（MSSPBUFTRACE）](configobject/UDG/20.15.2/MSSPBUFTRACE.md)

## 使用实例

打开微服务类型为104的微服务实例csdb-pod-0172-16-0-247__103__0内PBUF轨迹开关：

```
%%SET MSSPBUFTRACE: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-0-247__103__0", POOLNAME="PAE", TRACESWITCH=TRUE, TIME=1440;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PBUF轨迹设置的开关（SET-MSSPBUFTRACE）_85410312.md`
