---
id: UNC@20.15.2@MMLCommand@LST PDPFILTERCTL
type: MMLCommand
name: LST PDPFILTERCTL（查询PDP过滤功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDPFILTERCTL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- PDP过滤功能
status: active
---

# LST PDPFILTERCTL（查询PDP过滤功能参数）

## 功能

**适用网元：SGSN**

该命令用于查询PDP过滤功能参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPFILTERCTL]] · PDP过滤功能参数（PDPFILTERCTL）

## 使用实例

查询PDP过滤功能参数：

LST PDPFILTERCTL:;

```
%%LST PDPFILTERCTL:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
         过滤开关  =  开启
最大保留的PDP个数  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDPFILTERCTL.md`
