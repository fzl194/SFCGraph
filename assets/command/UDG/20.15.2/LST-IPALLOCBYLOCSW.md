---
id: UDG@20.15.2@MMLCommand@LST IPALLOCBYLOCSW
type: MMLCommand
name: LST IPALLOCBYLOCSW（显示基于位置区分配地址的开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYLOCSW
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
- 基于位置区分配地址开关
status: active
---

# LST IPALLOCBYLOCSW（显示基于位置区分配地址的开关）

## 功能

**适用NF：PGW-U、UPF**

该命令显示指定位置区组或所有的基于位置区分配地址的开关信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令指定位置区组类型和名称时，表示查询指定位置区组基于位置区分配地址的开关信息。指定位置区组的类型而不指定名称时，表示查询指定类型位置区组基于位置区分配地址的开关信息。不指定位置区组的类型和名称时，表示查询所有基于位置区组分配地址的开关信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：枚举类型。只能选取一个选项。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPALLOCBYLOCSW]] · 基于位置区分配地址的开关（IPALLOCBYLOCSW）

## 使用实例

- 查询名为tac1的TAC-GROUP基于位置区分配地址的开关信息：
  ```
  LST IPALLOCBYLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tac1";
  ```
  ```

  RETCODE = 0 操作成功。

  基于位置区分配地址的开关
  ----------------------------------------
  位置区组类型 = TAC
  IPv4开关 = 不使能
  IPv6开关 = 不使能
  位置区组名称 = tac1
  (结果个数 = 1)
  --- END
  ```
- 查询所有LAC-GROUP基于位置区分配地址的开关信息：
  ```
  LST IPALLOCBYLOCSW: LOCATIONGRPTYPE=LAC;
  ```
  ```

  RETCODE = 0 操作成功。

  基于位置区分配地址的开关
  ----------------------------------------
  位置区组类型 开关 位置区组名称

  LAC 使能 lac1
  LAC 不使能 lac2
  LAC 继承 lac3
  (结果个数 = 3)
  --- END
  ```
- 查询所有的基于位置区分配地址的开关信息：
  ```
  LST IPALLOCBYLOCSW:;
  ```
  ```

  RETCODE = 0 操作成功。

  基于位置区分配地址的开关
  ----------------------------------------
  位置区组类型 IPv4开关 IPv6开关 位置区组名称

  LAC 使能 使能 lac1
  LAC 不使能 不使能 lac2
  LAC 继承 继承 lac3
  TAC 不使能 不使能 tac1
  TAC 继承 继承 tac2
  TAC 使能 使能 tac3
  TAC 继承 继承 tac4
  TAC 继承 继承 tac5
  (结果个数 = 8)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPALLOCBYLOCSW.md`
