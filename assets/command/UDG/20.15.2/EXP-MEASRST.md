---
id: UDG@20.15.2@MMLCommand@EXP MEASRST
type: MMLCommand
name: EXP MEASRST（导出测量结果文件）
nf: UDG
version: 20.15.2
verb: EXP
object_keyword: MEASRST
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# EXP MEASRST（导出测量结果文件）

## 功能

该命令用于导出网元的测量结果文件。

> **说明**
> 该命令最多支持同时下发4个并发导出任务，建议不同的任务导出到不同的目标目录下。
>
> 如果下发的并发任务存在导出相同名称的话统结果文件，且目标目录相同，会出现并发任务之间上传文件冲突，只有最后一个任务可全部导出成功，其他任务可能呈现部分文件导出失败。
>
> 在升级场景下，为兼容低版本需要，系统会在对接SFTP时针对安全算法使用兼容方式处理。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| SERVERIPTYPE | SFTP服务器IP地址类型 | 可选必选说明：必选参数<br>参数含义：用于标识SFTP服务器的IP地址类型。<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无。<br>配置原则：无。 |
| IPV4 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>“SFTP服务器IP地址类型”<br>配置为<br>“IPV4(IPV4)”<br>时为条件必选参数。<br>参数含义：标识SFTP服务器的IP地址。<br>取值范围：合法的IPv4地址。<br>默认值：无。<br>配置原则：无。 |
| IPV6 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>“SFTP服务器IP地址类型”<br>配置为<br>“IPV6(IPV6)”<br>时为条件必选参数。<br>参数含义：标识SFTP服务器的IP地址。<br>取值范围：合法的IPv6地址。<br>默认值：无。<br>配置原则：无。 |
| FTPUSER | SFTP用户名 | 可选必选说明：必选参数<br>参数含义：用于标识登录SFTP服务器的用户名。<br>取值范围：字符串类型，长度不超过128个字符。<br>默认值：无。<br>配置原则：无。 |
| FTPPSSWD | SFTP密码 | 可选必选说明：必选参数<br>参数含义：用于标识登录SFTP服务器的密码。<br>取值范围：字符串类型，长度不超过128个字符。<br>默认值：无。<br>配置原则：无。 |
| DSTF | 目标目录 | 可选必选说明：必选参数<br>参数含义：用于标识SFTP传输的目标路径。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：无。 |
| FTPPORT | SFTP端口号 | 可选必选说明：可选参数<br>参数含义：用于标识SFTP服务器的端口号。<br>取值范围：1～65535。<br>默认值：22。<br>配置原则：需要和真实的SFTP服务器端口一致，不填写则使用默认端口22。 |
| PRD | 测量周期 | 可选必选说明：必选参数。<br>参数含义：标识导出的周期。<br>取值范围：<br>- ALL(全部)<br>- FIVE(5分钟)<br>- FIFTEEN(15分钟)<br>- THIRTY(30分钟)<br>- SIXTY(1小时)<br>- ONE_DAY(一天)<br>默认值：无。<br>配置原则：无。 |
| SDT | 导出起始时间 | 可选必选说明：必选参数。<br>参数含义：导出起始时间。<br>取值范围：年月日时分秒，规则为YYYY/MM/DD HH:MM:SS。<br>默认值：客户端当前时间。<br>配置原则：无。 |
| EDT | 导出结束时间 | 可选必选说明：必选参数。<br>参数含义：导出结束时间。<br>取值范围：年月日时分秒，规则为YYYY/MM/DD HH:MM:SS。<br>默认值：客户端当前时间。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MEASRST]] · 测量结果文件（MEASRST）

## 使用实例

导出网元测量结果文件：

```
%EXP MEASRST: MEID=88, SERVERIPTYPE=IPV6, IPV6="fc00::1", FTPUSER="sftpserver", FTPPSSWD="*****", DSTF="/test", PRD=FIVE, SDT=2021&12&01&07&50&59, EDT=2021&12&20&08&51&02;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 0%
(结果个数 = 1)
---    END

%%EXP MEASRST: MEID=88, SERVERIPTYPE=IPV6, IPV6="fc00::1", FTPUSER="sftpserver", FTPPSSWD="*****", DSTF="/test", PRD=FIVE, SDT=2021&12&01&07&50&59, EDT=2021&12&20&08&51&02;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 100%
(结果个数 = 1)
---    END

%%EXP MEASRST: MEID=88, SERVERIPTYPE=IPV6, IPV6="fc00::1", FTPUSER="sftpserver", FTPPSSWD="*****", DSTF="/test", PRD=FIVE, SDT=2021&12&01&07&50&59, EDT=2021&12&20&08&51&02;%%
RETCODE = 0  操作成功

导出结果
--------
导出成功文件个数  =  1403
导出失败文件个数  =  0
(结果个数 = 1)

共有3个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/导出测量结果文件(EXP-MEASRST)_92314776.md`
