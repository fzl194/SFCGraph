---
id: UDG@20.15.2@MMLCommand@SET MSSDEBUGSWITCH
type: MMLCommand
name: SET MSSDEBUGSWITCH（设置维测信息统计开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MSSDEBUGSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 维测开关统计查询
status: active
---

# SET MSSDEBUGSWITCH（设置维测信息统计开关）

## 功能

![](设置维测信息统计开关（SET MSSDEBUGSWITCH）_00441413.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置MSS维测统计信息开关。

## 注意事项

- 该命令执行后立即生效。
- 本功能使能会消耗内存、降低性能且在用户指定的时间之后会自动去使能，去使能之后内存释放、性能恢复。默认时间是30分钟。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| DEBUGSWITCH | 开关标记 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| DEBUGTYPE | 开关类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- schedule-work：Work精度维测开关。<br>- schedule-group：调度组精度开关。<br>- schedule-queue：调度队列维测开关。<br>- energy-conservation：绿色节能维测开关。<br>- oe-check：保序校验维测开关。<br>- oe-statistics：保序精度维测开关。<br>- timer-event：定时器事件维测开关。<br>- timer-statistics：定时器精度维测开关。<br>- schedule-trace：调度轨迹维测开关。<br>默认值：无 |
| TIME | 维测时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGSWITCH”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示维测状态持续时间，单位为秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～86400。<br>默认值：1800 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSDEBUGSWITCH]] · 维测信息统计开关（MSSDEBUGSWITCH）

## 使用实例

设置维测信息统计开关打开：

```
SET MSSDEBUGSWITCH:DEBUGSWITCH=TRUE,DEBUGTYPE=schedule-work,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置维测信息统计开关（SET-MSSDEBUGSWITCH）_00441413.md`
