---
id: UNC@20.15.2@MMLCommand@LST NGIPAREAGRPMEM
type: MMLCommand
name: LST NGIPAREAGRPMEM（查询5G IP区域群成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIPAREAGRPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G IP细分区域组成员管理
status: active
---

# LST NGIPAREAGRPMEM（查询5G IP区域群成员）

## 功能

**适用NF：AMF**

该命令用于查询5G IP区域群成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域群标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。此AREAID要与NGIPAREAGRP中的AREAID保持一致，受NGIPAREAGRP中的IPAREASW开关控制；。<br>默认值：无<br>配置原则：无 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREAGRPMEM]] · 5G IP区域群成员（NGIPAREAGRPMEM）

## 使用实例

- 查询5G全部区域群成员的信息，执行如下命令：
  ```
  %%LST NGIPAREAGRPMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  区域群标识  跟踪区域码  跟踪区域结束值  描述信息  

  1           010101      010103          tac010101   
  SomeCity    010104      010106          tac010102   
  (结果个数 = 2)

  ---    END
  ```
- 查询区域群标识为SomeCity的区域群成员记录，执行如下命令：
  ```
  %%LST NGIPAREAGRPMEM: AREAID="SomeCity";%%
  RETCODE = 0  操作成功

  结果如下
  --------
      区域群标识  =  SomeCity
      跟踪区域码  =  010102
  跟踪区域结束值  =  010103
        描述信息  =  tac010102
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-IP区域群成员（LST-NGIPAREAGRPMEM）_09654417.md`
