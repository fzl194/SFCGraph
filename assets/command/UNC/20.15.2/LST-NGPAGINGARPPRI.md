---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGARPPRI
type: MMLCommand
name: LST NGPAGINGARPPRI（查询基于ARP的Paging消息在流控期间放通的优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGARPPRI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口消息流控优先级管理
- 基于ARP的Paging消息流控优先级管理
status: active
---

# LST NGPAGINGARPPRI（查询基于ARP的Paging消息在流控期间放通的优先级）

## 功能

**适用NF：AMF**

该命令用于查询基于ARP的Paging消息在流控期间放通的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ARP | ARP数值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGARPPRI]] · 基于ARP的Paging消息在流控期间放通的优先级（NGPAGINGARPPRI）

## 使用实例

查询基于ARP的Paging消息在流控期间放通的优先级，执行如下命令：

```
%%LST NGPAGINGARPPRI:;%%
RETCODE = 0  操作成功

结果如下
--------
ARP数值  优先级                 

1        高  
2        高  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPAGINGARPPRI.md`
