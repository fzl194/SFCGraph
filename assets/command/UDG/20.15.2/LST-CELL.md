---
id: UDG@20.15.2@MMLCommand@LST CELL
type: MMLCommand
name: LST CELL（查询小区）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CELL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- 小区配置
status: active
---

# LST CELL（查询小区）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询小区信息。当运营商希望查询小区信息时，则执行该命令。

## 注意事项

如果不输入小区名称，表示查询系统中所有小区信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLNAME | 小区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置小区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELL]] · 小区（CELL）

## 使用实例

- 假如运营商需要查询位置名称为test_cell_1的小区：
  ```
  LST CELL: CELLNAME="test_cell_1";
  ```
  ```

  RETCODE = 0 操作成功。

  小区信息
  --------
  小区名称 = test_cell_1
  小区ID = 123456789
  (结果个数 = 1)
  --- END
  ```
- 假如运营商需要查询所有的位置信息：
  ```
  LST CELL:;
  ```
  ```

  RETCODE = 0 操作成功。

  小区信息
  --------
  小区名称    小区ID
  test_cell_1 123456789
  test_cell_2 1234567890
  (结果个数 = 2)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询小区（LST-CELL）_86616994.md`
