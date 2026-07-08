---
id: UNC@20.15.2@MMLCommand@LST PCFSSCOPE
type: MMLCommand
name: LST PCFSSCOPE（查询PCF的业务服务区）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCFSSCOPE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区
status: active
---

# LST PCFSSCOPE（查询PCF的业务服务区）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询PCF的业务服务区。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSCOPEID | 服务区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PCF的业务服务区（PCFSSCOPE）](configobject/UNC/20.15.2/PCFSSCOPE.md)

## 使用实例

- 查询服务区标识为citya的PCF业务服务区。
  ```
  LST PCFSSCOPE:SSCOPEID="citya";
  RETCODE = 0  操作成功

  结果如下
  --------
  服务区标识  =  citya
  服务区名称  =  City_A
  (结果个数 = 1)

  ---    END
  ```
- 查询所有PCF业务服务区。
  ```
  LST PCFSSCOPE:;
  RETCODE = 0  操作成功

  结果如下
  --------
  服务区标识  =  citya
  服务区名称  =  City_A
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCF的业务服务区（LST-PCFSSCOPE）_35273623.md`
