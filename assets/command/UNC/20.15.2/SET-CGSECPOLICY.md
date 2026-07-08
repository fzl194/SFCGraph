---
id: UNC@20.15.2@MMLCommand@SET CGSECPOLICY
type: MMLCommand
name: SET CGSECPOLICY（设置安全策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CGSECPOLICY
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 计费安全管理
status: active
---

# SET CGSECPOLICY（设置安全策略）

## 功能

![](设置安全策略（SET CGSECPOLICY）_51174350.assets/notice_3.0-zh-cn_2.png)

当安全策略配置低于默认配置时，可能存在安全风险，请谨慎操作。配置RODD分发目录只读参数后，需要执行“RST VNFC”重启服务。

**适用NF：NCG**

该命令用于设置NCG对外开放的FTP/SFTP服务的安全策略。开放FTP/SFTP服务时，密码参数必须符合本命令设置的密码复杂度。

## 注意事项

- 该命令执行后立即生效。
- 配置RODD分发目录只读参数后，需在“MML命令行 - UNC”窗口执行“**RST VNFC**”命令重新启动系统才能生效。
- 该命令最大记录数为1。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| PWDPO | MINPWDLEN | CHSET | HISPWDS | DICT | CONUSER | ALP | COLFBL | ALD | SSHAF | CDRANONYMITY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NO | 8 | LEAST_THREE | 5 | NO | NO | NO | 5 | 5 | HIGH_EA | ON |

