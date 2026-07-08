---
id: UNC@20.15.2@MMLCommand@RMV SCCPDPCSHR
type: MMLCommand
name: RMV SCCPDPCSHR（删除DPC多点负荷分担记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCCPDPCSHR
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP目的信令点多点负荷分担
status: active
---

# RMV SCCPDPCSHR（删除DPC多点负荷分担记录）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP目的信令点多点负荷分担记录。

## 注意事项

- 此命令执行后立即生效。
- 执行该命令会中断该主SCCP目的信令点的多点负荷分担功能，会影响已有业务，删除之后，有可能会选到其他的DPC。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAINDPX | 主DPC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定主SCCP目的信令点索引。<br>取值范围：0～1279<br>默认值：无<br>说明：此目的信令点索引记录必须在SCCP目的信令点表中存在。SCCP目的信令点表的相关信息请参考<br>[**ADD SCCPDPC**](../SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md)<br>命令。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPDPCSHR]] · DPC多点负荷分担记录（SCCPDPCSHR）

## 使用实例

删除主SCCP目的信令点索引为1的多点负荷分担记录：

RMV SCCPDPCSHR: MAINDPX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DPC多点负荷分担记录(RMV-SCCPDPCSHR)_72345923.md`
