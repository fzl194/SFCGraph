---
id: UNC@20.15.2@MMLCommand@RMV SCTPPARA
type: MMLCommand
name: RMV SCTPPARA（删除SCTP协议参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCTPPARA
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# RMV SCTPPARA（删除SCTP协议参数）

## 功能

**适用网元：SGSN、MME、AMF** 、 **SMSF**

该命令用于删除SCTP协议参数表中指定的记录。

## 注意事项

- 该命令执行后立即生效。
- 删除SCTP协议参数表中指定的记录前，请执行[**LST SCTPPARA**](查询SCTP协议参数(LST SCTPPARA)_72226019.md)命令查询该记录是否存在。若存在且执行本命令失败，再执行[**LST S1APLE**](../../S1接口管理/S1AP本地实体/查询S1AP本地实体(LST S1APLE)_72345855.md)命令，[**LST LCSAPLNK**](../../业务安全管理/LCS/LCSAP链路配置/查询LCSAP链路配置(LST LCSAPLNK)_26305618.md)命令，[**LST SBCAPLE**](../../SBc接口管理/SBCAP本地实体/查询SBCAP本地实体(LST SBCAPLE)_26146378.md)命令，[**LST SBCAPLNK**](../../SBc接口管理/SBc链路/查询SBc链路(LST SBCAPLNK)_26306186.md)命令，[**LST SGSLNK**](../../电路域联合业务/SGSAP/SGsAP链路管理/查询SGs链路(LST SGSLNK)_26305246.md)命令，[**LST DMLNK**](../Diameter管理/Diameter链路/查询Diameter链路配置(LST DMLNK)_26146276.md)命令，[**LST M3LNK**](../M3UA管理/M3UA链路/查询M3UA信令链路(LST M3LNK)_26146306.md)命令，[**LST SCTPLE**](../../S1接口管理/SCTP本地实体/查询SCTP本地实体(LST SCTPLE)_11295784.md)命令，[**LST RCAPLNK**](../注册中心管理/查询注册中心链路 (LST RCAPLNK)_45868734.md)命令，[**LST SGSRLNK**](../SMSF管理/SGS服务端链路/查询SGS服务端链路 (LST SGSRLNK)_97187029.md)命令，依次确认S1APLE数据表、LCSAPLNK数据表、SBCAPLE数据表、SBCAPLNK数据表、SGSLNK数据表、DMLNK数据表、M3LNK数据表、SCTPLE数据表、RCAPLNK数据表及SGSRLNK数据表中是否存在引用了此SCTP协议参数相关的记录，如果存在引用关系，则需要先删除该参数被引用的数据表中的相应记录后，再尝试删除该SCTP协议参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPPARAINDEX | SCTP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数用于删除指定SCTP协议参数索引，在系统范围内部唯一标识一条SCTP协议参数。<br>前提条件：此参数已经在<br>[**ADD SCTPPARA**](增加SCTP协议参数(ADD SCTPPARA)_26306150.md)<br>中设置。<br>取值范围：0~65534<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPPARA]] · SCTP协议参数（SCTPPARA）

## 使用实例

删除SCTP协议参数索引号为0的SCTP协议参数表中指定的记录：

RMV SCTPPARA:SCTPPARAINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCTP协议参数(RMV-SCTPPARA)_72345939.md`
