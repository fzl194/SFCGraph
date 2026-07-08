---
id: UNC@20.15.2@MMLCommand@LST QCI2ARP
type: MMLCommand
name: LST QCI2ARP（查询标准QCI到ARP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QCI2ARP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QCI到ARP映射
status: active
---

# LST QCI2ARP（查询标准QCI到ARP的映射规则）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询ARP和标准QCI的对应关系，从而通过标准QCI来对应出相应的承载ARP取值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/QCI2ARP]] · 标准QCI到ARP的映射规则（QCI2ARP）

## 使用实例

查询ARP和标准QCI的对应关系：

```
%%LST QCI2ARP:;%%
RETCODE = 0  操作成功

结果如下
--------
标准QCI  ARP的可抢占能力  ARP的优先级别  ARP的被抢占能力  

1        0                7              0                
2        0                7              0                
3        0                7              0                
4        0                7              0                
5        0                3              0                
6        1                11             0                
7        1                11             0                
8        1                11             0                
9        1                11             0                
65       0                3              1                
66       0                7              0                
69       0                3              1                
70       0                6              0                
(结果个数 = 13)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询标准QCI到ARP的映射规则（LST-QCI2ARP）_09653066.md`
