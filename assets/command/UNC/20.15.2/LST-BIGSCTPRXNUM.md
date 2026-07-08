---
id: UNC@20.15.2@MMLCommand@LST BIGSCTPRXNUM
type: MMLCommand
name: LST BIGSCTPRXNUM（查询大端模式SCTP接收缓冲区参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BIGSCTPRXNUM
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST BIGSCTPRXNUM（查询大端模式SCTP接收缓冲区参数）

## 功能

**适用网元：MME**

该命令用于查询大端模式SCTP接收缓冲区参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/BIGSCTPRXNUM]] · 大端模式SCTP接收缓冲区参数（BIGSCTPRXNUM）

## 使用实例

查询大端模式SCTP接收缓冲区参数：

LST BIGSCTPRXNUM:;

```
%%LST BIGSCTPRXNUM:;%%
RETCODE = 0  操作成功
输出结果如下
------------------------
私有模式max块数目  =  120
 私有模式耦连个数  =  144
共享模式max块数目  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询大端模式SCTP接收缓冲区参数(LST-BIGSCTPRXNUM)_61676129.md`
