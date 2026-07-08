---
id: UNC@20.15.2@MMLCommand@RMV SGSLNK
type: MMLCommand
name: RMV SGSLNK（删除SGs链路）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGSLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路管理
status: active
---

# RMV SGSLNK（删除SGs链路）

## 功能

![](删除SGs链路(RMV SGSLNK)_26145430.assets/notice_3.0-zh-cn_2.png)

与这个SGSLNK相关的SGs链路将会被删除。

**适用网元：MME**

此命令用于删除指定的SGs链路配置。

## 注意事项

- 此命令执行后立即生效。
- 此命令的执行会导致此链路中断，当到对应MSC/VLR下的所有链路都删除后将会导致到此MSC/VLR的业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：必选参数<br>参数含义：待删除链路的索引。<br>取值范围：0~511<br>默认值：无<br>说明：可以通过<br>[**LST SGSLNK**](查询SGs链路(LST SGSLNK)_26305246.md)<br>命令查看已有的SGs链路配置，确认待删除SGs链路的索引号。 |

## 操作的配置对象

- [SGs链路（SGSLNK）](configobject/UNC/20.15.2/SGSLNK.md)

## 使用实例

删除链路索引为1的SGs链路配置：

RMV SGSLNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGs链路(RMV-SGSLNK)_26145430.md`
