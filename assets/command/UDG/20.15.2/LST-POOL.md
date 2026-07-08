---
id: UDG@20.15.2@MMLCommand@LST POOL
type: MMLCommand
name: LST POOL（显示地址池）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: POOL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池配置
status: active
---

# LST POOL（显示地址池）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示所有地址池或指定地址池的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POOL]] · 地址池（POOL）

## 使用实例

- 查询地址池lap的信息，PoolName为lap：
  ```
  LST POOL:POOLNAME="lap";
  ```
  ```

  RETCODE = 0 操作成功。

  地址池信息
  ----------
  地址池名称 = lap
  IP地址类型 = IPV4
  地址租约使能标志 = 不使能
  地址租期（秒） = 10
  小地址池标志 = 不使能
  检查静态地址的合法性 = 不使能
  绑定VPN = 不使能
  VPN实例名 = NULL
  告警特性是否使能 = 不使能
  地址池锁定标志 = 不锁定
  IMS开关 = 使能
  地址池类型 = POOL_LOCAL
  冗余备份功能开关 = 不使能
  (结果个数 = 1)

  --- END
  ```
- 查询所有的地址池信息：
  ```
  LST POOL:;
  ```
  ```

  RETCODE = 0 操作成功。

  地址池信息
  ----------------
  地址池名称 IP地址类型 地址租约使能标志 地址租期（秒） 小地址池标志 检查静态地址的合法性 绑定VPN VPN实例名 告警特性是否使能 地址池锁定标志 IMS开关 地址池类型 冗余备份功能开关

  lap IPV4 不使能 10 不使能 不使能 不使能 NULL 不使能 不锁定 使能 POOL_LOCAL 不使能
  pool1 IPV4 不使能 10 不使能 不使能 不使能 NULL 不使能 不锁定 使能 POOL_EXTERNAL 不使能
  pool2 IPV4 不使能 10 不使能 不使能 不使能 NULL 不使能 不锁定 使能 POOL_LOCAL 不使能
  (Number of results = 3)

  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示地址池（LST-POOL）_82837135.md`
