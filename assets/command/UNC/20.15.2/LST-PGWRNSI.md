---
id: UNC@20.15.2@MMLCommand@LST PGWRNSI
type: MMLCommand
name: LST PGWRNSI（查询PGW重定向配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWRNSI
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- GGSN_P-GW选择
status: active
---

# LST PGWRNSI（查询PGW重定向配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询PGW重定向配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定支持PGW重定向的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”:指网络中与指定的IMSI前缀匹配的用户。<br>- “HOME_USER(本网用户)”:指网络中的本网签约用户。<br>- “FOREIGN_USER(外网用户)”:指网络中的漫游用户。<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>- 默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在"用户范围"参数配置为"本网用户"或"外网用户"后生效。<br>数据来源：整网规划<br>取值范围：整数类型，取值范围为0~64,128~254。<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为0或128～254之间的值，该取值必须和[ADD MNO](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置的“MNOID”参数取值相同。<br>- 当用户为MVNO用户时，该参数需要配置为1～64之间的值，该取值必须和[ADD MVNO](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置的“MVNOID”参数取值相同。<br>- 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：当该参数配置生效时，按照IMSI最长匹配进行查询，如果匹配到记录，使用该记录的配置；如果没有匹配的记录，则查找IMSI次长匹配的记录。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：该APNNI需要与打开PGW重定向功能的用户携带的APNNI一致。<br>说明：紧急呼叫的APN不建议配置PGWRNSI功能，如果端到端规划不合理，可能导致紧急呼叫失败。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWRNSI]] · PGW重定向配置（PGWRNSI）

## 使用实例

查询所有PGW重定向配置：

LST PGWRNSI:;

```
%%LST 
PGWRNSI
:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                     用户范围  =  所有用户
                     IMSI前缀  =  NULL
                   运营商标识  =  NULL
                        APNNI  =  HUAWEI.COM
              是否开启PGWRNSI  =  支持
PGW-C/SMF同时携带FQDN和IP时处理策略  =  FQDN
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PGW重定向配置(LST-PGWRNSI)_18410968.md`
