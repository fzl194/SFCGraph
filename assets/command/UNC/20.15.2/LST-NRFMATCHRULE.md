---
id: UNC@20.15.2@MMLCommand@LST NRFMATCHRULE
type: MMLCommand
name: LST NRFMATCHRULE（查询服务发现最长匹配处理规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFMATCHRULE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现最长匹配规则
status: active
---

# LST NRFMATCHRULE（查询服务发现最长匹配处理规则）

## 功能

**适用NF：NRF**

该命令用于查询服务发现最长匹配规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF服务发现的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- SMF（SMF ）<br>- BSF（BSF）<br>- UDR（UDR）<br>- UDM（UDM）<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFMATCHRULE]] · 服务发现最长匹配处理规则（NRFMATCHRULE）

## 使用实例

查询服务发现最长匹配规则。

```
LST NRFMATCHRULE:;
%%LST NRFMATCHRULE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
网元类型      匹配开关  

UDM           关闭      
AMF           关闭      
SMF           关闭      
AUSF          关闭      
PCF           关闭      
UDR           关闭      
BSF           关闭      
CHF           关闭      
CUSTOM_OCS    关闭      
SMSF          关闭      
NWDAF         关闭      
(结果个数 = 11)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFMATCHRULE.md`
