---
id: UNC@20.15.2@MMLCommand@LST N2OVERLOAD
type: MMLCommand
name: LST N2OVERLOAD（查询N2过载控制信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2OVERLOAD
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口过载控制
status: active
---

# LST N2OVERLOAD（查询N2过载控制信息）

## 功能

**适用NF：AMF**

此命令用于查询N2过载控制信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [N2过载控制信息（N2OVERLOAD）](configobject/UNC/20.15.2/N2OVERLOAD.md)

## 使用实例

查询N2 Overload Start消息参数：

```
%%LST N2OVERLOAD:;%%
RETCODE = 0  操作成功

结果如下
--------
Overload功能开关  =  OFF
        过载行为  =  不携带Overload Action信元
    拒绝比例指示  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N2过载控制信息（LST-N2OVERLOAD）_09653038.md`
