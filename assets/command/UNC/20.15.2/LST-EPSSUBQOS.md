---
id: UNC@20.15.2@MMLCommand@LST EPSSUBQOS
type: MMLCommand
name: LST EPSSUBQOS（查询EPS签约QoS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPSSUBQOS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 本地EPS QoS
status: active
---

# LST EPSSUBQOS（查询EPS签约QoS配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来查询用户的签约QoS属性。

## 注意事项

当不输入参数时，系统查询所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：可选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [EPS签约QoS配置（EPSSUBQOS）](configobject/UNC/20.15.2/EPSSUBQOS.md)

## 使用实例

- 查询“SUBQOSINDEX”为“123”的记录：
  ```
  %%LST EPSSUBQOS: SUBQOSINDEX=123;%%
  RETCODE = 0  操作成功

  EPS用户QoS配置信息
  ------------------
               用户QoS索引  =  123
                   标准QCI  =  5
             ARP的优先级别  =  10
  下行APN AMBRR(千比特/秒)  =  564110
  上行APN AMBRR(千比特/秒)  =  300000
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的记录：
  ```
  %%LST EPSSUBQOS:;%%
  RETCODE = 0  操作成功

  EPS用户QoS配置信息
  ------------------
  用户QoS索引    标准QCI    ARP的优先级别    下行APN AMBRR(千比特/秒)    上行APN AMBRR(千比特/秒)

  1              5          1                2                             5                         
  123            5          10               564110                        300000                    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS签约QoS配置（LST-EPSSUBQOS）_09651639.md`
