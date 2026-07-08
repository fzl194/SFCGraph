---
id: UDG@20.15.2@MMLCommand@LST BGPPEER
type: MMLCommand
name: LST BGPPEER（查询BGP对等体）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BGPPEER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体
status: active
---

# LST BGPPEER（查询BGP对等体）

## 功能

该命令用于查看IPv4或IPv6地址类型的对等体的相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| ADDRESSTYPE | 地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体的地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- noaf：不指定地址族。<br>- ipv4：IPv4。<br>- ipv6：IPv6。<br>默认值：无 |
| PEERADDR | IPv4对等体地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“noaf” 或 “ipv4”时为可选参数。<br>参数含义：该参数用于指定连接对等体的IPv4接口地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| PEERADDRV6 | IPv6对等体地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为可选参数。<br>参数含义：该参数用于指定连接对等体的IPv6接口地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [BGP对等体（BGPPEER）](configobject/UDG/20.15.2/BGPPEER.md)

## 使用实例

- 查看名称为“vrf1”的BGP VPN实例下IPv4地址类型的对等体的相关参数：
  ```
  LST BGPPEER: VRFNAME="vrf1",ADDRESSTYPE=ipv4,PEERADDR="10.2.2.2";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                           VPN实例名称  =  vrf1
                              地址类型  =  IPv4
                        IPv4对等体地址  =  10.2.2.2
                        IPv6对等体地址  =  ::
                            对等体AS号  =  100
                                  组名  =  NULL
                              路由刷新  =  TRUE
                         4字节AS号功能  =  TRUE
                            常规路由器  =  FALSE
                          本地接口地址  =  NULL
                          本地接口名称  =  NULL
                          EBGP最大跳数  =  NULL
                    需要检测的TTL跳数值  =  NULL
                                伪AS号  =  NULL
                              是否忽略  =  FALSE
                              连接模式  =  NULL
                          是否记录日志  =  TRUE
                              密码类型  =  NULL
                                  密码  =  NULL
                         存活时间（s）  =  60
                         保持时间（s）  =  180
                          Keychain名称  =  NULL
                       路径MTU发现功能  =  FALSE
                                  描述  =  NULL
  使能快速感知邻居不可达并断开连接功能  =  FALSE
                 邻居断连延迟时间（s）  =  0
                         重连时间（s）  =  32
  (结果个数 = 1)
  ---    END
  ```
- 查看名称为“vrf1”的BGP VPN实例下IPv6地址类型的对等体的相关参数：
  ```
  LST BGPPEER: VRFNAME="vrf1",ADDRESSTYPE=ipv6,PEERADDRV6="2001:db8:1:1:1:1:1:1";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
                           VPN实例名称  =  vrf1
                              地址类型  =  IPv6
                        IPv4对等体地址  =  0.0.0.0
                        IPv6对等体地址  =  2001:db8:1:1:1:1:1:1
                            对等体AS号  =  100
                                  组名  =  NULL
                              路由刷新  =  TRUE
                         4字节AS号功能  =  TRUE
                            常规路由器  =  FALSE
                          本地接口地址  =  NULL
                          本地接口名称  =  NULL
                          EBGP最大跳数  =  NULL
               指定需要检测的TTL跳数值  =  NULL
                                伪AS号  =  NULL
                              是否忽略  =  FALSE
                              连接模式  =  NULL
                          是否记录日志  =  TRUE
                              密码类型  =  NULL
                                  密码  =  NULL
                         存活时间（s）  =  60
                         保持时间（s）  =  180
                          Keychain名称  =  NULL
                       路径MTU发现功能  =  FALSE
                                  描述  =  NULL
  使能快速感知邻居不可达并断开连接功能  =  FALSE
                 邻居断连延迟时间（s）  =  0
                         重连时间（s）  =  32
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BGP对等体（LST-BGPPEER）_50120942.md`
