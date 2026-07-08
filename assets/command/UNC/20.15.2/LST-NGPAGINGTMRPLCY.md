---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGTMRPLCY
type: MMLCommand
name: LST NGPAGINGTMRPLCY（查询5G寻呼定时器策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGTMRPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼定时器策略管理
status: active
---

# LST NGPAGINGTMRPLCY（查询5G寻呼定时器策略配置）

## 功能

**适用NF：AMF**

该命令用于查看NG寻呼定时器策略配置数据。

## 注意事项

如果命令中的寻呼策略指示没有输入，查询结果中将以无效值255显示。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：可选参数<br>参数含义：该参数用于在AMF中唯一标识一条寻呼定时器策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGTMRPLCY]] · 5G寻呼定时器策略配置（NGPAGINGTMRPLCY）

## 使用实例

- 查询所有NG寻呼定时器策略配置，执行如下命令：
  ```
  %%LST NGPAGINGTMRPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
             策略索引  =  2
         数据网络名称  =  HUAWEI.COM
           5G QoS标识  =  0
          ARP优先级别  =  0
         寻呼策略指示  =  3
             T3513(s)  =  4
         N3513(times)  =  1
  重寻呼间隔递增值(s)  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询一条“策略索引”为“1”的NG寻呼定时器策略配置，执行如下命令：
  ```
  %%LST NGPAGINGTMRPLCY: PLCYIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
             策略索引  =  1
         数据网络名称  =  HUAWEI
           5G QoS标识  =  0
          ARP优先级别  =  0
         寻呼策略指示  =  255
             T3513(s)  =  5
         N3513(times)  =  1
  重寻呼间隔递增值(s)  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPAGINGTMRPLCY.md`
