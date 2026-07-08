---
id: UNC@20.15.2@MMLCommand@ADD DRA
type: MMLCommand
name: ADD DRA（增加DRA）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DRA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 80
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- DRA管理
- DRA信息
status: active
---

# ADD DRA（增加DRA）

## 功能

**适用NF：PGW-C、SMF**

此命令用于增加DRA的基本信息，配置DRA主机名、VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为80。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DRA的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数不支持与PCRF、OCS、BMSC等Diameter应用的主机名重名。该参数错误，会导致DRA连接不能建立，DRA状态异常。<br>- 软参BIT150置1与否，都不允许配置两个转小写后名字相同的DRA。 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DRA所在的vpn-instance的实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送给DRA的信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：46<br>配置原则：无 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示UNC每秒发送给该DRA的最大CCR消息数，但CCR-T消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0<br>配置原则：该参数配置为0时，表示不控制发送给该DRA的CCR消息数。 |
| REALMNAME | DRA域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DRA的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DRA（DRA）](configobject/UNC/20.15.2/DRA.md)

## 使用实例

根据网络规划，需要新增一个DRA的实例，并且在UNC上规划DRA的vpn实例为vpn1，则通过该命令新增一个DRA：

```
ADD DRA:HOSTNAME="dra1",VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DRA（ADD-DRA）_09897291.md`
