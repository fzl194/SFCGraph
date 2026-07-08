---
id: UNC@20.15.2@MMLCommand@RMV DCN
type: MMLCommand
name: RMV DCN（删除DCN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DCN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN配置
status: active
---

# RMV DCN（删除DCN）

## 功能

**适用网元：MME**

此命令用于删除一条DCN记录。例如运营商为合理规划网络，将原有DCN划分删除，删除后将不能通过UE USAGE TYPE映射到此DCN。

## 注意事项

该命令执行后立即生效。

执行该命令前需要删除同一“DCN ID”下的DCN映射关系和DCN成员，请执行 [**LST DCNMAP**](../DCN映射关系/查询DCN映射关系(LST DCNMAP)_26145830.md) 和 [**LST DCNMEMBER**](../DCN成员管理/查询DCN成员(LST DCNMEMBER)_26145832.md) 查询记录是否存在。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DCN标识。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DCN]] · DCN（DCN）

## 使用实例

MCC为123，MNC为01的运营商为合理规划网络，将eMtc用户所属DCN ID为0的网络删除：

RMV DCN: DCNID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DCN.md`
