---
id: UDG@20.15.2@MMLCommand@DSP PIMROUTEUP
type: MMLCommand
name: DSP PIMROUTEUP（查询PIM表项上游信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PIMROUTEUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM路由表信息
status: active
---

# DSP PIMROUTEUP（查询PIM表项上游信息）

## 功能

该命令用于显示PIM表项上游信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| SRCADDR | 源地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用于表示源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| GRPADDR | 组地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用于表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PIMROUTEUP]] · PIM表项上游信息（PIMROUTEUP）

## 使用实例

显示PIM表项上游信息：

```
DSP PIMROUTEUP: VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,SRCADDR="10.1.1.2",GRPADDR="239.0.0.1";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                  VPN实例名称  =  _public_
                       地址族  =  IPv4单播
                       源地址  =  10.1.1.2
                       组地址  =  239.0.0.1
                 上游协议类型  =  ASM模式
                       RP类型  =  其他类型
                       RP地址  =  10.0.0.1
                   RP本地标记  =  FALSE
                     表项标记  =  SPT NIIF SG_RCVR
                 表项存活时间  =  00:00:30
                       入接口  =  NULL
                 上游邻居地址  =  0.0.0.0
                      RPF地址  =  0.0.0.0
                 上游加入状态  =  非加入状态
             上游加入超时时间  =  00:00:00
                  上游RPT状态  =  非加入状态
              上游RPT否决时间  =  00:00:00
                     注册状态  =  无状态
                 注册停止时间  =  00:00:00
   抑制发送剪枝报文的超时时间  =  00:00:00
     剪枝否决定时器的超时时间  =  00:00:00
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PIMROUTEUP.md`
