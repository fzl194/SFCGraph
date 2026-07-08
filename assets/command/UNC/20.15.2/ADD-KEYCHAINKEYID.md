---
id: UNC@20.15.2@MMLCommand@ADD KEYCHAINKEYID
type: MMLCommand
name: ADD KEYCHAINKEYID（增加Keychain Key ID的配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: KEYCHAINKEYID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain Key ID配置
status: active
---

# ADD KEYCHAINKEYID（增加Keychain Key ID的配置）

## 功能

该命令用于设置Keychain Key ID的各种属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为单个Keychain下的最大记录数。
- Keychain名称可以通过LST KEYCHAIN命令获取。
- 为了保证更好的安全性，建议使用SHA-256算法或者HMAC-SHA-256算法。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |
| KEYID | Key索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Key索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |
| KEYSTRING | 密码字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定密码字段。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～255。字符不包括问号和空格。<br>默认值：无<br>配置原则：<br>- 字符不允许包括问号和空格。<br>- 配置的密码建议至少包含大写、小写、特殊字符、数字中的2种，并且长度不能小于6。 |
| ALGORITHM | 认证算法 | 可选必选说明：必选参数<br>参数含义：该参数用于指定认证算法。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- MD5：认证算法为MD5。<br>- SHA-1：认证算法为SHA-1。<br>- HMAC-MD5：认证算法为HMAC-MD5。<br>- HMAC-SHA1-12：认证算法为HMAC-SHA1-12。<br>- HMAC-SHA1-20：认证算法为HMAC-SHA1-20。<br>- HMAC-SHA-256：认证算法为HMAC-SHA-256。<br>- SHA-256：认证算法为SHA-256。<br>默认值：无<br>配置原则：在使用中需要注意，MD5、HMAC-MD5、SHA-1、HMAC-SHA1-20和HMAC-SHA1-12属于不安全的加密算法。为了保证更好的安全性，建议不要使用MD5、HMAC-MD5、SHA-1、HMAC-SHA1-20和HMAC-SHA1-12算法，建议使用HMAC-SHA-256或者SHA-256验证方式。 |
| DEFSENDKEYID | 是否默认发送Key ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定默认发送Key索引。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：非默认的发送key-id。<br>- TRUE：默认的发送key-id。<br>默认值：FALSE |
| MODE | 生效模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Keychain生效模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABSOLUTE：绝对时间生效模式。<br>- DAILY：日周期生效模式。<br>- MONTHLY：月周期生效模式。<br>- WEEKLY：周周期生效模式。<br>- YEARLY：年周期生效模式。<br>默认值：无 |
| SENDDURTYPE | 发送时长类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE”时为必选参数。<br>参数含义：该参数用于指定发送时长类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DURATION：持续某段时间。<br>- INFINITE：持续永久。<br>- ENDTIME：持续到某个结束时间。<br>默认值：无 |
| SENDSTARTDATE | 发送起始日期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE”时为必选参数。<br>参数含义：该参数用于指定发送起始日期。<br>数据来源：本端规划<br>取值范围：日期类型，输入格式是YYYY&MM&DD。取值范围是1970年1月1日～2050年12月31日。<br>默认值：无 |
| SENDSTARTTIME | 发送起始时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE” 或 “DAILY”时为必选参数。<br>参数含义：该参数用于指定发送起始时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。取值范围是00:00～23:59。<br>默认值：无 |
| SENDDURATION | 发送时长（min） | 可选必选说明：条件必选参数<br>前提条件：该参数在“SENDDURTYPE”配置为“DURATION”时为必选参数。<br>参数含义：该参数用于指定发送时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～26280000，单位是分钟。<br>默认值：无 |
| SENDWEEKLY | 发送每周周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“WEEKLY”时为必选参数。<br>参数含义：该参数用于指定发送每周周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- MON：星期一。<br>- TUE：星期二。<br>- WED：星期三。<br>- THU：星期四。<br>- FRI：星期五。<br>- SAT：星期六。<br>- SUN：星期日。<br>默认值：无 |
| SENDMONTHLY | 发送每月周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“MONTHLY”时为必选参数。<br>参数含义：该参数用于指定发送每月周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- DAY1：1号。<br>- DAY2：2号。<br>- DAY3：3号。<br>- DAY4：4号。<br>- DAY5：5号。<br>- DAY6：6号。<br>- DAY7：7号。<br>- DAY8：8号。<br>- DAY9：9号。<br>- DAY10：10号。<br>- DAY11：11号。<br>- DAY12：12号。<br>- DAY13：13号。<br>- DAY14：14号。<br>- DAY15：15号。<br>- DAY16：16号。<br>- DAY17：17号。<br>- DAY18：18号。<br>- DAY19：19号。<br>- DAY20：20号。<br>- DAY21：21号。<br>- DAY22：22号。<br>- DAY23：23号。<br>- DAY24：24号。<br>- DAY25：25号。<br>- DAY26：26号。<br>- DAY27：27号。<br>- DAY28：28号。<br>- DAY29：29号。<br>- DAY30：30号。<br>- DAY31：31号。<br>默认值：无 |
| SENDYEARLY | 发送每年周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“YEARLY”时为必选参数。<br>参数含义：该参数用于指定发送每年周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- JAN：一月。<br>- FEB：二月。<br>- MAR：三月。<br>- APR：四月。<br>- MAY：五月。<br>- JUN：六月。<br>- JUL：七月。<br>- AUG：八月。<br>- SEP：九月。<br>- OCT：十月。<br>- NOV：十一月。<br>- DEC：十二月。<br>默认值：无 |
| SENDENDDATE | 发送结束日期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SENDDURTYPE”配置为“ENDTIME”时为必选参数。<br>参数含义：该参数用于指定发送结束日期。<br>数据来源：本端规划<br>取值范围：日期类型，输入格式是YYYY&MM&DD。取值范围是1970年1月1日～2050年12月31日。结束日期必须不小于开始日期。<br>默认值：无 |
| SENDENDTIME | 发送结束时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SENDDURTYPE”配置为“ENDTIME”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“DAILY”时为必选参数。<br>参数含义：该参数用于指定发送结束时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。取值范围是00:00～23:59。结束时间必须不小于开始时间。<br>默认值：无 |
| RCVDURTYPE | 接收时长类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE”时为必选参数。<br>参数含义：该参数用于指定接收时长类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DURATION：持续某段时间。<br>- INFINITE：持续永久。<br>- ENDTIME：持续到某个结束时间。<br>默认值：无 |
| RCVSTARTDATE | 接收起始日期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE”时为必选参数。<br>参数含义：该参数用于指定接收起始日期。<br>数据来源：本端规划<br>取值范围：日期类型，输入格式是YYYY&MM&DD。取值范围是1970年1月1日～2050年12月31日。<br>默认值：无 |
| RCVSTARTTIME | 接收起始时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“ABSOLUTE” 或 “DAILY”时为必选参数。<br>参数含义：该参数用于指定接收起始时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。取值范围是00:00～23:59。<br>默认值：无 |
| RCVDURATION | 接收时长（min） | 可选必选说明：条件必选参数<br>前提条件：该参数在“RCVDURTYPE”配置为“DURATION”时为必选参数。<br>参数含义：该参数用于指定接收时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～26280000，单位是分钟。<br>默认值：无 |
| RCVWEEKLY | 接收每周周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“WEEKLY”时为必选参数。<br>参数含义：该参数用于指定接收每周周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- MON：星期一。<br>- TUE：星期二。<br>- WED：星期三。<br>- THU：星期四。<br>- FRI：星期五。<br>- SAT：星期六。<br>- SUN：星期日。<br>默认值：无 |
| RCVMONTHLY | 接收每月周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“MONTHLY”时为必选参数。<br>参数含义：该参数用于指定接收每月周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- DAY1：1号。<br>- DAY2：2号。<br>- DAY3：3号。<br>- DAY4：4号。<br>- DAY5：5号。<br>- DAY6：6号。<br>- DAY7：7号。<br>- DAY8：8号。<br>- DAY9：9号。<br>- DAY10：10号。<br>- DAY11：11号。<br>- DAY12：12号。<br>- DAY13：13号。<br>- DAY14：14号。<br>- DAY15：15号。<br>- DAY16：16号。<br>- DAY17：17号。<br>- DAY18：18号。<br>- DAY19：19号。<br>- DAY20：20号。<br>- DAY21：21号。<br>- DAY22：22号。<br>- DAY23：23号。<br>- DAY24：24号。<br>- DAY25：25号。<br>- DAY26：26号。<br>- DAY27：27号。<br>- DAY28：28号。<br>- DAY29：29号。<br>- DAY30：30号。<br>- DAY31：31号。<br>默认值：无 |
| RCVYEARLY | 接收每年周期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“YEARLY”时为必选参数。<br>参数含义：该参数用于指定接收每年周期。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- JAN：一月。<br>- FEB：二月。<br>- MAR：三月。<br>- APR：四月。<br>- MAY：五月。<br>- JUN：六月。<br>- JUL：七月。<br>- AUG：八月。<br>- SEP：九月。<br>- OCT：十月。<br>- NOV：十一月。<br>- DEC：十二月。<br>默认值：无 |
| RCVENDDATE | 接收结束日期 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RCVDURTYPE”配置为“ENDTIME”时为必选参数。<br>参数含义：该参数用于指定接收结束日期。<br>数据来源：本端规划<br>取值范围：日期类型，输入格式是YYYY&MM&DD。取值范围是1970年1月1日～2050年12月31日。结束日期必须不小于开始日期。<br>默认值：无 |
| RCVENDTIME | 接收结束时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RCVDURTYPE”配置为“ENDTIME”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“DAILY”时为必选参数。<br>参数含义：该参数用于指定接收结束时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是HH:MM。取值范围是00:00～23:59。结束时间必须不小于开始时间。<br>默认值：无 |

## 操作的配置对象

- [Keychain Key ID的配置（KEYCHAINKEYID）](configobject/UNC/20.15.2/KEYCHAINKEYID.md)

## 使用实例

配置Keychain ospf的Key ID 1，密码为ospfKeychain，认证算法HMAC-SHA-256，是默认发送key-id，生效模式为周周期，发送时间为周一周三周五，接收时间为每周二周四周六：

```
ADD KEYCHAINKEYID:KEYCHAINNAME="ospf",KEYID=1,KEYSTRING="******",ALGORITHM=HMAC-SHA-256,DEFSENDKEYID=TRUE,MODE=WEEKLY,SENDWEEKLY=MON-1&WED-1&FRI-1,RCVWEEKLY=TUE-1&THU-1&SAT-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Keychain-Key-ID的配置（ADD-KEYCHAINKEYID）_00441313.md`
