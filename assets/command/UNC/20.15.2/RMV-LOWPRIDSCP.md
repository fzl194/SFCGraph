---
id: UNC@20.15.2@MMLCommand@RMV LOWPRIDSCP
type: MMLCommand
name: RMV LOWPRIDSCP（删除低优先级业务DSCP）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOWPRIDSCP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 低优先级DSCP
status: active
---

# RMV LOWPRIDSCP（删除低优先级业务DSCP）

## 功能

![](删除低优先级业务DSCP(RMV LOWPRIDSCP)_72225191.assets/notice_3.0-zh-cn_2.png)

- 删除该命令后会使得对低优先级业务触发的寻呼进行的控制失效，导致寻呼数增加。
- 如果不输入任何参数，执行该命令会删除所有记录。

**适用网元：SGSN**

该命令用于删除低优先级业务和DSCP的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 删除该命令后会使得对低优先级业务触发的寻呼进行的控制失效，导致寻呼数增加。
- 如果不输入任何参数，执行该命令会删除所有记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSCP | DSCP | 可选必选说明：可选参数<br>参数含义：该参数用于指定待删除DSCP区间的DSCP，该DSCP属于待删除的DSCP区间。<br>取值范围：0~63<br>默认值：无<br>说明：该命令会删除指定的DSCP所在的DSCP区间。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOWPRIDSCP]] · 低优先级业务DSCP（LOWPRIDSCP）

## 使用实例

删除DSCP为10所在的DSCP区间:

RMV LOWPRIDSCP: DSCP=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LOWPRIDSCP.md`
