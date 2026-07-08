---
id: UNC@20.15.2@MMLCommand@LST SMFEMGCFG
type: MMLCommand
name: LST SMFEMGCFG（查询运营商紧急呼叫会话功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFEMGCFG
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 紧急呼叫会话配置
status: active
---

# LST SMFEMGCFG（查询运营商紧急呼叫会话功能配置）

## 功能

**适用NF：SMF**

该命令用于查询指定的MNO或MVNO对应的紧急呼叫会话功能配置数据。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFEMGCFG]] · 运营商紧急呼叫会话功能配置（SMFEMGCFG）

## 使用实例

查询表中全部紧急呼叫会话功能配置的数据，执行如下命令：

```
%%LST SMFEMGCFG: NOID=0;%%
RETCODE = 0  操作成功

结果如下
--------
                            运营商标识  =  0
   紧急会话上行Session AMBR(千比特/秒)  =  20000
   紧急会话下行session AMBR(千比特/秒)  =  40000
                 紧急会话ARP优先级级别  =  1
   紧急会话ARP的Pre-emption Capability  =  不抢占
紧急会话ARP的Pre-emption Vulnerability  =  不可抢占
                      紧急会话创建模式  =  仅限合法用户
                       紧急会话标准5QI  =  5
                 紧急会话5QI的优先级别  =  0
               紧急会话注册UDM功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询运营商紧急呼叫会话功能配置（LST-SMFEMGCFG）_90836434.md`
