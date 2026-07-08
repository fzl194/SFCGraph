---
id: UNC@20.15.2@MMLCommand@SET MSSDEBUGSWITCHM
type: MMLCommand
name: SET MSSDEBUGSWITCHM（设置维测信息统计开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSSDEBUGSWITCHM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# SET MSSDEBUGSWITCHM（设置维测信息统计开关）

## 功能

![](设置维测信息统计开关（SET MSSDEBUGSWITCHM）_93243682.assets/notice_3.0-zh-cn_2.png)

本功能使能会消耗内存、降低性能且在用户指定的时间之后会自动去使能，去使能之后内存释放、性能恢复。默认时间是30分钟。

该命令用于设置MSS维测统计信息开关。

## 注意事项

- 该命令执行后立即生效。
- 本功能使能会消耗内存、降低性能且在用户指定的时间之后会自动去使能，去使能之后内存释放、性能恢复。默认时间是30分钟。
- 当前版本DEBUGTYPE参数只支持schedule-work、energy-conservation开关配置生效，其余开关配置不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| DEBUGSWITCH | 开关标记 | 可选必选说明：必选参数<br>参数含义：该参数用于表示维测开关标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| DEBUGTYPE | 开关类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- schedule-work：Work精度维测开关。<br>- schedule-group：调度组精度开关。<br>- schedule-queue：调度队列维测开关。<br>- energy-conservation：绿色节能维测开关。<br>- oe-check：保序校验维测开关。<br>- oe-statistics：保序精度维测开关。<br>- timer-event：定时器事件维测开关。<br>- timer-statistics：定时器精度维测开关。<br>- schedule-trace：调度轨迹维测开关。<br>默认值：无 |
| TIME | 维测时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示维测状态持续时间。<br>数据来源：本端规划<br>取值范围：1~86400<br>默认值：1800 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSDEBUGSWITCHM]] · 维测信息统计开关（MSSDEBUGSWITCHM）

## 使用实例

设置微服务类型为aa的微服务实例bb的维测信息统计开关打开：

```
SET MSSDEBUGSWITCHM:DEBUGSWITCH=TRUE,DEBUGTYPE=schedule-work,CELLTYPE="aa", CELLINSTANCE="bb";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MSSDEBUGSWITCHM.md`
