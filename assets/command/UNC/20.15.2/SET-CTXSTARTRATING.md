---
id: UNC@20.15.2@MMLCommand@SET CTXSTARTRATING
type: MMLCommand
name: SET CTXSTARTRATING（设置给OCS/CHF发送的消息初始携带的计费属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CTXSTARTRATING
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 5000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# SET CTXSTARTRATING（设置给OCS/CHF发送的消息初始携带的计费属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置上下文激活时的给OCS/CHF发送的消息的计费属性。配置该命令后，用户激活时，UNC与在线计费服务器交互的消息中将携带指定的费率组，在线计费服务器会给该费率组下发相应的配额。当用户从离线计费自动恢复成在线计费时，UNC根据该命令的配置决定是否在发送的消息中为该用户使用过的业务重新申请配额。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5000。
- 配置此命令需要通过ADD URRGROUP添加计费属性。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| CTXRURRGRPNAME1 | 初始请求URR组名称1 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME2 | 初始请求URR组名称2 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME3 | 初始请求URR组名称3 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME4 | 初始请求URR组名称4 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称4。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME5 | 初始请求URR组名称5 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称5。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME6 | 初始请求URR组名称6 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称6。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME7 | 初始请求URR组名称7 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称7。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME8 | 初始请求URR组名称8 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称8。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME9 | 初始请求URR组名称9 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称9。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CTXRURRGRPNAME10 | 初始请求URR组名称10 | 可选必选说明：可选参数<br>参数含义：指定CCR-Initial URR组名称10。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CTXSTARTRATING]] · 给OCS/CHF发送的消息初始携带的计费属性（CTXSTARTRATING）

## 使用实例

假如运营商需要绑定上下文激活时的给OCS/CHF发送的计费属性到名称为“testuserprofilename”的用户模板：

```
SET CTXSTARTRATING:USERPROFILENAME="testuserprofilename",CTXRURRGRPNAME1="testctxrchgproname1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CTXSTARTRATING.md`
