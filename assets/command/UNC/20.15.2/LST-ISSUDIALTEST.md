---
id: UNC@20.15.2@MMLCommand@LST ISSUDIALTEST
type: MMLCommand
name: LST ISSUDIALTEST（查询拨测用户配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ISSUDIALTEST
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
- 网络管理
- 灰度升级
- 拨测管理
status: active
---

# LST ISSUDIALTEST（查询拨测用户配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询拨测用户配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUSRRANGE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- “MSISDN(MSISDN)”<br>- “IMSI(IMSI)”<br>默认值：无 |
| BEGMSISDN | 起始MSISDN | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置拨测用户的起始MSISDN。<br>前提条件：该参数在<br>“用户标识类型”<br>参数配置为<br>“MSISDN(MSISDN)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>前提条件：该参数在<br>“用户标识类型”<br>参数配置为<br>“IMSI(IMSI)”<br>后生效。<br>数据来源：本端规划<br>取值范围：6～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ISSUDIALTEST]] · 拨测用户配置（ISSUDIALTEST）

## 使用实例

查询一条拨测用户配置，起始IMSI为123001111111111。

LST ISSUDIALTEST: BEGIMSI="123001111111111";

```
%%LST ISSUDIALTEST: BEGIMSI="123001111111111";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
      用户标识类型  =  IMSI
         起始IMSI  =  123001111111111
         终止IMSI  =  123001111111112
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ISSUDIALTEST.md`
