---
id: UDG@20.15.2@MMLCommand@DSP ICAPSVRGSTATUS
type: MMLCommand
name: DSP ICAPSVRGSTATUS（查询ICAP服务器组状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ICAPSVRGSTATUS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器组
status: active
---

# DSP ICAPSVRGSTATUS（查询ICAP服务器组状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示所有已经配置的ICAP Server Group或者指定名字的ICAP Server Group的工作状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ICAP服务器组状态（ICAPSVRGSTATUS）](configobject/UDG/20.15.2/ICAPSVRGSTATUS.md)

## 使用实例

- 查询所有已经配置的ICAP Server Group的工作状态信息：
  ```
  DSP ICAPSVRGSTATUS:;
  ```
  ```

  RETCODE = 0 操作成功

  ICAP服务器组状态
  ------------------------
  ICAP服务器组名称  Pod名称      ICAP服务器组状态  

  isg1              icapc-pod-0  Abnormal          
  isg2              icapc-pod-0  Abnormal          
  (结果个数 = 2)

  ---    END
  ```
- 查询指定名字的ICAP Server Group的状态信息：
  ```
  DSP ICAPSVRGSTATUS: ICAPSVRGRPNAME="isg1";
  ```
  ```

  RETCODE = 0 操作成功

  ICAP服务器组状态
  ------------------------
  ICAP服务器组名称  =  isg1
           Pod名称  =  icapc-pod-0
  ICAP服务器组状态  =  Abnormal
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ICAP服务器组状态（DSP-ICAPSVRGSTATUS）_28511770.md`
