---
id: UDG@20.15.2@MMLCommand@LST HTTPSTATOBJ
type: MMLCommand
name: LST HTTPSTATOBJ（查询基于对端结点的性能统计测量对象信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPSTATOBJ
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP统计管理
status: active
---

# LST HTTPSTATOBJ（查询基于对端结点的性能统计测量对象信息）

## 功能

该命令用于查询基于对端结点的性能统计测量对象信息，测量对象信息由HTTP消息触发动态生成。

> **说明**
> HTTPSTATOBJ表的记录是业务消息触发动态生成的，但存在"测量对象ID=2999;对端类型=Other;HTTP链路对端地址=Other"的默认记录，在实际“对端类型”及“HTTP链路对端地址”未动态生成场景下，将业务消息统计到默认记录的测量对象，比如测量对象的记录数量超过规格的消息、测量对象创建前的消息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [基于对端结点的性能统计测量对象信息（HTTPSTATOBJ）](configobject/UDG/20.15.2/HTTPSTATOBJ.md)

## 使用实例

如果想查询基于对端结点的性能统计测量对象信息，可以用如下命令：

```
%%LST HTTPSTATOBJ:;%%
RETCODE = 0  操作成功

结果如下
--------
测量对象ID  对端网元类型  对端IP地址           

2999        Other         Other
1           AMF           192.168.111.222   
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询基于对端结点的性能统计测量对象信息（LST-HTTPSTATOBJ）_31878393.md`
