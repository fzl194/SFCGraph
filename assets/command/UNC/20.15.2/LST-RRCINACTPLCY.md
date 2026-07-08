---
id: UNC@20.15.2@MMLCommand@LST RRCINACTPLCY
type: MMLCommand
name: LST RRCINACTPLCY（查询RRC Inactive策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RRCINACTPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- RRC Inactive业务管理
- RRC Inactive策略
status: active
---

# LST RRCINACTPLCY（查询RRC Inactive策略）

## 功能

**适用NF：AMF**

该命令用于查询RRC Inactive功能的开启策略，若查询无结果表示所有用户均开启RRC Inactive功能，若查询有结果则表示对应结果的用户开启RRC Inactive功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIBEGN | IMSI起始号段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>若期望下发基于指定IMSI前缀的号段匹配策略，需要用十进制数字"0"和"9"分别补齐IMSIBEGN和IMSIEND的剩余长度。 |

## 操作的配置对象

- [RRC Inactive策略（RRCINACTPLCY）](configobject/UNC/20.15.2/RRCINACTPLCY.md)

## 使用实例

- 查询开启RRC Inactive功能的IMSI范围以及其他附加条件，执行如下命令：
  ```
  %%LST RRCINACTPLCY:;%%
  RETCODE = 0  操作成功
 
  输出结果如下
  --------------
              IMSI起始号段  =  123450000000000
              IMSI结束号段  =  123450000000000
  其他RRC Inactive开启条件  =  无效
                  描述信息  =  NULL
  (结果个数 = 1)
 
  ---    END
  ```
- 查询IMSI起始号段为“123450000000000”的RRC Inactive策略，执行如下命令：
  ```
  %%LST RRCINACTPLCY: IMSIBEGN="123450000000000";%%
  RETCODE = 0  操作成功
 
  输出结果如下
  --------------
              IMSI起始号段  =  123450000000000
              IMSI结束号段  =  123450000000000
  其他RRC Inactive开启条件  =  无效
                  描述信息  =  NULL
  (结果个数 = 1)
 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RRC-Inactive策略（LST-RRCINACTPLCY）_70382337.md`
