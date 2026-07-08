---
id: UNC@20.15.2@MMLCommand@LST OFLZEROUSGRPTSW
type: MMLCommand
name: LST OFLZEROUSGRPTSW（查询离线业务零用量容器上报方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OFLZEROUSGRPTSW
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST OFLZEROUSGRPTSW（查询离线业务零用量容器上报方式）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询离线业务零用量容器上报方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFLZEROUSGRPTSW]] · 离线业务零用量容器上报方式（OFLZEROUSGRPTSW）

## 使用实例

查询离线业务零用量容器上报方式：

```
%%LST OFLZEROUSGRPTSW:;%%
RETCODE = 0  操作成功
结果如下
--------
    上报方式  =  上报
上报业务终结  =  使能
上报费率切换  =  使能
     上报QHT  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询离线业务零用量容器上报方式（LST-OFLZEROUSGRPTSW）_89266901.md`
