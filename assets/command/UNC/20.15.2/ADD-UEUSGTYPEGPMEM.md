---
id: UNC@20.15.2@MMLCommand@ADD UEUSGTYPEGPMEM
type: MMLCommand
name: ADD UEUSGTYPEGPMEM（增加UE USAGE TYPE群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UEUSGTYPEGPMEM
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
- UE USAGE TYPE群组成员管理
status: active
---

# ADD UEUSGTYPEGPMEM（增加UE USAGE TYPE群组成员）

## 功能

**适用网元：MME**

此命令用于为UE USAGE TYPE群组添加一条成员记录。MME为该群组范围内的用户通过DNS查找到对应网元。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>配置原则：<br>- 此参数已通过[**ADD UEUSGTYPEGP**](../UE USAGE TYPE群组管理/增加UE USAGE TYPE群组(ADD UEUSGTYPEGP)_72225499.md)配置。<br>- 同一个“UE USAGE TYPE群组标识”可配置多条记录。 |
| BGNUEUSGTYPE | 起始UE USAGE TYPE | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE范围的起始值。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无 |
| ENDUEUSGTYPE | 终止UE USAGE TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE的终止值。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：<br>- 该参数的取值需要大于或者等于“起始UE USAGE TYPE”。<br>说明：- 该参数与“起始UE USAGE TYPE”参数构成一个UE USAGE TYPE范围，方便维护人员配置连续的UE USAGE TYPE区段。<br>- 该值如果不输入，默认与“起始UE USAGE TYPE”相同。<br>- 同一个群组标识下的UE USAGE TYPE范围不可重叠。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEUSGTYPEGPMEM]] · UE USAGE TYPE群组成员（UEUSGTYPEGPMEM）

## 使用实例

运营商为“eMtc”专网规划一个“UE USAGE TYPE群组标识”为“1”的UE USAGE TYPE群组，对于UE USAGE TYPE在“100”至“120”范围内的用户，MME能够通过DNS查询找到对应网元：

- ADD UEUSGTYPEGP: UEUSGTYPEGPID=1, DESC="eMtc";
- ADD UEUSGTYPEGPMEM: UEUSGTYPEGPID=1, BGNUEUSGTYPE=100, ENDUEUSGTYPE=120;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UEUSGTYPEGPMEM.md`
