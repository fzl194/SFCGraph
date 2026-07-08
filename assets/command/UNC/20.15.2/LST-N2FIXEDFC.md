---
id: UNC@20.15.2@MMLCommand@LST N2FIXEDFC
type: MMLCommand
name: LST N2FIXEDFC（查询N2接口固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2FIXEDFC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口固定速率流控管理
status: active
---

# LST N2FIXEDFC（查询N2接口固定速率流控信息）

## 功能

**适用NF：AMF**

该命令用于查询N2接口固定速率流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2FIXEDFC]] · N2接口固定速率流控信息（N2FIXEDFC）

## 使用实例

查询N2接口固定速率流控信息，执行如下命令：

```
%%LST N2FIXEDFC:;%%
RETCODE = 0  操作成功

结果如下
--------
       固定速率流控开关  =  开启
    接收速率门限(个/秒)  =  10000
    发送速率门限(个/秒)  =  100000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N2接口固定速率流控信息（LST-N2FIXEDFC）_09651654.md`
