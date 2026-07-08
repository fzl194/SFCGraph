---
id: UDG@20.15.2@MMLCommand@LST EXPBASICFUNC
type: MMLCommand
name: LST EXPBASICFUNC（查询体验业务基本功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EXPBASICFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 体验分析基本功能
status: active
---

# LST EXPBASICFUNC（查询体验业务基本功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询体验业务基本功能的开关及上报周期等参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [体验业务基本功能（EXPBASICFUNC）](configobject/UDG/20.15.2/EXPBASICFUNC.md)

## 使用实例

查询当前体验业务基本功能的设置：

```
%%LST EXPBASICFUNC:;
```

```
%%
RETCODE = 0  操作成功

查询体验业务基本功能
--------------------
          体验分析基本功能  =  使能
      体验业务上报周期（秒）=  300
体验业务上报的服务器端口号  =  15000
      体验单据采集周期（秒）=  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询体验业务基本功能（LST-EXPBASICFUNC）_72322914.md`
