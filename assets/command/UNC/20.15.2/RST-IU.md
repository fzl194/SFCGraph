---
id: UNC@20.15.2@MMLCommand@RST IU
type: MMLCommand
name: RST IU（复位Iu接口）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: IU
command_category: 动作类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口复位管理
status: active
---

# RST IU（复位Iu接口）

## 功能

![](复位Iu接口(RST IU)_26305848.assets/notice_3.0-zh-cn_2.png)

该命令会导致SGSN与相关RNC之间的业务中断，需慎重使用。

**适用网元：SGSN**

该命令用于对SGSN与指定RNC之间的Iu接口进行软件复位，复位将导致此Iu接口上所有已激活会话的丢失和Iu连接的释放。通常，SGSN在发生错误的情况下，会自动发送reset消息，如果怀疑SGP进程上的连接资源和SPP进程或RNC的连接资源相差太大的时候，才需要进行手工Iu接口复位。

## 注意事项

该命令会导致SGSN与相关RNC之间的业务中断，需慎重使用。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RNCNO | 内部RNC编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内部RNC编号。<br>取值范围：0~511<br>默认值：无<br>说明：RNC信息表的索引，相关数据可查询RNC信息表。查询RNC信息表请执行<br>[**LST RNC**](../Iu接口RNC信息/查询Iu接口RNC信息(LST RNC)_72345641.md)<br>命令。 |

## 操作的配置对象

- [复位Iu接口（IU）](configobject/UNC/20.15.2/IU.md)

## 使用实例

复位Iu接口，RNC索引为1：

RST IU: RNCNO=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位Iu接口(RST-IU)_26305848.md`
