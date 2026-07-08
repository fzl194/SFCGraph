---
id: UDG@20.15.2@MMLCommand@LST FUIFLOWCTLPARA
type: MMLCommand
name: LST FUIFLOWCTLPARA（查询欠费重定向流控参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FUIFLOWCTLPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- FUI重定向控制
- FUI流控参数
status: active
---

# LST FUIFLOWCTLPARA（查询欠费重定向流控参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示欠费重定向流控参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FUIFLOWCTLPARA]] · 欠费重定向流控参数（FUIFLOWCTLPARA）

## 使用实例

显示欠费重定向流控参数，命令如下：

```
LST FUIFLOWCTLPARA:;
```

```

RETCODE = 0  操作成功。

欠费重定向流控参数信息
----------------------
     欠费重定向DNS无配额流控开关  =  使能
欠费重定向临时流量无配额流控开关  =  使能
          单用户流量阈值（字节）  =  5000
                  流控周期（秒）  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FUIFLOWCTLPARA.md`
