---
id: UNC@20.15.2@MMLCommand@LST NGSMARTDNNCL
type: MMLCommand
name: LST NGSMARTDNNCL（查询智能分流功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGSMARTDNNCL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN智能分流管理
- 智能分流功能管理
status: active
---

# LST NGSMARTDNNCL（查询智能分流功能）

## 功能

**适用NF：AMF**

该命令用于查询智能分流功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGSMARTDNNCL]] · 智能分流功能（NGSMARTDNNCL）

## 使用实例

查询智能分流功能参数，执行如下命令：

```
%%LST NGSMARTDNNCL:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                智能分流开关  =  开启
           DNN智能分流关键字  =  multidomain
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGSMARTDNNCL.md`
