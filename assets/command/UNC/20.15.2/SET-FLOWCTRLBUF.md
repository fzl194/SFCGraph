---
id: UNC@20.15.2@MMLCommand@SET FLOWCTRLBUF
type: MMLCommand
name: SET FLOWCTRLBUF（设置流量控制缓存配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FLOWCTRLBUF
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- BSSGP参数
status: active
---

# SET FLOWCTRLBUF（设置流量控制缓存配置）

## 功能

**适用网元：SGSN**

该命令用于修改BSSGP流控缓存参数配置。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令需要华为技术支持人员指导下才能执行，请慎重使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSSIGQL | MS信令队列最大长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置MS信令队列最大长度，表示MS信令队列的最大节点数。<br>数据来源：整网规划<br>取值范围：1～32<br>系统初始设置值：32 |
| MSDATQL | MS数据队列最大长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置MS数据队列最大长度，表示MS数据队列的最大节点数。<br>数据来源：整网规划<br>取值范围：1～512<br>系统初始设置值：512 |
| MSCONTHD | MS拥塞门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置MS拥塞门限。<br>数据来源：整网规划<br>取值范围：1～100<br>系统初始设置值：80<br>配置原则：该参数的取值一定要大于<br>“MSCONRTHD”<br>。 |
| MSCONRTHD | MS拥塞恢复门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置MS拥塞恢复门限。<br>数据来源：整网规划<br>取值范围：0～99<br>系统初始设置值：60<br>配置原则：该参数的取值一定要小于<br>“MSCONTHD”<br>。 |
| BVCSIGQL | BVC信令队列最大长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置BVC信令队列最大长度，表示BVC信令队列的最大节点数。<br>数据来源：整网规划<br>取值范围：1～384<br>系统初始设置值：384 |
| BVCDATQL | BVC数据队列最大长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置BVC数据队列最大长度，表示BVC数据队列的最大节点数。<br>数据来源：整网规划<br>取值范围：1～1536<br>系统初始设置值：1536 |
| BVCCONTHD | BVC拥塞门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置BVC拥塞门限。<br>数据来源：整网规划<br>取值范围：1～100<br>系统初始设置值：80<br>配置原则：该参数的取值一定要大于<br>“BVCCONRTHD”<br>。 |
| BVCCONRTHD | BVC拥塞恢复门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于设置BVC拥塞恢复门限。<br>数据来源：整网规划<br>取值范围：0～99<br>系统初始设置值：60<br>配置原则：该参数的取值一定要小于<br>“BVCCONTHD”<br>。 |

## 操作的配置对象

- [流量控制缓存配置（FLOWCTRLBUF）](configobject/UNC/20.15.2/FLOWCTRLBUF.md)

## 使用实例

修改BSSGP流控缓存配置：

SET FLOWCTRLBUF: MSSIGQL=16, MSDATQL=100, MSCONTHD=60, MSCONRTHD=50, BVCSIGQL=200, BVCDATQL=500, BVCCONTHD=60, BVCCONRTHD=50;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置流量控制缓存配置(SET-FLOWCTRLBUF)_72225667.md`
