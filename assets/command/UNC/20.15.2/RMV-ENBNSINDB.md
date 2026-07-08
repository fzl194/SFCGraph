---
id: UNC@20.15.2@MMLCommand@RMV ENBNSINDB
type: MMLCommand
name: RMV ENBNSINDB（删除配置的eNodeB邻接关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ENBNSINDB
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
- eNodeB邻接关系测试
status: active
---

# RMV ENBNSINDB（删除配置的eNodeB邻接关系）

## 功能

**适用网元：MME**

此命令用于删除手动添加的eNodeB邻接关系。

## 注意事项

此命令执行后立即生效，并将导致整网所有eNodeB邻接关系的学习时间变长。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：待删除邻接关系的中心eNodeB的类型。<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”：表示中心eNodeB类型为家庭基站，其标志长度为28位。<br>- “MACRO_ENODEB(Macro_eNodeB)”：表示中心eNodeB类型为宏基站，其标识长度为20位。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待删除邻接关系的中心eNodeB和邻接eNodeB共用的移动国家码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待删除邻接关系的中心eNodeB和邻接eNodeB共用的移动网号。<br>取值范围：2～3位十进制数字<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：待删除邻接关系的中心eNodeB的ID。<br>取值范围：0～268435455<br>默认值：无 |

## 操作的配置对象

- [配置的eNodeB邻接关系（ENBNSINDB）](configobject/UNC/20.15.2/ENBNSINDB.md)

## 使用实例

删除一条手动添加的eNodeB邻接关系，其中心eNodeB的 “eNodeB类型” 为 “HOME_ENODEB(Home_eNodeB)” ， “移动国家码” 为 “123” ， “移动网号” 为 “01” ， “eNodeB标识” 为 “327697” ：

RMV ENBNSINDB: ENBTYPE=HOME_ENODEB, MCC="123", MNC="01", ENBID=327697;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除配置的eNodeB邻接关系(RMV-ENBNSINDB)_26146260.md`
