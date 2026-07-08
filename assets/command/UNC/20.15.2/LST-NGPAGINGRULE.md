---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGRULE
type: MMLCommand
name: LST NGPAGINGRULE（查询5G寻呼规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGRULE
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
- NG寻呼规则管理
status: active
---

# LST NGPAGINGRULE（查询5G寻呼规则）

## 功能

**适用NF：AMF**

此命令用于查询系统中全部或者指定条件的5G寻呼规则。

## 注意事项

如果命令中的寻呼策略指示没有输入，查询结果中将以无效值255显示。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEIDX | 规则索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G寻呼规则的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGRULE]] · 5G寻呼规则（NGPAGINGRULE）

## 使用实例

- 查询所有5G寻呼规则，执行如下命令：
  ```
  %%LST NGPAGINGRULE:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          规则索引  =  6
        用户群类型  =  所有用户
          IMEI TAC  =  NULL
        MSISDN前缀  =  NULL
          IMSI前缀  =  NULL
          业务类型  =  N1N2TRANS消息
           DNN指示  =  所有DNN
      数据网络名称  =  NULL
        5G QoS标识  =  0
       ARP优先级别  =  0
      寻呼策略指示  =  255
        匹配优先级  =  50
          规则描述  =  NULL
      寻呼动作组合  =  最近访问GNB
  (结果个数 = 1)

  ---    END
  ```
- 查询一条“规则索引”为“1”的5G寻呼规则，执行如下命令：
  ```
  %%LST NGPAGINGRULE: RULEIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          规则索引  =  1
        用户群类型  =  所有用户
          IMEI TAC  =  NULL
        MSISDN前缀  =  NULL
          IMSI前缀  =  NULL
          业务类型  =  N1N2TRANS消息
           DNN指示  =  所有DNN
      数据网络名称  =  NULL
        5G QoS标识  =  0
       ARP优先级别  =  0
      寻呼策略指示  =  0
        匹配优先级  =  50
          规则描述  =  NULL
      寻呼动作组合  =  最近访问GNB
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPAGINGRULE.md`
