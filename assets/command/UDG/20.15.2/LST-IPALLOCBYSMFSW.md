---
id: UDG@20.15.2@MMLCommand@LST IPALLOCBYSMFSW
type: MMLCommand
name: LST IPALLOCBYSMFSW（显示基于SMF分配地址开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYSMFSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 基于SMF分配地址开关
status: active
---

# LST IPALLOCBYSMFSW（显示基于SMF分配地址开关）

## 功能

**适用NF：PGW-U、UPF**

该命令显示指定SMF实例或所有的基于SMF分配地址的开关信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令指定SMF实例名时，表示查询指定SMF实例的基于SMF分配地址的开关。不指定SMF实例名时，表示查询所有的基于SMF分配地址的开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMF | SMF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPALLOCBYSMFSW]] · 基于SMF分配地址开关（IPALLOCBYSMFSW）

## 使用实例

- 查询名为smfnode1的SMF实例基于SMF分配地址开关的信息：
  ```
  LST IPALLOCBYSMFSW: SMF="smfnode1";
  ```
  ```

  RETCODE = 0 操作成功。

  基于SMF分配地址开关
  -----------------------------------
  SMF名称 = smfnode1
  IPv4开关 = 不使能
  IPv6开关 = 不使能
  (结果个数 = 1)
  --- END
  ```
- 查询所有SMF实例基于SMF分配地址开关的信息：
  ```
  LST IPALLOCBYSMFSW:;
  ```
  ```

  RETCODE = 0 操作成功。

  基于SMF分配地址开关
  -----------------------------------
  SMF名称 IPv4开关 IPv6开关

  smfnode1 不使能 不使能
  smfnode2 使能 使能
  smfnode3 继承 继承
  (结果个数 = 3)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基于SMF分配地址开关（LST-IPALLOCBYSMFSW）_82837156.md`
