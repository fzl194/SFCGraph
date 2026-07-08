---
id: UNC@20.15.2@MMLCommand@LST NGCHRSTORCFG
type: MMLCommand
name: LST NGCHRSTORCFG（查询AMF小范围CHR存储配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGCHRSTORCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入小范围CHR配置
status: active
---

# LST NGCHRSTORCFG（查询AMF小范围CHR存储配置）

## 功能

**适用NF：AMF**

该命令用于查询AMF小范围CHR存储配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGCHRSTORCFG]] · AMF小范围CHR存储配置（NGCHRSTORCFG）

## 使用实例

查询当前AMF小范围CHR存储配置，执行如下命令：

```
%%LST NGCHRSTORCFG:;%%
RETCODE = 0  操作成功

输出结果如下
------------
小范围CHR使能开关  =  使能
小范围CHR存储路径  =  保存到OMU
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGCHRSTORCFG.md`
