---
id: UDG@20.15.2@MMLCommand@MOD UPDRA
type: MMLCommand
name: MOD UPDRA（修改DRA）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: UPDRA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- DRA管理
- DRA信息
status: active
---

# MOD UPDRA（修改DRA）

## 功能

**适用NF：UPF**

![](修改DRA（MOD UPDRA）_97314571.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改对端信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用于修改DRA的基本信息，修改特定的DRA。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后可能导致DRA闪断，影响链路连接。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DRA的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DRA所在的vpn-instance的实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送给DRA的信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示UPF每秒发送给该DRA的最大DER消息数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：该参数配置为0时，表示不控制发送给该DRA的DER消息数。 |
| REALMNAME | DRA域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DRA的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDRA]] · DRA（UPDRA）

## 使用实例

根据网络规划，需要在UPF上修改DRA的vpn实例为vpn2，则通过该命令修改一个DRA：

```
MOD UPDRA:HOSTNAME="dra1",VPNINSTANCE="vpn2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改DRA（MOD-UPDRA）_97314571.md`
