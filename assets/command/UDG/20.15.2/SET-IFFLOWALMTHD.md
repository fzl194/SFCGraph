---
id: UDG@20.15.2@MMLCommand@SET IFFLOWALMTHD
type: MMLCommand
name: SET IFFLOWALMTHD（设置接口带宽利用率告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IFFLOWALMTHD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口带宽利用率告警阈值
status: active
---

# SET IFFLOWALMTHD（设置接口带宽利用率告警阈值）

## 功能

该命令用于设置接口带宽利用率告警阈值。

带宽利用率=（接口流量速率/接口带宽）*100，若超过阈值，则产生告警。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| INRISINGRATE | INRESUMERATE | OUTRISINGRATE | OUTRESUMERATE |
| --- | --- | --- | --- |
| 100 | 100 | 100 | 100 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定带宽利用率告警阈值的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| INRISINGRATE | 入向带宽利用率告警产生阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定入方向产生告警带宽利用率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。入方向带宽利用率告警产生阈值需大于等于入方向告警恢复阈值。<br>默认值：无 |
| INRESUMERATE | 入向带宽利用率告警恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定入方向恢复告警带宽利用率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。入方向告警恢复带宽利用率阈值需小于等于入方向带宽利用率告警产生阈值。<br>默认值：无 |
| OUTRISINGRATE | 出向带宽利用率告警产生阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定出方向产生告警带宽利用率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。出方向带宽利用率告警产生阈值需大于等于出方向告警恢复带宽利用率阈值。<br>默认值：无 |
| OUTRESUMERATE | 出向带宽利用率告警恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定出方向恢复告警带宽利用率阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。出方向告警恢复带宽利用率阈值需小于等于出方向带宽利用率告警产生阈值。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFFLOWALMTHD]] · 接口带宽利用率告警阈值（IFFLOWALMTHD）

## 使用实例

设置接口带宽利用率阈值：

```
SET IFFLOWALMTHD:IFNAME="ethernet64/0/3",INRISINGRATE=100,INRESUMERATE=100,OUTRISINGRATE=50,OUTRESUMERATE=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IFFLOWALMTHD.md`
