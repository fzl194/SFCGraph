---
id: UNC@20.15.2@MMLCommand@RMV S1APLE
type: MMLCommand
name: RMV S1APLE（删除S1AP本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1APLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP本地实体
status: active
---

# RMV S1APLE（删除S1AP本地实体）

## 功能

![](删除S1AP本地实体(RMV S1APLE)_26306066.assets/notice_3.0-zh-cn_2.png)

删除S1AP本地实体会导致和此本地实体相连的eNodeB上的用户业务中断。

**适用网元：MME**

该命令用于删除S1AP链路本地实体。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，会导致和此本地实体相连的eNodeB上的用户业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 链路本地实体号 | 可选必选说明：必选参数<br>参数含义：待删除的S1AP链路本地实体号。<br>取值范围：0～63<br>默认值：无<br>说明：可以通过<br>[**LST S1APLE**](查询S1AP本地实体(LST S1APLE)_72345855.md)<br>命令查看已有配置，确认所要删除的S1AP链路本地实体号。 |

## 操作的配置对象

- [S1AP本地实体（S1APLE）](configobject/UNC/20.15.2/S1APLE.md)

## 使用实例

删除链路本地实体号为0的S1AP链路：

RMV S1APLE: LLEINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1AP本地实体(RMV-S1APLE)_26306066.md`
