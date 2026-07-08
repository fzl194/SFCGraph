---
id: UNC@20.15.2@MMLCommand@RMV UEUSGTYPEGPMEM
type: MMLCommand
name: RMV UEUSGTYPEGPMEM（删除UE USAGE TYPE群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UEUSGTYPEGPMEM
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
- UE USAGE TYPE群组成员管理
status: active
---

# RMV UEUSGTYPEGPMEM（删除UE USAGE TYPE群组成员）

## 功能

**适用网元：MME**

该命令用于删除UE USAGE TYPE群组成员记录，删除后可能会导致专用核心网重选过程中DNS查询失败。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |
| BGNUEUSGTYPE | 起始UE USAGE TYPE | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE的起始值。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEUSGTYPEGPMEM]] · UE USAGE TYPE群组成员（UEUSGTYPEGPMEM）

## 使用实例

删除 “UE USAGE TYPE群组标识” 为 “1” ， “起始UE USAGE TYPE” 为 “100” 的UE USAGE TYPE群组成员：

RMV UEUSGTYPEGPMEM: UEUSGTYPEGPID=1, BGNUEUSGTYPE=100;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UE-USAGE-TYPE群组成员(RMV-UEUSGTYPEGPMEM)_72345423.md`
