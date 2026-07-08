---
id: UNC@20.15.2@MMLCommand@SND S1MESSAGE
type: MMLCommand
name: SND S1MESSAGE（发送模拟S1AP错误消息）
nf: UNC
version: 20.15.2
verb: SND
object_keyword: S1MESSAGE
command_category: 调测类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1消息
status: active
---

# SND S1MESSAGE（发送模拟S1AP错误消息）

## 功能

**适用网元：MME**

该命令用于向MME或eNodeB发送一条错误消息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PROCESSNO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGP进程所在的进程号。通过<br>[**DSP PROCESSLINK**](../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询LINK进程信息(DSP PROCESSLINK)_11295772.md)<br>获取。<br>取值范围：0～20<br>默认值：无 |
| MESSAGETYPE | 消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所模拟消息的类型。<br>取值范围：<br>- “MME(模拟MME消息)”<br>- “ENODEB(模拟eNodeB消息)”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>该参数用于指定S1AP链路的eNodeB的移动国家码。<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1AP链路的eNodeB的移动网号。<br>取值范围：2～3位的十进制数<br>默认值：无<br>说明：如果MCC相同，有效长度为2和3的MNC的前两位不允许相同。 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1AP链路的eNodeB的类型。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”<br>- “MACRO_ENB(MACRO_ENB)”<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1AP链路的eNodeB的标识。<br>取值范围：0～268435455<br>默认值：无 |
| MESSAGELEN | 消息长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1AP的消息长度。<br>长度范围：0～4294967294<br>默认值：100<br>说明：当<br>“消息类型”<br>配置为<br>“ENODEB(模拟eNodeB消息)”<br>时，该参数不能为0，且支持的最大值为20480。 |

## 操作的配置对象

- [发送模拟S1AP错误消息（S1MESSAGE）](configobject/UNC/20.15.2/S1MESSAGE.md)

## 使用实例

向编号为12的NODEB，发送消息长度为200的错误消息：

SND S1MESSAGE: RUNAME="LINK_SP_RU_0064", PROCESSNO=0, MESSAGETYPE=ENODEB, MCC="123", MNC="230", ENODEBTYPE=HOME_ENB, ENODEBID=12, MESSAGELEN=200;

## 证据

- 原始手册：`evidence/UNC/20.15.2/发送模拟S1AP错误消息(SND-S1MESSAGE)_72225923.md`
