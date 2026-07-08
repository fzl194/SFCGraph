---
id: UNC@20.15.2@MMLCommand@LST E2ETRCTSK
type: MMLCommand
name: LST E2ETRCTSK（查询端到端跟踪任务）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: E2ETRCTSK
command_category: 查询类
applicable_nf:
- AMF
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# LST E2ETRCTSK（查询端到端跟踪任务）

## 功能

**适用NF：AMF、MME**

该命令用于查询端到端跟踪任务。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| TRCID | 跟踪参考号 | 可选必选说明：可选参数<br>参数含义：该参数用于全局唯一标识一个跟踪任务，由MCC、MNC和Trace ID三部分组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是12~13。本参数的格式是<MCC><MNC>-<Trace ID>，其中MCC是3个十进制数字，MNC是2或3个十进制数字，Trace ID则是使用字符串表示的3字节长的十六进制数。比如MCC是123，MNC是45，Trace ID是100，那么本参数表示为12345-000064。<br>默认值：无<br>配置原则：无 |
| NGRAN | NGRAN | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| TRCINTERFACE | NGRAN接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGRAN上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “NGC（NGC）”：NGC<br>- “XNC（XN-C）”：XN-C<br>- “UU（Uu）”：Uu<br>- “F1C（F1-C）”：F1-C<br>- “E1（E1）”：E1<br>默认值：无<br>配置原则：无 |
| TRCDPTH | 跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |
| ENB | ENODEB | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB是否上报跟踪消息。<br>数据来源：全网规划<br>取值范围：<br>- “NORPT（不上报）”：不上报<br>- “RPT（上报）”：上报<br>默认值：无<br>配置原则：无 |
| ENBINTERFACE | eNodeB接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB上报跟踪消息的接口列表。<br>数据来源：全网规划<br>取值范围：<br>- “S1MME（S1-MME）”：S1-MME<br>- “X2（X2）”：X2<br>- “UU（Uu）”：Uu<br>默认值：无<br>配置原则：无 |
| ENBTRCDPTH | eNodeB跟踪深度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元上报跟踪消息的级别，值越大，级别越高。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@E2ETRCTSK]] · 端到端跟踪任务（E2ETRCTSK）

## 使用实例

- 查询所有的端到端跟踪任务，执行如下命令：
  ```
  %%LST E2ETRCTSK:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                  IMSI  =  123030912121001
            跟踪参考号  =  12345-000064
                 NGRAN  =  上报
             NGRAN接口  =  NGC&XN-C&Uu&F1-C&E1
              跟踪深度  =  1
                ENODEB  =  上报
            eNODEB接口  =  S1-MME&X2&Uu
        eNodeB跟踪深度  =  1
  跟踪任务有效时长(天)  =  1
      跟踪任务生效日期  =  2021-12-06 15:42:35
  (结果个数 = 1)

  ---    END
  ```
- 查询“IMSI”为“123030912121002”且“跟踪参考号”为“12345-000065”的端到端跟踪任务，执行如下命令：
  ```
  %%LST E2ETRCTSK: IMSI="123030912121002", TRCID="12345-000065";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                  IMSI  =  123030912121002
            跟踪参考号  =  12345-000065
                 NGRAN  =  上报
             NGRAN接口  =  NGC
              跟踪深度  =  1
                ENODEB  =  上报
            eNODEB接口  =  S1-MME
        eNodeB跟踪深度  =  1
  跟踪任务有效时长(天)  =  1
      跟踪任务生效日期  =  2021-12-06 15:42:35
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-E2ETRCTSK.md`
