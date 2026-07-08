---
id: UNC@20.15.2@MMLCommand@LST NGNTNFUNC
type: MMLCommand
name: LST NGNTNFUNC（查询卫星网络接入管理功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGNTNFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 卫星网络接入管理
status: active
---

# LST NGNTNFUNC（查询卫星网络接入管理功能）

## 功能

**适用NF：AMF**

此命令用于查询卫星网络接入管理功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGNTNFUNC]] · 卫星网络接入管理功能（NGNTNFUNC）

## 使用实例

查询卫星网络接入管理功能，执行如下命令：

```
%%LST NGNTNFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
NTN透明模式接入开关  =  YES 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询卫星网络接入管理功能（LST-NGNTNFUNC）_70382325.md`
