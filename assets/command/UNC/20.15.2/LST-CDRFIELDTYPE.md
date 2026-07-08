---
id: UNC@20.15.2@MMLCommand@LST CDRFIELDTYPE
type: MMLCommand
name: LST CDRFIELDTYPE（查询字段映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRFIELDTYPE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF计费字段映射规则
status: active
---

# LST CDRFIELDTYPE（查询字段映射关系）

## 功能

**适用NF：NCG**

该命令用于查询字段映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FIELDNAME | 字段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字段名称。<br>数据来源：本端规划<br>取值范围：<br>- RATTYPE（RAT类型）<br>- SSCMODE（SSC模式）<br>- PDUSESSIONTYPE（PDU会话类型）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRFIELDTYPE]] · 字段映射关系（CDRFIELDTYPE）

## 使用实例

查询字段映射关系：

```
%%LST CDRFIELDTYPE:;%%
RETCODE = 0  操作成功

结果如下
--------
字段名称     RAT类型名称                                 SSC类型名称  PDU类型名称   类型取值  

RAT类型      New Radio                                   SSCMode 1    IPv4          51        
RAT类型      Evolved Universal Terrestrial Radio Access  SSCMode 1    IPv4          6         
RAT类型      Wireless LAN                                SSCMode 1    IPv4          3         
RAT类型      Virtual                                     SSCMode 1    IPv4          7         
RAT类型      GERA                                        SSCMode 1    IPv4          2         
RAT类型      NB IoT                                      SSCMode 1    IPv4          8         
RAT类型      LTE-M                                       SSCMode 1    IPv4          9         
RAT类型      UTRA                                        SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 2    IPv4          2         
SSC模式      New Radio                                   SSCMode 3    IPv4          3         
PDU会话类型  New Radio                                   SSCMode 1    IPv4          1         
PDU会话类型  New Radio                                   SSCMode 1    IPv6          2         
PDU会话类型  New Radio                                   SSCMode 1    IPv4v6        0         
PDU会话类型  New Radio                                   SSCMode 1    Unstructured  3         
PDU会话类型  New Radio                                   SSCMode 1    Ethernet      4         
PDU会话类型  New Radio                                   SSCMode 1    Non-IP        50
RAT类型      NR_REDCAP                                   SSCMode 1    IPv4          58
(结果个数 = 18)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询字段映射关系（LST-CDRFIELDTYPE）_45110920.md`
