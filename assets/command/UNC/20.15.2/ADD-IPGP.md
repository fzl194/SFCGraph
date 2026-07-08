---
id: UNC@20.15.2@MMLCommand@ADD IPGP
type: MMLCommand
name: ADD IPGP（增加IP群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPGP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 255
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- IP群组管理
- IP群组配置
status: active
---

# ADD IPGP（增加IP群组）

## 功能

**适用网元：SGSN、MME**

该命令用于增加IP群组记录。IP群组用于定义某种特定功能的设备群组，以该设备群组为粒度进行业务策略控制。需要结合 **[ADD IPV4GPMEM](../IP群组成员配置/增加IPv4群组成员(ADD IPV4GPMEM)_72225397.md)** 或 **[ADD IPV6GPMEM](../IP群组成员配置/增加IPv6群组成员(ADD IPV6GPMEM)_26145720.md)** 命令为IP群组添加成员。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为255。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPGPID | IP群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP群组标识。<br>数据来源：本端规划<br>取值范围：1-255<br>默认值：无 |
| NAME | 群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP群组名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPGP]] · IP群组（IPGP）

## 使用实例

为支持DCNR的S-GW配置IP群组：

ADD IPGP: IPGPID=1,NAME="DCNR_SGW";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IPGP.md`
