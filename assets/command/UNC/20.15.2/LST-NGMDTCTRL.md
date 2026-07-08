---
id: UNC@20.15.2@MMLCommand@LST NGMDTCTRL
type: MMLCommand
name: LST NGMDTCTRL（查询5G MDT控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMDTCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G MDT管理
status: active
---

# LST NGMDTCTRL（查询5G MDT控制参数）

## 功能

**适用NF：AMF**

该命令用于查询5G MDT控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMDTCTRL]] · 5G MDT控制参数（NGMDTCTRL）

## 使用实例

查询5G MDT控制参数：

```
%%LST NGMDTCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
基于管理的MDT开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGMDTCTRL.md`
