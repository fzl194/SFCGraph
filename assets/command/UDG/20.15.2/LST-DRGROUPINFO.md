---
id: UDG@20.15.2@MMLCommand@LST DRGROUPINFO
type: MMLCommand
name: LST DRGROUPINFO（查询容灾组信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRGROUPINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRGROUPINFO（查询容灾组信息）

## 功能

该命令用于查询容灾组信息。

> **说明**
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识一条容灾组信息，不同容灾组信息的该标识不能相同。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRGROUPINFO]] · 容灾组信息（DRGROUPINFO）

## 使用实例

查询容灾组信息：

```
%%LST DRGROUPINFO: DRGROUPID=1;%%
RETCODE = 0  操作成功

结果如下
--------
              容灾组标识  =  1
              容灾组名称  =  HafGTnGrp
        本端容灾实例标识  =  222
        本端默认运行模式  =  配置主
        对端容灾实例标识  =  111
对端容灾控制通道IPv4地址  =  0.0.0.0
对端容灾控制通道IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容灾组信息（LST-DRGROUPINFO）_74835153.md`
