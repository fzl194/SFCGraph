---
id: UNC@20.15.2@MMLCommand@SET AUTOLOGPOLICY
type: MMLCommand
name: SET AUTOLOGPOLICY（设置日志自动备份策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AUTOLOGPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET AUTOLOGPOLICY（设置日志自动备份策略）

## 功能

本命令用于设置日志自动备份到第三方服务器的备份策略。备份策略是指自动备份审计日志到第三方服务器的备份周期、备份SFTP服务器参数等信息。

## 注意事项

- 该命令存在系统初始记录，参数OPERATORTPYE(操作类型)的初始设定值为OFF(关闭)。
- 根据备份周期进行备份，备份日志内容包含操作日志5000条、安全日志5000条和系统日志5000条。
- SFTP服务器端口默认使用22，如果实际环境中端口有变更需要使用**[ADD FWRULE](../../系统管理/路由管理/代理管理/增加转发规则（ADD FWRULE）_01524840.md)**命令增加转发规则。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPERATORTPYE | 操作类型 | 可选必选说明：必选参数。<br>参数含义：标识是否开启备份策略。<br>取值范围：<br>- ON(开启)<br>- OFF(关闭)<br>默认值：无。<br>配置原则：无。 |
| BACKUPPERIOD | 备份周期(分) | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：自动备份周期。<br>取值范围：整数类型，取值范围为30~43200。<br>默认值：无。<br>配置原则：无。 |
| BKSERVERIPTYPE | SFTP服务器IP地址类型 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：SFTP服务器IP地址类型。<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无。<br>配置原则：无。 |
| IPV4 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>且<br>“BKSERVERIPTYPE（SFTP服务器IP地址类型）”<br>为<br>“IPV4(IPV4)”<br>时，为条件必选参数。<br>参数含义：SFTP服务器IPV4地址。<br>取值范围：IPV4地址。<br>默认值：无。<br>配置原则：无。 |
| IPV6 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>且<br>“BKSERVERIPTYPE（SFTP服务器IP地址类型）”<br>为<br>“IPV6(IPV6)”<br>时，为条件必选参数。<br>参数含义：SFTP服务器IPV6地址。<br>取值范围：IPV6地址。<br>默认值：无。<br>配置原则：无。 |
| SFTPUSER | SFTP用户名 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：SFTP服务器用户名，从对端获取。<br>取值范围：长度不超过128的字符串。<br>默认值：无。<br>配置原则：无。 |
| SFTPPSSWD | SFTP密码 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：SFTP服务器用户密码，从对端获取。<br>取值范围：长度不超过128的密码。<br>默认值：无。<br>配置原则：无。 |
| DSTF | 目标目录 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：用于标识SFTP服务器传输的目标路径。<br>取值范围：长度不超过256的字符串。<br>默认值：无。<br>配置原则：无。 |
| LOGTYPE | 日志类型 | 可选必选说明：该参数在<br>“OPERATORTPYE(操作类型)”<br>为<br>“ON(开启)”<br>时，为条件必选参数。<br>参数含义：备份的日志类型。<br>取值范围：<br>- OPERATING_LOG(操作日志)<br>- SECURITY_LOG(安全日志)<br>- SYSTEM_LOG(系统日志)<br>默认值：无。<br>配置原则：<br>开启备份策略时，至少选择一种日志类型。 |

## 操作的配置对象

- [日志自动备份策略（AUTOLOGPOLICY）](configobject/UNC/20.15.2/AUTOLOGPOLICY.md)

## 使用实例

设置日志自动备份开启策略：

```
%%SET AUTOLOGPOLICY: OPERATORTPYE=ON, BACKUPPERIOD=30, BKSERVERIPTYPE=IPV4, IPV4="10.213.11.7", SFTPUSER="sftpuser", SFTPPSSWD="*****", DSTF="/ftpboot", LOGTYPE=OPERATING_LOG-0&SECURITY_LOG-1&SYSTEM_LOG-1;%%
RETCODE = 0 操作成功

--- END
```

设置日志自动备份关闭策略：

```
%%SET AUTOLOGPOLICY: OPERATORTPYE=OFF;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置日志自动备份策略（SET-AUTOLOGPOLICY）_89632096.md`
