---
id: UNC@20.15.2@MMLCommand@SET SMSCHRCFG
type: MMLCommand
name: SET SMSCHRCFG（设置SMS CHR单据上报策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSCHRCFG
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# SET SMSCHRCFG（设置SMS CHR单据上报策略）

## 功能

**适用NF：SMSF**

该命令用于设置SMS CHR单据上报策略。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HISRVPRCTMPLIDX | LOSRVPRCTMPLIDX |
| --- | --- |
| 0 | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HISRVPRCTMPLIDX | 高性能服务器上报流程控制模板索引 | 可选必选说明：可选参数<br>参数含义：控制网元向高性能CHR服务器发送的SMS CHR单据的流程列表，此索引必须已经通过ADD SMSCHRPRCTMPL命令配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHRCFG查询当前参数配置值。<br>配置原则：<br>系统会默认创建一条索引为0的SMSCHRPRCTMPL配置，供本参数引用。直接修改此默认的SMSCHRPRCTMPL配置即可控制向高性能的CHR上报的SMS CHR流程。 操作人员也可以自行配置一条SMSCHRPRCTMPL配置，并修改此参数指向新增的配置。 |
| LOSRVPRCTMPLIDX | 低性能服务器上报流程控制模板索引 | 可选必选说明：可选参数<br>参数含义：控制网元向低性能CHR服务器发送的SMS CHR单据的流程列表，此索引必须已经通过ADD SMSCHRPRCTMPL命令配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSCHRCFG查询当前参数配置值。<br>配置原则：<br>系统会默认创建一条索引为0的SMSCHRPRCTMPL配置，供本参数引用。直接修改此默认的SMSCHRPRCTMPL配置即可控制向高性能的CHR上报的SMS CHR流程。 操作人员也可以自行配置一条SMSCHRPRCTMPL配置，并修改此参数指向新增的配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHRCFG]] · SMS CHR单据上报策略（SMSCHRCFG）

## 使用实例

运营商希望设置“高性能服务器上报流程控制模板索引”为“1”，“低性能服务器上报流程控制模板索引”为“2”执行如下命令：

```
SET SMSCHRCFG:HISRVPRCTMPLIDX=1, LOSRVPRCTMPLIDX=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMS-CHR单据上报策略（SET-SMSCHRCFG）_53801290.md`
