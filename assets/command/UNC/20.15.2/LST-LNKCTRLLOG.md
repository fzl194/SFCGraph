---
id: UNC@20.15.2@MMLCommand@LST LNKCTRLLOG
type: MMLCommand
name: LST LNKCTRLLOG（查询链路控制消息日志开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LNKCTRLLOG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST LNKCTRLLOG（查询链路控制消息日志开关）

## 功能

**适用NF：AMF**

该命令用于查询链路控制消息日志开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LNKCTRLLOG]] · 链路控制消息日志开关（LNKCTRLLOG）

## 使用实例

若要查询链路控制消息日志开关，可以用如下命令：

```
%%LST LNKCTRLLOG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
SCTP  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询链路控制消息日志开关(LST-LNKCTRLLOG)_13287832.md`
