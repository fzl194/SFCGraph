---
id: UNC@20.15.2@MMLCommand@DSP BOSSOPINFO
type: MMLCommand
name: DSP BOSSOPINFO（查询BOSS操作信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BOSSOPINFO
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- BOSS操作信息
status: active
---

# DSP BOSSOPINFO（查询BOSS操作信息）

## 功能

**适用NF：NCG**

该命令用于查询BOSS登录NCG的操作信息。

## 注意事项

- 该命令查找BOSS最近的操作信息，最多返回200条符合条件的信息。
- 该命令最多查找最近10000条信息：如通过过滤条件查询200条信息，但是在最近的10000条信息中只有100条满足要求，则只返回100条记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRANSTYPE | 传输协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示BOSS登录NCG使用的协议。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- FTP：FTP协议<br>- SFTP：SFTP协议<br>默认值：无<br>配置原则：无。 |
| RUID | RU的ID | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询BOSS登录到NCG的RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| OPTYPE | BOSS操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询的BOSS登录NCG的操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- LOG：日志<br>默认值：LOG<br>配置原则：无。 |
| LOGNUM | Log数量 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OPTYPE”配置为“LOG”时为条件必选参数。<br>参数含义：该参数用来表示查询BOSS的操作日志的数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～200。<br>默认值：20<br>配置原则：无。 |
| FILER | 过滤条件 | 可选必选说明：可选参数<br>参数含义：该参数用来表示查询满足一定条件的BOSS操作信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～255。<br>默认值：无<br>配置原则：<br>1、不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。<br>2、使用字符串匹配过滤信息，如：日期、时间、文件名等。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BOSSOPINFO]] · BOSS操作信息（BOSSOPINFO）

## 使用实例

查询“传输协议类型”为“FTP”，“RU的ID”为“79”，“BOSS操作类型”为“LOG”，“Log数量”为“10”。示例如下：

```
DSP BOSSOPINFO: TRANSTYPE=FTP, RUID=79, OPTYPE=LOG, LOGNUM=10;
```

```
RETCODE = 0  操作成功
结果如下:
---------
结果索引   查询BOSS操作结果
1          2024-05-20 19:07:24 CHFCDRZCJF[cmd:PASS]Client:172.31.225.98:55791.
2          2024-05-20 19:07:24 [cmd:OPEN 10.69.35.49]Client:172.31.225.98:27081.
3          2024-05-20 19:07:24 CHFCDRZCJF[cmd:TYPE I]Client:172.31.225.98:55791.
4          2024-05-20 19:07:24 CHFCDRZCJF[cmd:USER CHFCDRZCJF]Client:172.31.225.98:27081.
5          2024-05-20 19:07:24 Post Operation, download /AP79_1/second/Zhejiang/ABNORMAL1/CHF008791_H_110100_20231202190723_00419387.dat@@Getting_by_xfer_sa_sacg75_No.8 ret:0 Progress: 100%
6          2024-05-20 19:07:24 CHFCDRZCJF[cmd:RETR /AP79_1/second/Zhejiang/ABNORMAL1/CHF008791_H_110100_20231202190723_00419387.dat@@Getting_by_xfer_sa_sacg75_No.8]Client:172.31.225.98:26301.
7          2024-05-20 19:07:24 CHFCDRZCJF[cmd:CWD /AP79_1/second/Zhejiang/ONLINE]Client:172.31.225.98:55791.
8          2024-05-20 19:07:24 CHFCDRZCJF[cmd:PASV]Client:172.31.225.98:55791.
9          2024-05-20 19:07:24 CHFCDRZCJF[cmd:LIST]Client:172.31.225.98:55791.
10         2024-05-20 19:07:24 CHFCDRZCJF[cmd:PASS]Client:172.31.225.98:27081.
(结果个数 = 10)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BOSS操作信息（DSP-BOSSOPINFO）_04110590.md`
