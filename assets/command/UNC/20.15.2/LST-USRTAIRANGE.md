---
id: UNC@20.15.2@MMLCommand@LST USRTAIRANGE
type: MMLCommand
name: LST USRTAIRANGE（查询用户TAI区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRTAIRANGE
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
- 用户TAI区域
status: active
---

# LST USRTAIRANGE（查询用户TAI区域）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询用户TAI区域。

## 注意事项

如果不输入区域名称，表示查询系统中所有用户TAI区域。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGENAME | 区域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRTAIRANGE]] · 用户TAI区域（USRTAIRANGE）

## 使用实例

- 查询区域名称为tai1的用户TAI区域。
  ```
  LST USRTAIRANGE: RANGENAME="tai1";
  RETCODE = 0  操作成功

  结果如下
  --------
       区域名称  =  tai1
     移动国家码  =  460
     移动网络码  =  02
  TAC区域起点值  =  1234
  TAC区域结束值  =  1236
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的用户TAI区域。
  ```
  LST USRTAIRANGE:;
  RETCODE = 0  操作成功

  结果如下
  --------
       区域名称  =  tai1
     移动国家码  =  460
     移动网络码  =  02
  TAC区域起点值  =  1234
  TAC区域结束值  =  1236
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRTAIRANGE.md`
