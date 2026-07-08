---
id: UDG@20.15.2@MMLCommand@LST VONRONEWAYSIL
type: MMLCommand
name: LST VONRONEWAYSIL（查询单通检测信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VONRONEWAYSIL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR单通检测
status: active
---

# LST VONRONEWAYSIL（查询单通检测信息）

## 功能

**适用NF：UPF**

该命令用于查询单通检测信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VONRONEWAYSIL]] · 单通检测的系统初始设置值（VONRONEWAYSIL）

## 使用实例

查询单通检测信息：

```
LST VONRONEWAYSIL:;
```

```

RETCODE = 0  操作成功

单通检测信息
------------
               单通检测开关  =  使能（开启）
       单通检测的丢包率门限  =  25
单通检测的连续MOS计算周期数  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VONRONEWAYSIL.md`
