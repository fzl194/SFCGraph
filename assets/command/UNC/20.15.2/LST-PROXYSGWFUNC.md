---
id: UNC@20.15.2@MMLCommand@LST PROXYSGWFUNC
type: MMLCommand
name: LST PROXYSGWFUNC（查询Proxy SGW功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROXYSGWFUNC
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SGW-C功能参数
status: active
---

# LST PROXYSGWFUNC（查询Proxy SGW功能参数）

## 功能

**适用NF：SGW-C**

该命令用于查询Proxy S-GW特性的功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [Proxy SGW功能参数（PROXYSGWFUNC）](configobject/UNC/20.15.2/PROXYSGWFUNC.md)

## 使用实例

查询Proxy S-GW特性的功能参数：

```
%%LST PROXYSGWFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           查询类型  =  IMSI优先
           控制类型  =  拒绝
           解析方式  =  本地配置优先
       是否允许4切2  =  使能
    透传NSA流量开关  =  使能
透传5GSIWKI标志开关  =  使能
 透传5GCNRI标志开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Proxy-SGW功能参数（LST-PROXYSGWFUNC）_06399915.md`
