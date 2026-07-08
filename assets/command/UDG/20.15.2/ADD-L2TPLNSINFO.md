---
id: UDG@20.15.2@MMLCommand@ADD L2TPLNSINFO
type: MMLCommand
name: ADD L2TPLNSINFO（添加LNS与L2TP组绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: L2TPLNSINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 45000
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2tp组Lns信息
status: active
---

# ADD L2TPLNSINFO（添加LNS与L2TP组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于在L2TP组中添加LNS信息。如果LNS信息超过6个时， 可以使用该命令添加LNS信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为45000。
- 系统最多支持配置45000条绑定关系。
- 通过ADD L2TPLNSINFO添加LNS配置前，需要先通过ADD L2TPGROUP配置L2TP组信息。
- 每个L2TP组最多可以绑定30个LNSINFO，ADD L2TPGROUP命令和当前命令配置的LNS总数不能超过30个。
- 使用ADD L2TPLNSINFO或ADD L2TPGROUP配置的同一个L2TP组内的LNS，IP地址不能重复。
- 使用ADD L2TPLNSINFO或ADD L2TPGROUP配置的同一个L2TP组内的LNS，不支持IPv4 LNS和IPv6 LNS共存的情况。
- ADD L2TPGROUP下的LNS IP序号与ADD L2TPLNSINFO的LNSNO不能相同。例如，如果使用ADD L2TPGROUP配置了FIRSTLNSIP相关信息，则不允许使用ADD L2TPLNSINFO配置LNSNO为1的LNS IP配置。
- 主备模式下，仅允许使用ADD/MOD L2TPGROUP配置IPv4 LNS信息；使用ADD/MOD L2TPLNSINFO配置IPv6 LNS信息，且LNSNO的值只能配置为1或2，LNSNO为1的是主LNS，LNSNO为2的是备LNS。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO | LNS序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加LNS的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：无 |
| LNSIPVER | LNS IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LNS IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：LNS的IP版本号为IPv4。<br>- IPV6：LNS的IP版本号为IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | LNS IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LNSIPVER”配置为“IPV4”时为必选参数。<br>参数含义：指定LNS的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | LNS IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LNSIPVER”配置为“IPV6”时为必选参数。<br>参数含义：指定该LNS的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| PWD | LNS隧道认证密码 | 可选必选说明：可选参数<br>参数含义：指定该LNS的密码。<br>数据来源：对端协商<br>取值范围：密码类型，不加密输入时，取值范围1～432个字符。不支持空格，区分大小写。输入PWD时，必须同时输入确认密码CFMPWD，且密码相同。<br>默认值：无<br>配置原则：无 |
| CFMPWD | 确认LNS隧道认证密码 | 可选必选说明：可选参数<br>参数含义：该参数用于确认LNS隧道认证密码。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～432。不支持空格，区分大小写。CFMPWD需要和PWD密码相同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L2TPLNSINFO]] · L2TP组的LNS信息（L2TPLNSINFO）

## 使用实例

当需要使用本地配置的L2TP信息接入L2TP用户时，需要使用该命令配置L2TP组下的LNS信息：

```
ADD L2TPLNSINFO: GROUPID=1, LNSNO=2, LNSIPVER=IPV4, IPV4ADDRESS="10.1.1.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-L2TPLNSINFO.md`
