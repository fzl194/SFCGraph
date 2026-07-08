---
id: UNC@20.15.2@MMLCommand@DSP VNFSTACKNAMES
type: MMLCommand
name: DSP VNFSTACKNAMES（显示网元下所有堆栈名称）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VNFSTACKNAMES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# DSP VNFSTACKNAMES（显示网元下所有堆栈名称）

## 功能

该命令用于显示网元下所有堆栈名称。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFSTACKNAMES]] · 网元下所有堆栈名称（VNFSTACKNAMES）

## 使用实例

假如操作员想知道网元下有哪些堆栈，可以调用一下命令显示网元下所有的堆栈名称。

```
%%DSP VNFSTACKNAMES:;%%
RETCODE = 0  操作成功

结果如下
--------
堆栈名称               

om-service-fst-manage  
unc-to                 
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示网元下所有堆栈名称（DSP-VNFSTACKNAMES）_78247277.md`