| RODD | SFTPKEYEXCG | SFTPCLIPOLICY | ITERCOUNT | CDRQUERYANON |
| --- | --- | --- | --- | --- |
| ON | ON | ON | 1000 | ON |

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PWDPO | 口令复杂度自定义 | 可选必选说明：可选参数<br>参数含义：该参数用于设置口令复杂度是否自定义。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：当本参数设置为“YES”时，将采用用户自定义的口令复杂度策略，如果策略设置过于简单，会存在安全风险，请谨慎使用。 |
| MINPWDLEN | 口令最小长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PWDPO”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置账户口令的最小长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为6～32。<br>默认值：无<br>配置原则：无 |
| CHSET | 口令字符集 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PWDPO”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置口令中必须包含的字符集种类数目。该参数可配置为：“包含小写字母”、“包含大写字母”、“包含数字”、“包含特殊字符”四类字符集至少包含几种。其中特殊字符指以下字符：` ~ ! @ # % ^ & * ( ) - _ + \ \| [ { } ] : < . > /。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LEAST_ONE：至少一种字符集。<br>- LEAST_TWO：至少两种字符集。<br>- LEAST_THREE：至少三种字符集。<br>- LEAST_FOUR：至少四种字符集。<br>默认值：无<br>配置原则：无 |
| HISPWDS | 历史口令个数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PWDPO”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置口令不能修改为过去几次使用过的旧口令。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10。<br>默认值：无<br>配置原则：当本参数设置为“0”时，表示不限制历史口令使用。 |
| DICT | 口令是否使用字典词汇 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PWDPO”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置口令是否可以使用字典词汇。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| CONUSER | 口令是否允许包含用户名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PWDPO”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置是否允许口令包含用户名（或私钥文件名）的正序或倒序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：无 |
| ALP | 账户锁定策略自定义 | 可选必选说明：可选参数<br>参数含义：该参数用于设置账户锁定策略是否自定义。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：无<br>配置原则：当本参数设置为“YES”时，将采用用户自定义的账户锁定策略，如果策略设置过于简单，会存在安全风险，请谨慎使用。 |
| COLFBL | 登录失败尝试次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALP”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置登录失败尝试次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～99。<br>默认值：无<br>配置原则：<br>- 当本参数设置为“0”时，表示无论登录失败多少次，都不锁定账户。 |
| ALD | 账户持续锁定时间(分钟) | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALP”配置为“YES”时为条件可选参数。<br>参数含义：该参数用于设置账户持续锁定时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～999，单位是分钟。<br>默认值：无<br>配置原则：<br>- 当本参数设置为“0”时，表示无限期锁定。说明：FTP PULL任务不支持无限期锁定，当帐户持续锁定时间设定为<br>**0**<br>时，则代表帐户持续锁定时间设定为最大值，即<br>**999**<br>分钟。 |
| SSHAF | SSH算法族策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SSH使用的摘要的算法族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HIGH_EA：高密算法。<br>- LOW_EA：低密算法。<br>默认值：无<br>配置原则：如果该参数配置为“LOW_EA”时，系统存在安全风险，请谨慎使用。<br>说明：- 当取值为高密算法：**mac**<br>：<br>hmac-sha2-256、hmac-sha2-512<br>。<br>- 当取值为低密算法：**mac**<br>：<br>hmac-sha1、hmac-sha2-256、hmac-sha2-512、hmac-md5<br>。 |
| CDRANONYMITY | CDR匿名 | 可选必选说明：可选参数<br>参数含义：该参数用来控制CDR匿名功能是否开启。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：该参数配置为“ON”时，开启匿名化功能，配置为“OFF”时，不启用匿名化功能。 |
| RODD | 分发目录只读 | 可选必选说明：可选参数<br>参数含义：该参数用来控制分发目录功能只读是否开启。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：当本参数配置为“ON”时，开启分发目录只读功能，配置为“OFF”时，不启用分发目录只读功能。 |
| SFTPKEYEXCG | SFTP服务端密钥交换算法 | 可选必选说明：可选参数<br>参数含义：该参数用来控制SFTP服务端密钥交换算法、加密算法和主机密钥算法使用安全算法功能是<br>否<br>开启。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：该参数配置为“ON”时，启用SFTP服务端密钥交换安全算法功能。配置为“OFF”时，不启用SFTP服务端密钥交换安全算法功能，会存在安全风险，请谨慎使用。<br>说明：- 当取值为开启：**kex**<br>：<br>curve25519-sha256、curve25519-sha256@libssh.org、diffie-hellman-group-exchange-sha256、ecdh-sha2-nistp521、ecdh-sha2-nistp384<br>。**hostkey**<br>：<br>ssh-ed25519、rsa-sha2-512、rsa-sha2-256、ecdsa-sha2-nistp256<br>。**cipher**<br>：<br>chacha20-poly1305@openssh.com、aes128-ctr、aes192-ctr、aes256-ctr、aes128-gcm@openssh.com、aes256-gcm@openssh.com<br>。**PubkeyAcceptedKeyTypes**<br>：ssh-ed25519、rsa-sha2-512、rsa-sha2-256、ecdsa-sha2-nistp256、ecdsa-sha2-nistp384、ecdsa-sha2-nistp521。<br>- 当取值为关闭：**kex**<br>：<br>curve25519-sha256、curve25519-sha256@libssh.org、diffie-hellman-group-exchange-sha256、ecdh-sha2-nistp521、ecdh-sha2-nistp384、ecdh-sha2-nistp256、diffie-hellman-group-exchange-sha1、diffie-hellman-group14-sha1。**hostkey**<br>：<br>ssh-ed25519、rsa-sha2-512、rsa-sha2-256、ecdsa-sha2-nistp256、ssh-rsa<br>。**cipher**<br>：<br>chacha20-poly1305@openssh.com、aes128-ctr、aes192-ctr、aes256-ctr、aes128-gcm@openssh.com、aes256-gcm@openssh.com、aes128-cbc、aes192-cbc、aes256-cbc、3des-cbc<br>。**PubkeyAcceptedKeyTypes**<br>：ssh-ed25519、rsa-sha2-512、rsa-sha2-256、ecdsa-sha2-nistp256、ecdsa-sha2-nistp384、ecdsa-sha2-nistp521、ssh-rsa。 |
| SFTPCLIPOLICY | SFTP客户端密码策略 | 可选必选说明：可选参数<br>参数含义：该参数用来控制SFTP客户端密码策略使用安全算法功能是否开启。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：当本参数设置为“OFF”时，CG作为SFTP客户端时将兼容不安全算法，会存在安全风险，请谨慎使用。配置为“ON”时，如果服务端不支持安全算法，将会连接失败，上报ALM<br>**-**<br>82005 备份链路异常或ALM-82007 分发链路异常告警。<br>说明：- 当取值为开启：**kex**<br>：<br>diffie-hellman-group-exchange-sha256<br>。**mac**<br>：<br>hmac-sha2-512、hmac-sha2-256<br>。**hostkey**<br>：<br>rsa-sha2-256、rsa-sha2-512<br>。**cipher**<br>：<br>aes256-ctr、aes192-ctr、aes128-ctr<br>。<br>- 当取值为关闭：**kex**<br>：<br>diffie-hellman-group-exchange-sha256、diffie-hellman-group-exchange-sha1、diffie-hellman-group14-sha1、diffie-hellman-group1-sha1<br>。**mac**<br>：<br>hmac-sha2-512、hmac-sha2-256、hmac-sha1-96、hmac-sha1、hmac-md5-96、hmac-md5<br>。**hostkey**<br>：<br>rsa-sha2-256、rsa-sha2-512、<br>ssh-dss、ssh-rsa<br>。**cipher**<br>：<br>aes256-ctr、aes192-ctr、aes128-ctr、arcfour、aes256-cbc、aes192-cbc、aes128-cbc、3des-cbc<br>。 |
| ITERCOUNT | 迭代次数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置FTP密码不可逆加密的迭代次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000。<br>默认值：1000<br>配置原则：迭代次数设置过高，FTP并发登录会导致CPU过高，请谨慎使用。当本参数设置小于1000时，FTP PULL分发任务的密码长度最小14位且必须同时包含大小写，数字，特殊字符。修改迭代次数后，只能对之后配置的FTP PULL分发任务生效。 |
| CDRQUERYANON | MML话单查询匿名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用MML话单查询匿名化。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [安全策略（CGSECPOLICY）](configobject/UNC/20.15.2/CGSECPOLICY.md)

## 使用实例

设置NCG的安全策略为自定义口令复杂度，口令最小长度为8，密码字符集至少包含两种字符集，历史口令个数为2，口令使用字典词汇，口令允许包含用户名，自定义账户锁定策略，登录失败尝试次数为20，账户持续锁定时间为300分钟，SSH算法族策略为低密算法，分发目录只读开关开启，SFTP服务端密钥交换算法使用安全算法，CG作为SFTP客户端时使用安全算法，迭代次数为1000，MML话单查询匿名开启：

```
SET CGSECPOLICY: PWDPO=YES, MINPWDLEN=8, CHSET=LEAST_TWO, HISPWDS=2, DICT=YES, CONUSER=YES, ALP=YES, COLFBL=20, ALD=300, SSHAF=LOW_EA, CDRANONYMITY=ON, RODD=ON, SFTPKEYEXCG=ON, SFTPCLIPOLICY=ON, ITERCOUNT=1000,CDRQUERYANON=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置安全策略（SET-CGSECPOLICY）_51174350.md`
