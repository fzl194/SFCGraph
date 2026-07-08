---
id: UNC@20.15.2@MMLCommand@MOD UEUSGTYPEGP
type: MMLCommand
name: MOD UEUSGTYPEGP（修改UE USAGE TYPE群组）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD UEUSGTYPEGP（修改UE USAGE TYPE群组）

## 功能

**适用网元：MME**

该命令用于修改UE USAGE TYPE群组的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组的描述信息。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEUSGTYPEGP]] · UE USAGE TYPE群组（UEUSGTYPEGP）

## 使用实例

修改 “UE USAGE TYPE群组标识” 为 “0” 的UE USAGE TYPE群组描述信息：

MOD UEUSGTYPEGP: UEUSGTYPEGPID=0, DESC="NB-IoT";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UE-USAGE-TYPE群组(MOD-UEUSGTYPEGP)_26305630.md`
