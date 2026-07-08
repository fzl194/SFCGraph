---
id: UNC@20.15.2@MMLCommand@DSP LBPLY
type: MMLCommand
name: DSP LBPLY（查询负载均衡策略）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBPLY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 策略调测
- 负载均衡策略
status: active
---

# DSP LBPLY（查询负载均衡策略）

## 功能

查询负载均衡策略的详细信息。

## 注意事项

- 单次查询最多显示1000条，并支持分页显示。如果负载均衡策略超过1000条，那么查询结果会提示“报文只包含部分查询结果”。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的策略类型。<br>数据来源：对端协商<br>默认值：无<br>取值范围：<br>- “SRV_PLY_TYPE_NORMAL(标准类型) ”<br>- “SRV_PLY_TYPE_EXTEND(扩展类型) ” |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODEID即为服务VNFC ID。对于微服务，该参数用于指定服务ID，可通过OPR DBGDATA命令查询，输入参数“DEBUGNAME”取值为“DSP PREFIX”，输出中的第二列为服务ID。<br>数据来源：全网规划<br>默认值：无 |
| PLYID | 策略ID | 可选必选说明：必选参数<br>参数含义：业务VNFC下发的策略号。<br>数据来源：可通过执行<br>**[DSP POLICYNUM](../../../../业务管理/服务管理/策略/查询策略数量（DSP POLICYNUM）_29627053.md)**<br>查询到。<br>默认值：无 |
| KEY1 | 关键字1 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字1。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY2 | 关键字2 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字2。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY3 | 关键字3 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字3。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY4 | 关键字4 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字4。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY5 | 关键字5 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字5。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY6 | 关键字6 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字6。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY7 | 关键字7 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字7。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |
| KEY8 | 关键字8 | 可选必选说明：可选参数<br>参数含义：业务VNFC下发的策略关键字8。<br>数据来源：对端协商<br>默认值：无<br>取值范围：0~63字符 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBPLY]] · 负载均衡策略（LBPLY）

## 使用实例

查询所有服务VNFC ID为4，策略ID为0的负载均衡策略的详细信息：

DSP LBPLY: PLYTYPE=SRV_PLY_TYPE_NORMAL, CONSUMERVNFCID=4, PLYID=0;

```
%%DSP LBPLY: PLYTYPE=SRV_PLY_TYPE_NORMAL, CONSUMERVNFCID=4, PLYID=0;%%
RETCODE = 0  操作成功

结果如下:
-------------------------
策略类型    服务VNFC ID    策略ID    关键字1     关键字2    关键字3    关键字4    关键字5    关键字6    关键字7    关键字8    动作类型    参数1    参数2    参数3    参数4    参数5    参数6    透明数据长度    透明数据 
标准类型    4              0         31313131    31         3131       NULL       NULL       NULL       NULL       NULL       41          42       43       0        0       0        0        0        NULL     
标准类型    4              0         31303130    31         3031       NULL       NULL       NULL       NULL       NULL       11          12       13       0        0       0        0        0        NULL     
标准类型    4              0         32323232    32         3232       NULL       NULL       NULL       NULL       NULL       21          22       23       0        0       0        0        0        NULL     
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBPLY.md`
