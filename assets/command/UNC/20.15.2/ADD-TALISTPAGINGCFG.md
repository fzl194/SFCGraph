---
id: UNC@20.15.2@MMLCommand@ADD TALISTPAGINGCFG
type: MMLCommand
name: ADD TALISTPAGINGCFG（增加TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TALISTPAGINGCFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- S1寻呼TALIST寻呼管理
status: active
---

# ADD TALISTPAGINGCFG（增加TALIST寻呼不重发TAC区间）

## 功能

**适用网元：MME**

该命令用于设置S1模式TALIST寻呼不重发的TAC区间。

当部分TAC下的eNodeB寻呼提前过载，则使用本命令进行TAC区间配置。通过判断当前用户所在TALIST的TAC是否在配置的ADD TALISTPAGINGCFG里面，如果TALIST中的任意一个TAC在，则用户基于TALIST寻呼不进行重发。

## 注意事项

- 此命令最大记录数为128。
- 此命令只控制寻呼范围为TALIST的场景；如果匹配到精确寻呼或智能寻呼，只控制TALIST的寻呼是否重发。
- 该命令执行后立即生效，对命令配置后发起寻呼的4G、NSA和NBIOT用户生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0x0000~0xFFFF，输入时可以不输入0x前缀。<br>默认值： 无<br>配置原则：<br>- 新增的TAC区间不能和TALISTPAGINGCFG表中已有的TAC区间存在交集。该表通过本命令配置，并通过LST TALISTPAGINGCFG进行查询。<br>- 配置TAC区间为0x0000~0xFFFF，表示所有TALIST重发控制生效。 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0x0000~0xFFFF，输入时可以不输入0x前缀。<br>默认值：无<br>配置原则：<br>- 如果未输入TACRANGE或输入值等于TAC，则表示某个固定TAC。<br>- 输入的TACRANGE要大于或等于TAC。 |
| IMSPAGINGSW | 语音寻呼重传开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能语音类寻呼重传限制。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”<br>- “ON（开启）”<br>默认值：“ON（开启）”<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TALISTPAGINGCFG]] · TALIST寻呼不重发TAC区间（TALISTPAGINGCFG）

## 使用实例

增加TAC起始为0xBF85的跟踪区间：

ADD TALISTPAGINGCFG: TAC="0xBF85",IMSPAGINGSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TALISTPAGINGCFG.md`
