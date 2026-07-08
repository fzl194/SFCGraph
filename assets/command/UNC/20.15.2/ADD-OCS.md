---
id: UNC@20.15.2@MMLCommand@ADD OCS
type: MMLCommand
name: ADD OCS（增加OCS）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OCS
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Server
status: active
---

# ADD OCS（增加OCS）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加OCS的基本信息，包括OCS主机名、域名、VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSHOSTNAME | Ocs主机名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数不支持与DRA的主机名重名。需要与对端OCS设备配置保持一致。该参数错误，会导致OCS连接不能建立，OCS状态异常，在线计费特性无法使用。<br>- 软参BIT150置1与否，都不允许配置两个转小写后名字相同的OCS。 |
| REALMNAME | Ocs域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN的名称，OCS所在的vpn-instance的名字，指定此OCS绑在哪个VPN上。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，参数区分大小写。<br>默认值：无<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63，255。<br>默认值：255<br>配置原则：该参数配置为255时，表示继承SET LOGIFDSCP设置的全局Gy信令DSCP值。 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UNC）每秒发送给该host所标识的OCS的最大消息数，但CCR-T消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 缺省为0，表明不控制消息数。<br>- 不配置此参数时值默认为0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCS]] · OCS（OCS）

## 使用实例

当用户网络发生变更，要增加一个OCS的实例：OCS的名称为“ocs1”，域名为“www.huawei.com”，VPN为“vpn1”：

```
ADD OCS:OCSHOSTNAME="ocs1",REALMNAME="www.huawei.com",VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OCS.md`
