---
id: UNC@20.15.2@MMLCommand@LST CCPFOT
type: MMLCommand
name: LST CCPFOT（查询融合计费Proxy Failover模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPFOT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy Failover模板
status: active
---

# LST CCPFOT（查询融合计费Proxy Failover模板）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy Failover模板。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FOTNM | Failover模板标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| FOENABLE | 是否支持Failover开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否支持Failover开关。<br>数据来源：本端规划<br>取值范围：<br>- TRUE（TRUE）<br>- FALSE（FALSE）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CCPFOT]] · 融合计费Proxy Failover模板（CCPFOT）

## 使用实例

查询融合计费Proxy Failover模板：

```
LST CCPFOT:;
RETCODE = 0  操作成功

结果如下
--------
         Failover模板标识  =  ccpfot1
     是否支持Failover开关  =  TRUE
    FailureHandling枚举值  =  CONTINUE
     默认上行流量额度(KB)  =  2560
     默认下行流量额度(KB)  =  2560
          默认时长额度(s)  =  1800
         默认事件额度(次)  =  20
NCG代应答时的配额类型选择  =  时长额度&流量总额度
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCPFOT.md`
