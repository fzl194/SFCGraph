---
id: UNC@20.15.2@MMLCommand@LST DHCPSERVERGRP
type: MMLCommand
name: LST DHCPSERVERGRP（查询DHCP服务器组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCPSERVERGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- DHCP管理
- DHCP服务器组
status: active
---

# LST DHCPSERVERGRP（查询DHCP服务器组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询DHCP服务器组配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCP服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DHCPSERVERGRP]] · DHCP服务器组（DHCPSERVERGRP）

## 使用实例

- 查询一个DHCP服务器组的信息，GROUPNAME为testgrp：
  ```
  %%LST DHCPSERVERGRP:GROUPNAME="testgrp";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          DHCP服务器组名称  =  testgrp
                    IP类型  =  IPV4
            租约时间(小时)  =  0
  DHCP消息超时重发时间(秒)  =  3
              DHCP重发次数  =  3
                   绑定VPN  =  不使能
                 VPN实例名  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的DHCP服务器的信息：
  ```
  %%LST DHCPSERVERGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DHCP服务器组名称    IP类型    租约时间(小时)    DHCP消息超时重发时间(秒)    DHCP重发次数    绑定VPN    VPN实例名

  testgrp             IPV4      0                 3                           3               不使能     NULL     
  testgrp2            IPV4      0                 3                           3               不使能     NULL     
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DHCPSERVERGRP.md`
