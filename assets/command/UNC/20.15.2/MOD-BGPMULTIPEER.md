---
id: UNC@20.15.2@MMLCommand@MOD BGPMULTIPEER
type: MMLCommand
name: MOD BGPMULTIPEER（修改BGP多源对等体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: BGPMULTIPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP多源对等体
status: active
---

# MOD BGPMULTIPEER（修改BGP多源对等体）

## 功能

该命令用于更新BGP多源对等体参数。

## 注意事项

- 该命令执行后立即生效。
- 如果将是否忽略设置为是，将导致该BGP多源对等体断连。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| PEERADDR | 对等体地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定建立对等体的接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCEIFNAME | 源接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定建立对等体的源接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：不区分大小写。 |
| ISIGNORE | 是否忽略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否忽略与指定对等体建立会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：一旦配置为TRUE，会中断邻居，且以后再也无法建立连接，BGP对等体状态显示为Idle。 |

## 操作的配置对象

- [BGP多源对等体（BGPMULTIPEER）](configobject/UNC/20.15.2/BGPMULTIPEER.md)

## 使用实例

在名称为“vrf1”的BGP VPN实例下修改对等体10.2.2.2是否忽略连接：

```
MOD BGPMULTIPEER:VRFNAME="vrf1",PEERADDR="10.2.2.2",SOURCEIFNAME="Ethernet66/0/3",ISIGNORE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改BGP多源对等体（MOD-BGPMULTIPEER）_49961406.md`
