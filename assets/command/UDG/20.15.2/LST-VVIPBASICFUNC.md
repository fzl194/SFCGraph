---
id: UDG@20.15.2@MMLCommand@LST VVIPBASICFUNC
type: MMLCommand
name: LST VVIPBASICFUNC（显示重点业务保障基本功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VVIPBASICFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 重点业务保障基本功能
status: active
---

# LST VVIPBASICFUNC（显示重点业务保障基本功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询重点业务保障基本功能的开关及上报周期等参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VVIPBASICFUNC]] · 重点业务保障基本功能（VVIPBASICFUNC）

## 使用实例

查询当前重点业务保障基本功能的设置：

```
%%LST VVIPBASICFUNC:;
```

```
%%
RETCODE = 0  操作成功

重点业务保障基本功能配置
------------------------
重点业务保障基本功能  =  使能
  质差上报周期（秒）  =  5
非质差上报周期（秒）  =  300
    质差报表上报范围  =  全部上报
  采集单据周期（秒）  =  5
        上报用户类型  =  上报5G用户
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VVIPBASICFUNC.md`
