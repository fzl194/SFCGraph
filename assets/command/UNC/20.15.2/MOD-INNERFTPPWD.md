---
id: UNC@20.15.2@MMLCommand@MOD INNERFTPPWD
type: MMLCommand
name: MOD INNERFTPPWD（修改内部FTPS账号密码）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: INNERFTPPWD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 账号维护
status: active
---

# MOD INNERFTPPWD（修改内部FTPS账号密码）

## 功能

![](修改内部FTPS账号密码（MOD INNERFTPPWD）_59103445.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，可能会导致网元内部FTPS服务通信故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于修改内部FTPS账号（如：ftpvrpv8_x，x是VNFC实例的ID）的密码。

## 注意事项

- 该命令执行后立即生效。
- 执行该操作后，内部FTPS账号的密码将被修改。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USER | 内部FTPS账号的用户名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内部FTPS账号的用户名。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为8～32的字符串。<br>默认值：无 |
| PWD | 内部FTPS账号的密码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内部FTPS账号的密码。<br>数据来源：本端规划<br>取值范围：密码类型，长度为8～64的字符串。<br>默认值：无<br>配置原则：<br>- 密码区分大小写。<br>- 密码必须包含数字、大写字母、小写字母、特殊字符（`~!@#$%^&*()-_+\\|[{}]:<.>/）这四类字符集中的两种字符集合的组合，不包括逗号、分号、等号，双引号、单引号，问号和空格。<br>- 密码中不建议包含如下字符串：“%%”、“+++”。<br>- 密码不能与操作系统用户名或用户名倒写字符串相同，密码与用户名比较时不区分大小写。<br>- 采用256位AES算法加密。 |
| CFM | 内部FTPS账号的确认密码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内部FTPS账号的确认密码。<br>数据来源：本端规划<br>取值范围：密码类型，长度为8～64的字符串。<br>默认值：无<br>配置原则：<br>- 密码区分大小写。<br>- 密码必须包含数字、大写字母、小写字母、特殊字符（`~!@#$%^&*()-_+\\|[{}]:<.>/）这四类字符集中的两种字符集合的组合，不包括逗号、分号、等号，双引号、单引号，问号和空格。<br>- 密码中不建议包含如下字符串：“%%”、“+++”。<br>- 密码不能与操作系统用户名或用户名倒写字符串相同，密码与用户名比较时不区分大小写。<br>- 采用256位AES算法加密。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INNERFTPPWD]] · 内部FTPS账号密码（INNERFTPPWD）

## 使用实例

修改内部FTPS账号（如：ftpvrpv8_x，x是VNFC实例的ID）的密码：

```
MOD INNERFTPPWD:USER="ftpvrpv8_x",PWD="*****",CFM="*****"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改内部FTPS账号密码（MOD-INNERFTPPWD）_59103445.md`
