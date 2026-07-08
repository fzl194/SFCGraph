---
id: UDG@20.15.2@MMLCommand@DSP TESTRULEMATCH
type: MMLCommand
name: DSP TESTRULEMATCH（查询规则匹配测试结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TESTRULEMATCH
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则匹配测试
- 规则匹配测试
status: active
---

# DSP TESTRULEMATCH（查询规则匹配测试结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用来获取匹配结果。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TESTRULEMATCH]] · 规则匹配测试结果（TESTRULEMATCH）

## 使用实例

显示规则匹配结果：

```
DSP TESTRULEMATCH:;
```

```

RETCODE = 0  Operation succeeded

Rule Match Result Information
-----------------------------
Match Result  =  
                      PCC Policy:
                       Rule Name = rule01
                     Filter Name = filter1l34
                Flow Filter Name = flowfilter1
               PccPolicyGrp Name = pccgp1
                   upUrr(ONLINE) = cbbid-34000
                 upUrrID(ONLINE) = 234000
                   dnUrr(ONLINE) = cbbid-34000
                 dnUrrID(ONLINE) = 234000
                  upUrr(OFFLINE) = cbbid-34000off
                upUrrID(OFFLINE) = 134000
                  dnUrr(OFFLINE) = cbbid-34000off
                dnUrrID(OFFLINE) = 134000

(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询规则匹配测试结果（DSP-TESTRULEMATCH）_90168657.md`
