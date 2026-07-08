---
id: UNC@20.15.2@MMLCommand@RMV VLR
type: MMLCommand
name: RMV VLR（删除VLR配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VLR
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- VLR管理
status: active
---

# RMV VLR（删除VLR配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一个与本局 UNC 相连的VLR的信息。

## 注意事项

- 该命令执行后立即生效。
- 如果LAIVLR表[**ADD LAIVLR**](../LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)或SGSLNK表[**ADD SGSLNK**](../SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)中有此VLR相关数据，则不能删除此VLR的信息。
- 如果没有增加VLR信息，也不能在RAIVLR表、SGSLNK表和NRA中增加此VLR的相关信息。
- 当MSC POOL中有VLR处于迁移状态时，不允许删除此MSC POOL中的VLR配置。
- 如果删除的VLR属于MSC POOL，建议把此VLR对应的V值重新分配到此MSC POOL中其他的VLR上以便此MSC POOL中的VLR能覆盖0～999所有的V值。
- 若该VLR属于某一个MSC POOL，执行该命令会把该VLR从MSC POOL中删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数说明：该参数用于指定待删除的VLR号。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLR]] · VLR配置信息（VLR）

## 使用实例

删除VLR信息，VLR号为86139027：

```
RMV VLR: VN="86139027";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除VLR配置信息(RMV-VLR)_72345041.md`
