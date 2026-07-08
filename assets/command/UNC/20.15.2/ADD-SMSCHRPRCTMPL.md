---
id: UNC@20.15.2@MMLCommand@ADD SMSCHRPRCTMPL
type: MMLCommand
name: ADD SMSCHRPRCTMPL（增加SMS CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMSCHRPRCTMPL
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

# ADD SMSCHRPRCTMPL（增加SMS CHR流程控制模板）

## 功能

**适用NF：SMSF**

该命令用于SMS CHR流程控制模板，用以控制CHR的采集流程。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMPLIDX | SMSCHRFAILPRC |
| --- | --- |
| 0 | OTHER-1&SMSFREG-1&SMSFDEREG-1&SMSFMO-1&SMSFMT-1&VLRLUR-1&VLRDETACH-1&VLRMO-1&VLRMT-1&VLRALERT-1 |
| 1 | OTHER-1&SMSFREG-1&SMSFDEREG-1&SMSFMO-1&SMSFMT-1&VLRLUR-1&VLRDETACH-1&VLRMO-1&VLRMT-1&VLRALERT-1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| SMSCHRFAILPRC | SMS CHR失败流程上报选项 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMS CHR失败流程上报选项。<br>数据来源：本端规划<br>取值范围：<br>- “OTHER（其他流程需要上报CHR单据）”：表示其他流程需要上报CHR单据。<br>- “SMSFREG（5G注册流程需要上报CHR单据）”：表示5G注册流程需要上报CHR单据。<br>- “SMSFDEREG（5G去注册流程需要上报CHR单据）”：表示5G去注册流程需要上报CHR单据。<br>- “SMSFMO（5G MO流程需要上报CHR单据）”：表示5G MO流程需要上报CHR单据。<br>- “SMSFMT（5G MT流程需要上报CHR单据）”：表示5G MT流程需要上报CHR单据。<br>- “VLRLUR（4G位置更新流程需要上报CHR单据）”：表示4G位置更新流程需要上报CHR单据。<br>- “VLRDETACH（4G去注册流程需要上报CHR单据）”：表示4G去注册流程需要上报CHR单据。<br>- “VLRMO（4G MO流程需要上报CHR单据）”：表示4G MO流程需要上报CHR单据。<br>- “VLRMT（4G MT流程需要上报CHR单据）”：表示4G MT流程需要上报CHR单据。<br>- “VLRALERT（4G用户可达通知流程需要上报CHR单据）”：表示4G用户可达通知流程需要上报CHR单据。<br>默认值：OTHER-1&SMSFREG-1&SMSFDEREG-1&SMSFMO-1&SMSFMT-1&VLRLUR-1&VLRDETACH-1&VLRMO-1&VLRMT-1&VLRALERT-1<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHRPRCTMPL]] · SMS CHR流程控制模板（SMSCHRPRCTMPL）

## 使用实例

运营商希望增加“流程控制模板索引”为“1”，“短信CHR失败流程上报选项”为“5G注册流程需要上报CHR单据”的SMS CHR流程控制模板，执行如下命令 ：

```
ADD SMSCHRPRCTMPL: TMPLIDX=3, SMSCHRFAILPRC=OTHER-0&SMSFREG-1&SMSFDEREG-1&SMSFMO-1&SMSFMT-0&VLRLUR-0&VLRDETACH-0&VLRMO-0&VLRMT-0&VLRALERT-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMS-CHR流程控制模板（ADD-SMSCHRPRCTMPL）_53481530.md`
