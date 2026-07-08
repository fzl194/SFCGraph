---
id: UNC@20.15.2@MMLCommand@GET LOGFILE
type: MMLCommand
name: GET LOGFILE（获取审计日志文件）
nf: UNC
version: 20.15.2
verb: GET
object_keyword: LOGFILE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# GET LOGFILE（获取审计日志文件）

## 功能

本命令用于获取审计日志文件，审计日志包含操作日志、安全日志、系统日志。

审计日志文件也可在 OM Portal 界面 “ 安全>日志审计 ” 导出获取。

## 注意事项

该命令最多支持导出10万条记录。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SDT | 开始时间 | 可选必选说明：可选参数。<br>参数含义：日志收集起始时间。<br>取值范围：1990/01/01 00:00:00-2037/12/31 23:59:59。<br>默认值：无。<br>配置原则：无。 |
| EDT | 结束时间 | 可选必选说明：可选参数。<br>参数含义：收集日志结束时间。<br>数据来源：用户输入。<br>取值范围：1990/01/01 00:00:00-2037/12/31 23:59:59。<br>默认值：无。<br>配置原则：无。 |
| IP | 服务器IP | 可选必选说明：必选参数。<br>参数含义：SFTP服务器IP地址。<br>取值范围：长度不超过100个字符串。<br>默认值：无。<br>配置原则：无。 |
| USR | 用户名 | 可选必选说明：必选参数。<br>参数含义：SFTP用户名，从对端获取。<br>取值范围：长度不超过32的字符串。<br>默认值：无。<br>配置原则：无。 |
| PWD | 密码 | 可选必选说明：必选参数。<br>参数含义：SFTP用户密码，从对端获取。<br>取值范围：长度不超过128的密码。<br>默认值：无。<br>配置原则：无。 |
| DSTF | 服务端文件路径 | 可选必选说明：必选参数。<br>参数含义：用于标识SFTP传输的目标路径（含文件名）。<br>取值范围：长度不超过256的字符串。<br>默认值：无。<br>配置原则：文件名不能为点（.）或点点（..）；不能包含如下特殊字符：* : ? " < > \| ' ` ! $ # & ( )和空格。 |
| LT | 日志类型 | 可选必选说明：必选参数。<br>参数含义：标识收集日志的类型。<br>取值范围：<br>- OPERATING_LOG(操作日志)<br>- SECURITY_LOG(安全日志)<br>- SYSTEM_LOG(系统日志)<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：标识收集的网元ID。<br>可以通过执行LST ME命令获取。<br>取值范围：整数类型，取值范围为0~65535。<br>默认值：无。<br>配置原则：无。 |
| RSVFILE | 是否保留文件 | 可选必选说明：可选参数。<br>参数含义：标识是否保留文件。目前无作用。<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：NO（否）。<br>配置原则：无。 |
| FILETYPE | 文件类型 | 可选必选说明：可选参数。<br>参数含义：标识输出的文件类型。<br>取值范围：<br>- XML(XML)<br>- CSV(CSV)<br>默认值：无，如果不输入该参数，系统按照缺省值XML导出。<br>配置原则：无。 |
| LAN | 日志语言 | 可选必选说明：可选参数。<br>参数含义：标识输出的日志语言。<br>取值范围：<br>- ZH(中文)<br>- EN(英文)<br>默认值：无，如果不输入该参数，按照系统语言导出。<br>配置原则：无。 |
| PORT | 端口 | 可选必选说明：可选参数。<br>参数含义：SFTP服务器端口。<br>取值范围：整数类型，取值范围为1~65535。<br>默认值：22。<br>配置原则：与实际服务器上sftp服务启动指定端口号一致。 |
| MODE | 内容格式 | 可选必选说明：当<br>“FILETYPE”<br>取值为<br>“XML”<br>时，该参数为条件可选。<br>参数含义：XML文件内容的格式。<br>取值范围：<br>- NORMAL(普通)<br>- STANDARD(标准)<br>默认值：NORMAL(普通) 。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOGFILE]] · 保存黑匣子的数据到日志文件中（LOGFILE）

## 使用实例

获取审计日志文件：

```
%%GET LOGFILE: SDT=2019&11&21&16&23&16, EDT=2019&11&22&16&23&19, IP="10.213.11.7", USR="sftpuser", PWD="*****", DSTF="/ftpboot/text111.xml", LT=OPERATING_LOG, MEID=0, RSVFILE=NO, PORT=3605;%%
 RETCODE = 0  操作成功
进度报告
 --------
已完成 = 0%
 (结果个数 = 1)
---    END

%%GET LOGFILE: SDT=2019&11&21&16&23&16, EDT=2019&11&22&16&23&19, IP="10.213.11.7", USR="sftpuser", PWD="*****", DSTF="/ftpboot/text111.xml", LT=OPERATING_LOG, MEID=0, RSVFILE=NO, PORT=3605;%%
 RETCODE = 0  操作成功
进度报告
 --------
已完成 = 10%
 (结果个数 = 1)
---    END

%%GET LOGFILE: SDT=2019&11&21&16&23&16, EDT=2019&11&22&16&23&19, IP="10.213.11.7", USR="sftpuser", PWD="*****", DSTF="/ftpboot/text111.xml", LT=OPERATING_LOG, MEID=0, RSVFILE=NO, PORT=3605;%%
 RETCODE = 0  操作成功
进度报告
 --------
已完成 = 100%
 (结果个数 = 1)
---    END

%%GET LOGFILE: SDT=2019&11&21&16&23&16, EDT=2019&11&22&16&23&19, IP="10.213.11.7", USR="sftpuser", PWD="*****", DSTF="/ftpboot/text111.xml", LT=OPERATING_LOG, MEID=0, RSVFILE=NO, PORT=3605;%%
 RETCODE = 0  操作成功
结果信息
 --------
     状态  =  Success
 (结果个数 = 1)
共有4个报告
 ---    END

%%GET LOGFILE: IP="10.213.11.7", USR="sopuser", PWD="*****", DSTF="/home/sopuser/test.xml", LT=OPERATING_LOG, MEID=0, RSVFILE=NO, FILETYPE=XML, MODE=STANDARD;%% 
RETCODE = 0  操作成功  
结果信息 
--------
    状态  =  Success 
(结果个数 = 1)  
共有8个报告
 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/GET-LOGFILE.md`
