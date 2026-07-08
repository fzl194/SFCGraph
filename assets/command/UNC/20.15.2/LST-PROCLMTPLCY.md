---
id: UNC@20.15.2@MMLCommand@LST PROCLMTPLCY
type: MMLCommand
name: LST PROCLMTPLCY（查询流程限制策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROCLMTPLCY
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 流程限制管理
status: active
---

# LST PROCLMTPLCY（查询流程限制策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询流程限制策略。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>默认值：无<br>配置原则：MME重选策略优先级高到低为：“IMSIPRE(IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”， “ALL_USER(所有用户)”。 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在"用户范围"参数配置为"指定IMSI前缀"后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无 |

## 操作的配置对象

- [流程限制策略（PROCLMTPLCY）](configobject/UNC/20.15.2/PROCLMTPLCY.md)

## 使用实例

1.查询一条 “用户范围” 为 “ALL_USER” 的流程限制策略配置：

LST PROCLMTPLCY: SUBRANGE=ALL_USER;

```
%%
LST PROCLMTPLCY: SUBRANGE=ALL_USER
;%%
RETCODE = 0  操作成功。

操作结果如下
------------
         用户范围  =  所有用户
       运营商标识  =  NULL
         IMSI前缀  =  NULL
    限制SRVCC流程  =  是
限制紧急SRVCC流程  =  是
  SRVCC失败原因值  =  自定义
     自定义原因值  =  100
     限制CS域业务  =  是  
   CS域失败原因值  =  #16 MSC temporarily not reachable
(结果个数 = 1)

---    END
```

2.查询全部的流程限制策略配置：

LST PROCLMTPLCY:;

```
%%LST PROCLMTPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
用户范围        运营商标识    IMSI前缀           限制SRVCC流程    限制紧急SRVCC流程    SRVCC失败原因值    自定义原因值    限制CS域业务    CS域失败原因值

所有用户        NULL          NULL               是               是                   自定义             20              是              #16 MSC temporarily not reachable
本网用户        1             NULL               是               是                   自定义             20              是              #16 MSC temporarily not reachable
指定IMSI前缀    NULL          123456789012345    是               是                   自定义             20              是              #16 MSC temporarily not reachable
------------
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流程限制策略(LST-PROCLMTPLCY)_26145630.md`
