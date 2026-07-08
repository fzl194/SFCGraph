---
id: UNC@20.15.2@MMLCommand@LST NGAPPARA
type: MMLCommand
name: LST NGAPPARA（查询NGAP协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAPPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP协议参数管理
status: active
---

# LST NGAPPARA（查询NGAP协议参数）

## 功能

**适用NF：AMF**

该命令用于显示NGAP协议参数配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPPARAIDX | NGAP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGAPPARA]] · NGAP协议参数（NGAPPARA）

## 使用实例

- 查询系统中当前配置的NGAP接口协议控制参数，执行如下命令：
  ```
  %%LST NGAPPARA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NGAP协议参数索引  AMF Configuration Update消息超时定时器(s)  AMF Configuration Update消息重发次数 (times)  Reset超时定时器(s)  Reset消息重发次数 (times)  重发NG SETUP REQUEST时长 (s)  等待时间指示器  

  0                 20                                         3                                             20                  3                          60                            否              
  1                 32                                         3                                             22                  3                          20                            否              
  (结果个数 = 2)

  ---    END
  ```
- 查询NGAPPARAIDX为1的当前配置的NGAP接口协议控制参数，执行如下命令：
  ```
  %%LST NGAPPARA: NGAPPARAIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                              NGAP协议参数索引  =  1
     AMF Configuration Update消息超时定时器(s)  =  32
  AMF Configuration Update消息重发次数 (times)  =  3
                            Reset超时定时器(s)  =  22
                     Reset消息重发次数 (times)  =  3
                  重发NG SETUP REQUEST时长 (s)  =  20
                                等待时间指示器  =  否
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGAPPARA.md`
