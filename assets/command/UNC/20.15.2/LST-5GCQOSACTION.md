---
id: UNC@20.15.2@MMLCommand@LST 5GCQOSACTION
type: MMLCommand
name: LST 5GCQOSACTION（查询5GC QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: 5GCQOSACTION
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC QoS控制动作
status: active
---

# LST 5GCQOSACTION（查询5GC QoS控制动作配置）

## 功能

**适用NF：SMF**

该命令用于查询5G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

- 当5QI值配置为GBR 5QI时，带宽参数才会生效，GBR 5QI取值参考协议23501以及STDQOSID配置。
- 带宽取值为0时，表示无效值。
- 上行保证带宽不能大于上行最大带宽。
- 下行保证带宽不能大于下行最大带宽。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/5GCQOSACTION]] · 5GC QoS控制动作配置（5GCQOSACTION）

## 使用实例

- 查询给定QoS Profile名称对应的5GC QoS Action配置：
  ```
  %%LST 5GCQOSACTION: QOSPROFILENAME="test";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
            QoS Profile名称  =  test
                    5QI值  =  2
  下行保证带宽(千比特/秒)  =  0
  上行保证带宽(千比特/秒)  =  0
  下行最大带宽(千比特/秒)  =  0
  上行最大带宽(千比特/秒)  =  0
       超过下行GFBR的处理  =  降级
       超过上行GFBR的处理  =  降级
       超过下行MFBR的处理  =  降级
       超过上行MFBR的处理  =  降级
  (结果个数 = 1)

  ---    END
  ```
- 查询所有5GC QoS Action配置：
  ```
  %%LST 5GCQOSACTION:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  QoS Profile名  5QI值  下行保证带宽(千比特/秒)  上行保证带宽(千比特/秒)  下行最大带宽(千比特/秒)  上行最大带宽(千比特/秒)  超过下行GFBR的处理  超过上行GFBR的处理  超过下行MFBR的处理  超过上行MFBR的处理  

  globalqos      4      0                        0                        0                        0                        降级                降级                降级                降级                
  test           2      0                        0                        0                        0                        降级                降级                降级                降级                
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5GC-QoS控制动作配置（LST-5GCQOSACTION）_09652147.md`
