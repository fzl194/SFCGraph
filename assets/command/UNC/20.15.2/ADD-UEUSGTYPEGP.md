---
id: UNC@20.15.2@MMLCommand@ADD UEUSGTYPEGP
type: MMLCommand
name: ADD UEUSGTYPEGP（增加UE USAGE TYPE群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UEUSGTYPEGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- UE USAGE TYPE群组管理
status: active
---

# ADD UEUSGTYPEGP（增加UE USAGE TYPE群组）

## 功能

**适用网元：MME**

该命令增加一条UE USAGE TYPE群组记录，用于在 [**ADD DNSN**](../../../GTP-C接口管理/DNS/DNS NAPTR管理/增加DNS NAPTR记录(ADD DNSN)_72225569.md) 中辅助进行DNS查询。需要结合 [**ADD UEUSGTYPEGPMEM**](../UE USAGE TYPE群组成员管理/增加UE USAGE TYPE群组成员(ADD UEUSGTYPEGPMEM)_26305632.md) 命令为UE USAGE TYPE群组添加成员。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>配置原则：<br>“UE USAGE TYPE群组标识”<br>在本MME内唯一。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组的描述信息。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：noname |

## 操作的配置对象

- [UE USAGE TYPE群组（UEUSGTYPEGP）](configobject/UNC/20.15.2/UEUSGTYPEGP.md)

## 使用实例

运营商规划网络，增加一个 “UE USAGE TYPE群组标识” 为 “1” ，群组名称为 “eMtc” 的UE USAGE TYPE群组：

ADD UEUSGTYPEGP: UEUSGTYPEGPID=1, DESC="eMtc";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UE-USAGE-TYPE群组(ADD-UEUSGTYPEGP)_72225499.md`
