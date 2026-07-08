---
id: UNC@20.15.2@MMLCommand@LST SMFDIALTEST
type: MMLCommand
name: LST SMFDIALTEST（查询SMF拨测用户配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFDIALTEST
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
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

# LST SMFDIALTEST（查询SMF拨测用户配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询拨测用户配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUSRRANGE | 用户标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置拨测用户类型。<br>数据来源：本端规划<br>取值范围：<br>- MSISDN（MSISDN）<br>- IMSI（IMSI）<br>默认值：无<br>配置原则：无 |
| BEGINMSISDN | 起始MSISDN | 可选必选说明：该参数在"TSTUSRRANGE"配置为"MSISDN"时为条件可选参数。<br>参数含义：该参数用于配置拨测用户的起始MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“MSISDN(MSISDN)”后生效。 |
| BEGINIMSI | 起始IMSI | 可选必选说明：该参数在"TSTUSRRANGE"配置为"IMSI"时为条件可选参数。<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“IMSI(IMSI)”后生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFDIALTEST]] · SMF拨测用户配置（SMFDIALTEST）

## 使用实例

查询一条拨测用户配置，起始IMSI为460001111111111。

```
%%LST SMFDIALTEST: BEGINIMSI="460001111111111";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
      用户标识类型  =  IMSI
        起始MSISDN  =  NULL
        终止MSISDN  =  NULL
          起始IMSI  =  460001111111111
          终止IMSI  =  460001111111112
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFDIALTEST.md`
