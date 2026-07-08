---
id: UNC@20.15.2@MMLCommand@DSP NSSFMSGSTAT
type: MMLCommand
name: DSP NSSFMSGSTAT（显示NSSF收发消息内部统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFMSGSTAT
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFMSGSTAT（显示NSSF收发消息内部统计）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF收发消息内部统计。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NSSF收发消息内部统计（NSSFMSGSTAT）](configobject/UNC/20.15.2/NSSFMSGSTAT.md)

## 使用实例

运营商想要查询NSSF收发消息内部统计信息，执行此命令。

```
DSP NSSFMSGSTAT:;
%%DSP NSSFMSGSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
功能实体名称                                      发送消息数目     接收消息数目
[uncpod-0]nssf/cellcore/cell-service-NssfExecSvc  6                6
[uncpod-1]nssf/cellcore/cell-service-NssfExecSvc  0                0
[uncpod-2]nssf/cellcore/cell-service-NssfExecSvc  2                1
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NSSF收发消息内部统计（DSP-NSSFMSGSTAT）_64343868.md`
