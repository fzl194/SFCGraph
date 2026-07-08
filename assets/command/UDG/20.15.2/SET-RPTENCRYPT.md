---
id: UDG@20.15.2@MMLCommand@SET RPTENCRYPT
type: MMLCommand
name: SET RPTENCRYPT（设置业务报表加密算法）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTENCRYPT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表加密控制
status: active
---

# SET RPTENCRYPT（设置业务报表加密算法）

## 功能

**适用NF：PGW-U、UPF**

此命令用于设置业务报表加密算法。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ENCRYMODE | ENCRYALGORI |
| --- | --- | --- |
| 初始值 | DEFAULT | SHA256 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENCRYMODE | 加密模式 | 可选必选说明：必选参数<br>参数含义：该参数用于配置报表个人敏感数据匿名化方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT：表示加密方式使用默认的SHA256加密方式，其使用的密钥通过U2020/MAE统一下发。<br>- USER_DEFINED：表示加密方式使用本命令设置的加密算法和加密密钥。<br>默认值：无<br>配置原则：无 |
| ENCRYALGORI | 业务报表加密算法 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于配置业务报表加密算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SHA256：表示加密类型为SHA256。<br>- SHA1：使用SHA1算法，有安全风险，不建议使用。<br>- AES256_CBC：表示加密类型为AES256_CBC，有安全风险不建议使用。<br>- AES256_GCM：表示加密类型为AES256_GCM。<br>- AES256_CTR：表示加密类型为AES256_CTR。<br>默认值：无<br>配置原则：无 |
| PSWDKEY | 密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于设置加密算法的密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255，单位是字节。不支持空格。<br>默认值：无<br>配置原则：如果是SHA1算法，密码长度为1~16； 如果是SHA256算法，密码长度为1~255； 如果是AES256算法，密码长度为1~32。 |
| PSWDKEYCONFIRM | 确认密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于确认加密算法的密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255，单位是字节。不支持空格。<br>默认值：无<br>配置原则：如果是SHA1算法，密码长度为1~16； 如果是SHA256算法，密码长度为1~255； 如果是AES256算法，密码长度为1~32。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTENCRYPT]] · 业务报表加密算法配置（RPTENCRYPT）

## 使用实例

设置报表加密模式为缺省：

```
SET RPTENCRYPT: ENCRYMODE=DEFAULT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-RPTENCRYPT.md`
