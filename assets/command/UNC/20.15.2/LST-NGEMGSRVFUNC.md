---
id: UNC@20.15.2@MMLCommand@LST NGEMGSRVFUNC
type: MMLCommand
name: LST NGEMGSRVFUNC（查询5G紧急服务功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGEMGSRVFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- 紧急呼叫业务管理
- 紧急服务功能配置
status: active
---

# LST NGEMGSRVFUNC（查询5G紧急服务功能）

## 功能

**适用NF：AMF**

该命令用于查询5G紧急服务功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGEMGSRVFUNC]] · 5G紧急服务功能（NGEMGSRVFUNC）

## 使用实例

查询5G紧急服务功能，执行如下命令：

```
%%LST NGEMGSRVFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
本网用户是否允许紧急呼叫业务  =  NR接入的紧急呼叫回落
本网用户紧急号码列表下发开关  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G紧急服务功能（LST-NGEMGSRVFUNC）_64061200.md`
