---
id: UDG@20.15.2@MMLCommand@MOD L2TPLNSINFO
type: MMLCommand
name: MOD L2TPLNSINFO（修改L2TP组的LNS信息）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: L2TPLNSINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2tp组Lns信息
status: active
---

# MOD L2TPLNSINFO（修改L2TP组的LNS信息）

## 功能

**适用NF：PGW-U、UPF**

修改L2TP组的LNS信息。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 只能通过MOD L2TPLNSINFO修改已有的LNS配置。
- 同一个组内的IP地址不能重复。
- 如果要修改L2TP组的IP类型，需要删除对应的L2TP组下所有L2TPLNSINFO配置。
- 当L2TP组存在用户时，不允许通过MOD L2TPLNSINFO命令修改LNSIP或密码信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO | LNS序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加LNS的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：无 |
| LNSIPVER | LNS IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LNS IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：LNS的IP版本号为IPv4。<br>- IPV6：LNS的IP版本号为IPV6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | LNS IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LNSIPVER”配置为“IPV4”时为必选参数。<br>参数含义：指定LNS的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | LNS IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LNSIPVER”配置为“IPV6”时为必选参数。<br>参数含义：指定该LNS的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| PWD | LNS隧道认证密码 | 可选必选说明：可选参数<br>参数含义：指定该LNS的密码。<br>数据来源：对端协商<br>取值范围：密码类型，不加密输入时，取值范围1～432个字符。不支持空格，区分大小写。输入PWD时，必须同时输入确认密码CFMPWD，且密码相同。<br>默认值：无<br>配置原则：无 |
| CFMPWD | 确认LNS隧道认证密码 | 可选必选说明：可选参数<br>参数含义：该参数用于确认LNS隧道认证密码。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～432。不支持空格，区分大小写。CFMPWD需要和PWD密码相同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L2TPLNSINFO]] · L2TP组的LNS信息（L2TPLNSINFO）

## 使用实例

假设用户需要修改隧道的IP地址：

```
MOD L2TPLNSINFO: GROUPID=1, LNSNO=1, LNSIPVER=IPV4, IPV4ADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-L2TPLNSINFO.md`
