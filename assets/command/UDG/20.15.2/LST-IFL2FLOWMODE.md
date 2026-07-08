---
id: UDG@20.15.2@MMLCommand@LST IFL2FLOWMODE
type: MMLCommand
name: LST IFL2FLOWMODE（查询主接口二层透传模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFL2FLOWMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 流模式配置
status: active
---

# LST IFL2FLOWMODE（查询主接口二层透传模式）

## 功能

该命令用来查询接口的二层透传模式。在不指定接口名时，查询所有使能了二层透传模式的主接口；指定接口名时，只查询该接口的二层透传模式是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IFL2FLOWMODE]] · 主接口二层透传模式（IFL2FLOWMODE）

## 使用实例

- 查询指定主接口下的二层透传模式：
  ```
  LST IFL2FLOWMODE:IFNAME="Ethernet65/0/6";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------
    接口名称  =  Ethernet65/0/6
  流模式使能  =  TRUE
  (结果个数 = 1)
  ---    END
  ```
- 查询所有主接口下的二层透传模式：
  ```
  LST IFL2FLOWMODE:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  接口名称          流模式使能 

  Ethernet66/0/4    TRUE             
  Ethernet66/0/5    TRUE             
  Ethernet65/0/6    TRUE             
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IFL2FLOWMODE.md`
