---
id: UNC@20.15.2@MMLCommand@LST DHCPBINDPOOLGRP
type: MMLCommand
name: LST DHCPBINDPOOLGRP（查询DHCP服务器组与地址池组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCPBINDPOOLGRP
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
- DHCP服务器绑定
status: active
---

# LST DHCPBINDPOOLGRP（查询DHCP服务器组与地址池组绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询DHCP服务器组与地址池组的关联。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOLGRP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPBINDPOOLGRP]] · DHCP服务器组与地址池组绑定关系（DHCPBINDPOOLGRP）

## 使用实例

- 当需要查看远端地址池组与DHCP服务器组的绑定关系时，使用该命令：
  ```
  %%LST DHCPBINDPOOLGRP:POOLGRPNAME="poolgrp1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
      地址池组名称  =  poolgrp1
  DHCP服务器组名称  =  group1
  (结果个数 = 1)

  ---    END
  ```
- 当需要查看所有远端地址池组和DHCP服务器的绑定关系时，使用该命令：
  ```
  %%LST DHCPBINDPOOLGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  地址池组名称       DHCP服务器组名称

  poolgrp1           group1         
  poolgrp2           group2         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DHCP服务器组与地址池组绑定关系（LST-DHCPBINDPOOLGRP）_32102615.md`
