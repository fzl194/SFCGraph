---
id: UNC@20.15.2@MMLCommand@DSP MSISDN
type: MMLCommand
name: DSP MSISDN（显示指定IMSI用户MSISDN信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSISDN
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
- 系统管理
- 用户数据库管理
status: active
---

# DSP MSISDN（显示指定IMSI用户MSISDN信息）

## 功能

**适用网元：SGSN、MME**

该命令用于根据用户的IMSI查询MSISDN。

## 注意事项

- 如果所查用户不是附着用户或支持super charger的分离用户，该命令查询失败。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>取值范围：6～15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSISDN]] · 指定IMSI用户MSISDN信息（MSISDN）

## 使用实例

查询当前系统中IMSI为“123071104000955”的用户的MSISDN号：

DSP MSISDN: IMSI="123071104000955";

```
%%DSP MSISDN: IMSI="123071104000955";%%
RETCODE = 0  执行成功。  

根据IMSI查询MSISDN
------------------ 
IMSI对应的MSISDN  =  8613911040955   
（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示指定IMSI用户MSISDN信息(DSP-MSISDN)_26146352.md`
