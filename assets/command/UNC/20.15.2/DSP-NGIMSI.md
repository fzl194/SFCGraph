---
id: UNC@20.15.2@MMLCommand@DSP NGIMSI
type: MMLCommand
name: DSP NGIMSI（显示用户IMSI信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGIMSI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGIMSI（显示用户IMSI信息）

## 功能

**适用NF：AMF**

该命令用于查询用户的IMSI信息。

## 注意事项

此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、INNERUSRID。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- INNER_USER_ID（内部用户标识）<br>- AMF_UE_NGAP_ID（AMF UE NGAP ID）<br>默认值：无<br>配置原则：无 |
| INNERUSRID | 内部用户标识 | 可选必选说明：该参数在"QUERYOPT"配置为"INNER_USER_ID"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的内部用户标识，内部用户标识的格式是<AMF Pointer><5G-TMSI>，其中AMF Pointer是2个十六进制数字，5G-TMSI是8个十六进制数字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是10~2199。单个内部用户标识为10位十六进制数字，输入多个内部用户标识时使用“\|”分隔，最大支持输入200个内部用户标识。<br>默认值：无<br>配置原则：无 |
| AMFUENGAPID | AMF UE NGAP ID | 可选必选说明：该参数在"QUERYOPT"配置为"AMF_UE_NGAP_ID"时为条件必选参数。<br>参数含义：该参数用于指定AMF侧的终端NGAP连接标识，该标识由AMF分配，在同一个AMF Set内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是10~2199。单个AMF UE NGAP ID为10位十六进制数字，输入多个AMF UE NGAP ID时使用“\|”分隔，最大支持输入200个AMF UE NGAP ID。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIMSI]] · 用户IMSI信息（NGIMSI）

## 使用实例

查询INNERUSRID为016FEC6F36和01E1121B76用户的IMSI信息，执行如下命令：

```
%%DSP NGIMSI: QUERYOPT=INNER_USER_ID, INNERUSRID="016FEC6F36|01E1121B76";%%
RETCODE = 0  操作成功。

结果如下
------------------------
内部用户标识    AMF UE NGAP ID    IMSI 

016FEC6F36      NULL              460021214869128
01E1121B76      NULL              460009273128548
(结果个数 = 2)

---   END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGIMSI.md`
