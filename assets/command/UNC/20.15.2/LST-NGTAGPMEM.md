---
id: UNC@20.15.2@MMLCommand@LST NGTAGPMEM
type: MMLCommand
name: LST NGTAGPMEM（查询5G TA群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTAGPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN跟踪区管理
- NGRAN跟踪区群组成员管理
status: active
---

# LST NGTAGPMEM（查询5G TA群组成员）

## 功能

**适用NF：AMF**

该命令用于查询跟踪区群组成员记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区群组标识。该参数已经通过ADD NGTAGP命令中的NGTAGPID参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。“跟踪区群组标识”已经通过ADD NGTAGP配置。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G TA群组成员（NGTAGPMEM）](configobject/UNC/20.15.2/NGTAGPMEM.md)

## 使用实例

- 查询所有TA群组成员记录
  ```
  %%LST NGTAGPMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  跟踪区群组标识  跟踪区编码起始值  跟踪区编码结束值  

  1            123456     123456 
  (结果个数 = 1)

  ---    END
  ```
- 查询TA群组标识为1的群组成员记录
  ```
  、%%LST NGTAGPMEM: NGTAGPID=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
      跟踪区群组标识  =  1
    跟踪区编码起始值  =  123456
    跟踪区编码结束值  =  123456
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-TA群组成员（LST-NGTAGPMEM）_58372925.md`
