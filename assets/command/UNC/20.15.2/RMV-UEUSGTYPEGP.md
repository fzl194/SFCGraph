---
id: UNC@20.15.2@MMLCommand@RMV UEUSGTYPEGP
type: MMLCommand
name: RMV UEUSGTYPEGP（删除UE USAGE TYPE群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UEUSGTYPEGP
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
- UE USAGE TYPE群组管理
status: active
---

# RMV UEUSGTYPEGP（删除UE USAGE TYPE群组）

## 功能

**适用网元：MME**

该命令用于删除UE USAGE TYPE群组记录。

## 注意事项

- 该命令执行后立即生效。
- 删除UE USAGE TYPE群组时必须保证相关表中不存在该UE USAGE TYPE群组的相关记录，可执行[**LST DNSN**](../../../GTP-C接口管理/DNS/DNS NAPTR管理/查询DNS NAPTR记录(LST DNSN)_26145892.md)查看相关记录。
- 删除UE USAGE TYPE群组时必须首先删除该UE USAGE TYPE群组下的所有成员，可执行[**RMV UEUSGTYPEGPMEM**](../UE USAGE TYPE群组成员管理/删除UE USAGE TYPE群组成员(RMV UEUSGTYPEGPMEM)_72345423.md)命令进行删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEUSGTYPEGP]] · UE USAGE TYPE群组（UEUSGTYPEGP）

## 使用实例

删除一个 “UEUSGTYPEGPID” 为 “0” 的UE USAGE TYPE群组：

RMV UEUSGTYPEGP: UEUSGTYPEGPID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UE-USAGE-TYPE群组(RMV-UEUSGTYPEGP)_72345421.md`
