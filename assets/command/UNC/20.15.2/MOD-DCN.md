---
id: UNC@20.15.2@MMLCommand@MOD DCN
type: MMLCommand
name: MOD DCN（修改DCN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DCN
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
- DCN配置
status: active
---

# MOD DCN（修改DCN）

## 功能

**适用网元：MME**

此命令用于修改指定DCN的类型或描述。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DCN标识。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：DCN ID不可重复。 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN所属PLMN的移动国家号码。<br>数据来源：全网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN所属PLMN的移动网号码。<br>数据来源：全网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无 |
| DCNTYPE | DCN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DCN的类型。<br>数据来源：全网规划<br>取值范围：<br>- “COMMON(普通DCN)”<br>- “DEFAULT(默认DCN)”<br>默认值：无<br>配置原则：默认DCN在PLMN内只能配置一条。<br>说明：当<br>UNC<br>判断专用核心网重选时，如果用户有规划普通DCN，将用户重选至普通DCN，否则将按照以下情况重选至默认DCN:<br>- 默认DCN通过[**ADD DCNMAP**](../DCN映射关系/增加DCN映射关系(ADD DCNMAP)_26305638.md)命令配置了UE USAGE TYPE范围：- MME获取到用户的UE USAGE TYPE，当用户的UE USAGE TYPE在默认DCN配置的UE USAGE TYPE范围内，则用户接入默认DCN，否则不接入。- MME未获取到用户的UE USAGE TYPE，则用户直接接入默认DCN。<br>- 默认DCN未配置UE USAGE TYPE范围，用户直接重选至默认DCN。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DCN描述信息。<br>数据来源：全网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DCN]] · DCN（DCN）

## 使用实例

“MCC” 为 “123” ， “MNC” 为 “01” 的运营商将eMtc用户的 “DCN类型” 修改为 “默认DCN” ：

MOD DCN: DCNID=0, MCC="123", MNC="01", DCNTYPE=DEFAULT, DESC="eMtc";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DCN.md`
