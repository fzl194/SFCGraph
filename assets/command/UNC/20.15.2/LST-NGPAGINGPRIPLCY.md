---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGPRIPLCY
type: MMLCommand
name: LST NGPAGINGPRIPLCY（查询5G寻呼优先级策略参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGPRIPLCY
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
- 寻呼优先级策略参数配置
status: active
---

# LST NGPAGINGPRIPLCY（查询5G寻呼优先级策略参数配置）

## 功能

**适用NF：AMF**

该命令用于查询5G寻呼优先级策略参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：可选参数<br>参数含义：该参数用于在AMF内唯一标识一条寻呼优先级策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGPRIPLCY]] · 5G寻呼优先级策略参数配置（NGPAGINGPRIPLCY）

## 使用实例

- 查询所有5G寻呼优先级策略参数，执行如下命令：
  ```
  %%LST NGPAGINGPRIPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        策略索引  =  1
    数据网络名称  =  HUAWEI.COM
       ARP优先级  =  0
  寻呼优先级等级  =  8
  (结果个数 = 1)

  ---    END
  ```
- 查询“策略索引”为2的5G寻呼优先级策略参数，执行如下命令：
  ```
  %%LST NGPAGINGPRIPLCY: PLCYIDX=2;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        策略索引  =  2
    数据网络名称  =  HUAWEI
       ARP优先级  =  0
  寻呼优先级等级  =  3
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G寻呼优先级策略参数配置（LST-NGPAGINGPRIPLCY）_09653161.md`
